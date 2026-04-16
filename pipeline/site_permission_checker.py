"""
pipeline/site_permission_checker.py  v1.2.0

Checks each site in kb_sites.toml for permission to scrape or reference content.

Design philosophy — fail safe:
  - Unknown robots.txt (timeout / connection error) is NOT treated as "allowed".
  - Missing robots.txt (HTTP 404) follows RFC 9309: conventional permission,
    but confidence is capped at "medium" — it is NOT explicit permission.
  - Every HTTP interaction is recorded (status code, error type, latency).
  - Both allow AND block keyword hits include ±150-char context sentences for human review.
  - Confidence is set by evidence quality, not by optimistic assumptions.
  - 10 parallel workers run concurrently (thread-local sessions for safety).

Checks performed per site:
  1. robots.txt   — urllib.robotparser; tracks present/absent/unreachable separately
  2. Homepage HTML — license/CC markers in <meta>, footer, <head>
  3. T&C discovery — heuristic link finder + common path fallback
  4. Keyword scoring — allow/block signals on T&C text with context extraction
  5. Public-domain override  — .gov.in / .gov / known open-access institutions
  6. API-only override       — Reddit (PRAW), GitHub, YouTube

Verdicts (conservative → liberal):
  ALLOWED         — explicit permission: public domain / open license / robots + positive T&C
  ALLOWED_VIA_API — use official API only; no direct scraping
  MANUAL_REVIEW   — ambiguous evidence; human decision required before any scraping
  SERP_ONLY       — robots or T&C restricts direct scraping; reference via SerpAPI only
  BLOCKED         — explicit prohibition in both robots.txt AND T&C
  UNREACHABLE     — site did not respond after all retries

Confidence levels:
  high   — multiple strong signals in agreement (e.g. .gov.in + open license)
  medium — single reliable signal (robots allows but T&C ambiguous; or 404 robots)
  low    — signals conflict or are absent; human must verify

Usage:
  python pipeline/site_permission_checker.py
  python pipeline/site_permission_checker.py --site zerodha_varsity
  python pipeline/site_permission_checker.py --tier 1
  python pipeline/site_permission_checker.py --category A
  python pipeline/site_permission_checker.py --dry-run
  python pipeline/site_permission_checker.py --workers 10
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
import threading
import time
import tomllib
import urllib.robotparser
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import tomli_w
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT       = Path(__file__).parent
SITES_FILE = ROOT / "kb_sites.toml"
DATA_DIR   = ROOT / "data"
CACHE_DIR  = ROOT / "cache"
LOGS_DIR   = ROOT / "logs"

DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

OUTPUT_TOML   = DATA_DIR / "permissible_sites.toml"
OUTPUT_REPORT = DATA_DIR / "permission_report.md"

# ---------------------------------------------------------------------------
# Logging  (UTF-8 on file; stdout uses replace for Windows cp1252)
# ---------------------------------------------------------------------------
_stream_handler = logging.StreamHandler(sys.stdout)
_stream_handler.stream.reconfigure(errors="replace")  # type: ignore[attr-defined]
_file_handler   = logging.FileHandler(LOGS_DIR / "permission_check.log", encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  [%(threadName)s]  %(message)s",
    handlers=[_stream_handler, _file_handler],
)
log = logging.getLogger("permission_checker")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
TOOL_VERSION   = "1.2.0"
BOT_AGENT      = "FinAwareBot/1.0 (educational; +https://fin-aware.in/bot)"
HEADERS        = {"User-Agent": BOT_AGENT, "Accept-Language": "en-US,en;q=0.9"}
DELAY          = 1.5          # seconds between outbound requests per thread
TIMEOUT        = 12           # seconds per HTTP request
MAX_RETRIES    = 3
CONTEXT_WINDOW = 150          # chars either side of matched keyword for context
DEFAULT_WORKERS = 10

# Allow signals — words that suggest reproduction / educational use is permitted
ALLOW_SIGNALS: list[str] = [
    "educational use",
    "non-commercial",
    "freely accessible",
    "open license",
    "creative commons",
    "public domain",
    "may reproduce",
    "attribution",
    "cc by",
    "open access",
    "freely available",
    "permitted for",
    "free to use",
    "share alike",
    "research purposes",
    "personal use",
    "non-profit",
]

# Block signals — words that suggest scraping / reproduction is prohibited
BLOCK_SIGNALS: list[str] = [
    "no scraping",
    "no crawling",
    "no automated",
    "do not copy",
    "strictly prohibited",
    "unauthorized access",
    "all rights reserved",
    "may not reproduce",
    "systematic download",
    "data mining",
    "scraping is prohibited",
    "prohibited from",
    "not permitted to",
    "you may not",
    "expressly prohibited",
]

# Open-license patterns to search in page HTML
LICENSE_PATTERNS: list[tuple[str, str]] = [
    (r"creativecommons\.org/licenses/by(?:-nc)?(?:-sa)?(?:-nd)?/", "CC BY"),
    (r"creativecommons\.org/publicdomain/zero",                    "CC0 / Public Domain"),
    (r"open\s+data\s+commons",                                     "Open Data Commons"),
    (r"\bmit\s+license\b",                                         "MIT"),
    (r"\bapache[\s-]+2\.0\b",                                      "Apache 2.0"),
    (r"\bgnu\s+gpl\b",                                             "GPL"),
    (r"\bpublic\s+domain\b",                                       "Public Domain"),
]

# Unconditionally public domain / open access
PUBLIC_DOMAIN_OVERRIDES: set[str] = {
    "sebi.gov.in", "investor.sebi.gov.in",
    "rbi.org.in",
    "amfiindia.com",
    "nseindia.com",
    "bseindia.com",
    "nism.ac.in",
    "irdai.gov.in",
    "pfrda.org.in",
    "npstrust.org.in",
    "epfindia.gov.in",
    "incometaxindia.gov.in",
    "incometax.gov.in",
    "itat.gov.in",
    "finmin.nic.in",
    "mca.gov.in",
    "ibbi.gov.in",
    "mospi.gov.in",
    "nabard.org",
    "gstcouncil.gov.in",
    "gst.gov.in",
    "arxiv.org",
    "quantecon.org",
    "imf.org",
    "worldbank.org",
    "federalreserve.gov",
    "sec.gov",
    "ecb.europa.eu",
    "oecd.org",
    "bis.org",
}

# Must be accessed via official API only
API_ONLY_OVERRIDES: set[str] = {
    "reddit.com", "www.reddit.com",
    "github.com", "raw.githubusercontent.com",
    "youtube.com", "www.youtube.com",
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class SiteRecord:
    id:         str
    name:       str
    base_url:   str
    scrape_url: str
    tier:       int
    domains:    list[str]
    levels:     list[str]
    extraction: str
    category:   str
    notes:      str = ""


@dataclass
class FetchAttempt:
    """Record of a single HTTP fetch attempt."""
    url:          str
    purpose:      str           # "robots" | "homepage" | "tos_discovery" | "tos_page"
    status_code:  int | None    # None if no response received
    error_type:   str           # "" | "timeout" | "connection" | "http_4xx" | "http_5xx" | "ssl" | "other"
    error_detail: str
    latency_ms:   int

    def to_dict(self) -> dict:
        return {
            "url":          self.url,
            "purpose":      self.purpose,
            # TOML has no null type — use 0 when no HTTP response was received
            "status_code":  self.status_code if self.status_code is not None else 0,
            "error_type":   self.error_type,
            "error_detail": self.error_detail,
            "latency_ms":   self.latency_ms,
        }


@dataclass
class CheckResult:
    id:          str
    name:        str
    base_url:    str
    scrape_url:  str
    tier:        int
    extraction:  str
    category:    str

    # --- robots.txt ---
    robots_status: str = "unknown"
    # "found"       — fetched and parsed
    # "not_found"   — HTTP 404; no file (RFC 9309 conventional allow, NOT explicit)
    # "unreachable" — timeout/connection/SSL (cannot determine)
    # "skipped"     — fast-path (API-only / dry-run)
    robots_allows:       bool = False   # True ONLY when found AND permits scraping
    robots_denies:       bool = False   # True ONLY when found AND denies scraping
    crawl_delay_seconds: int  = 0

    # --- Homepage ---
    homepage_status:  str = "unknown"   # "ok" | "error" | "skipped"
    license_detected: str = ""

    # --- T&C ---
    tos_status: str = "unknown"         # "found" | "not_found" | "skipped"
    tos_url:    str = ""
    tos_denies: bool = False            # True when block_signals found in T&C text

    # --- Keyword scoring ---
    allow_signals:         list[str]       = field(default_factory=list)
    allow_signal_contexts: dict[str, str]  = field(default_factory=dict)
    block_signals:         list[str]       = field(default_factory=list)
    block_signal_contexts: dict[str, str]  = field(default_factory=dict)
    permission_score:      int             = 0

    # --- Verdict ---
    verdict:        str = "MANUAL_REVIEW"
    confidence:     str = "low"
    verdict_reason: str = ""

    # --- Audit trail ---
    fetch_log:    list[FetchAttempt] = field(default_factory=list)
    checked_at:   str = ""
    source_notes: str = ""

    def to_dict(self) -> dict:
        return {
            "id":                     self.id,
            "name":                   self.name,
            "base_url":               self.base_url,
            "scrape_url":             self.scrape_url,
            "tier":                   self.tier,
            "extraction":             self.extraction,
            "category":               self.category,
            "robots_status":          self.robots_status,
            "robots_allows":          self.robots_allows,
            "robots_denies":          self.robots_denies,
            "crawl_delay_seconds":    self.crawl_delay_seconds,
            "homepage_status":        self.homepage_status,
            "license_detected":       self.license_detected,
            "tos_status":             self.tos_status,
            "tos_url":                self.tos_url,
            "tos_denies":             self.tos_denies,
            "allow_signals":          self.allow_signals,
            "allow_signal_contexts":  self.allow_signal_contexts,
            "block_signals":          self.block_signals,
            "block_signal_contexts":  self.block_signal_contexts,
            "permission_score":       self.permission_score,
            "verdict":                self.verdict,
            "confidence":             self.confidence,
            "verdict_reason":         self.verdict_reason,
            "fetch_log":              [f.to_dict() for f in self.fetch_log],
            "checked_at":             self.checked_at,
            "source_notes":           self.source_notes,
        }


# ---------------------------------------------------------------------------
# Thread-local state  (one session + one worker-id per physical thread)
# ---------------------------------------------------------------------------
_thread_local      = threading.local()
_cache_lock        = threading.Lock()   # guards concurrent cache file writes
_worker_id_counter = 0
_worker_id_lock    = threading.Lock()   # guards worker-id assignment


def _assign_worker_id() -> int:
    """
    Assign a stable sequential number (1-based) to the calling thread.
    Called once when a worker thread first picks up a task; the same thread
    keeps the same W-NN label for its entire lifetime in the pool.
    """
    global _worker_id_counter
    if not hasattr(_thread_local, "worker_id"):
        with _worker_id_lock:
            _worker_id_counter += 1
            _thread_local.worker_id = _worker_id_counter
        threading.current_thread().name = f"W-{_thread_local.worker_id:02d}"
    return _thread_local.worker_id


def _get_session() -> requests.Session:
    """One requests.Session per physical worker thread (not shared)."""
    if not hasattr(_thread_local, "session"):
        s = requests.Session()
        s.headers.update(HEADERS)
        _thread_local.session = s
    return _thread_local.session


def _fetch(
    url:                str,
    purpose:            str,
    fetch_log:          list[FetchAttempt],
    allow_ssl_fallback: bool = True,
) -> requests.Response | None:
    """
    Fetch a URL with retries.  Every attempt is recorded in fetch_log.
    Returns the successful Response, or None on failure.
    """
    session = _get_session()

    def _record(status_code, error_type, error_detail, t0):
        fetch_log.append(FetchAttempt(
            url=url, purpose=purpose,
            status_code=status_code,
            error_type=error_type,
            error_detail=error_detail,
            latency_ms=int((time.monotonic() - t0) * 1000),
        ))

    for attempt in range(1, MAX_RETRIES + 1):
        t0 = time.monotonic()
        try:
            resp = session.get(url, timeout=TIMEOUT, allow_redirects=True)
            if resp.status_code == 404:
                _record(404, "http_4xx", "Not Found", t0)
                log.info("  [http] 404 %s (%s)", url, purpose)
                return resp
            resp.raise_for_status()
            _record(resp.status_code, "", "", t0)
            return resp

        except requests.exceptions.SSLError as exc:
            _record(None, "ssl", str(exc), t0)
            log.warning("  [http] SSL error [%d/%d] %s: %s", attempt, MAX_RETRIES, url, exc)
            if allow_ssl_fallback and attempt == MAX_RETRIES:
                t0 = time.monotonic()
                try:
                    resp = session.get(url, timeout=TIMEOUT, verify=False, allow_redirects=True)  # noqa: S501
                    resp.raise_for_status()
                    _record(resp.status_code, "ssl_fallback", "verify=False used", t0)
                    log.warning("  [http] SSL fallback succeeded for %s", url)
                    return resp
                except Exception as exc2:
                    _record(None, "ssl", str(exc2), t0)
                    log.error("  [http] SSL fallback also failed for %s: %s", url, exc2)
                    return None

        except requests.exceptions.Timeout as exc:
            _record(None, "timeout", str(exc), t0)
            log.warning("  [http] Timeout [%d/%d] %s", attempt, MAX_RETRIES, url)

        except requests.exceptions.ConnectionError as exc:
            _record(None, "connection", str(exc), t0)
            log.warning("  [http] Connection error [%d/%d] %s: %s", attempt, MAX_RETRIES, url, exc)

        except requests.exceptions.HTTPError as exc:
            code  = exc.response.status_code if exc.response is not None else None
            etype = f"http_{code // 100}xx" if code else "http_error"
            _record(code, etype, str(exc), t0)
            log.warning("  [http] HTTP %s for %s (%s)", code, url, purpose)
            return None

        except Exception as exc:
            _record(None, "other", str(exc), t0)
            log.warning("  [http] Unexpected [%d/%d] %s: %s", attempt, MAX_RETRIES, url, exc)

        if attempt < MAX_RETRIES:
            time.sleep(DELAY * attempt)

    return None


def _polite_sleep() -> None:
    time.sleep(DELAY)


# ---------------------------------------------------------------------------
# robots.txt
# ---------------------------------------------------------------------------
def check_robots(
    site:      SiteRecord,
    fetch_log: list[FetchAttempt],
    cache_dir: Path,
) -> tuple[bool, bool, int, str]:
    """
    Returns (allows: bool, denies: bool, crawl_delay: int, status: str).

    status:
      "found"       — parsed successfully; allows/denies reflect actual rules
      "not_found"   — HTTP 404; no robots.txt (RFC 9309: conventional allow, NOT explicit)
      "unreachable" — network/SSL error; permission truly unknown

    Safe defaults when status != "found":
      allows=True  for not_found (RFC 9309 convention)
      allows=False for unreachable (fail-safe)
    """
    robots_url = urljoin(site.base_url.rstrip("/") + "/", "robots.txt")
    log.info("  [robots] %s", robots_url)
    _polite_sleep()
    resp = _fetch(robots_url, "robots", fetch_log)

    if resp is None:
        log.warning("  [robots] UNREACHABLE — permission unknown, safe default: deny")
        return False, False, 0, "unreachable"

    if resp.status_code == 404:
        log.info("  [robots] NOT FOUND (404) — conventional allow per RFC 9309")
        return True, False, 0, "not_found"

    raw = resp.text
    _cache_write(cache_dir, site.id, "robots.txt", raw)

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.parse(raw.splitlines())

    allows_wildcard  = rp.can_fetch("*", site.scrape_url)
    allows_specific  = rp.can_fetch(BOT_AGENT.split("/")[0], site.scrape_url)
    allows  = allows_wildcard or allows_specific
    denies  = not allows

    crawl_delay = 0
    m = re.search(r"(?i)crawl-delay\s*:\s*(\d+)", raw)
    if m:
        crawl_delay = int(m.group(1))

    log.info(
        "  [robots] FOUND — allows=%s (wildcard=%s specific=%s) delay=%ds",
        allows, allows_wildcard, allows_specific, crawl_delay,
    )
    return allows, denies, crawl_delay, "found"


# ---------------------------------------------------------------------------
# T&C discovery
# ---------------------------------------------------------------------------
TOS_LINK_KEYWORDS = re.compile(
    r"\b(terms|tos|privacy|legal|policy|license|licence|copyright|disclaimer|conditions)\b",
    re.IGNORECASE,
)

TOS_COMMON_PATHS = [
    "/terms", "/terms-of-use", "/terms-of-service", "/tos",
    "/privacy", "/privacy-policy", "/legal", "/copyright",
    "/license", "/disclaimer", "/about/legal", "/about/terms",
]


def discover_tos_url(
    site:          SiteRecord,
    fetch_log:     list[FetchAttempt],
    homepage_html: str,
) -> tuple[str, str]:
    """Returns (tos_url, tos_status).  tos_status: "found" | "not_found"."""
    candidates: list[tuple[int, str]] = []

    if homepage_html:
        soup = BeautifulSoup(homepage_html, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = str(a_tag["href"])
            text = a_tag.get_text(strip=True)
            combined = href + " " + text
            if TOS_LINK_KEYWORDS.search(combined):
                abs_url = urljoin(site.base_url, href)
                score   = 2 if re.search(r"\bterms\b", combined, re.I) else 1
                candidates.append((score, abs_url))

    for path in TOS_COMMON_PATHS:
        candidates.append((0, urljoin(site.base_url, path)))

    seen: set[str] = set()
    ordered: list[str] = []
    for _, url in sorted(candidates, reverse=True):
        if url not in seen:
            seen.add(url)
            ordered.append(url)

    for url in ordered[:6]:
        _polite_sleep()
        resp = _fetch(url, "tos_page", fetch_log)
        if resp and resp.status_code == 200 and len(resp.text) > 500:
            log.info("  [tos] Found: %s", url)
            return url, "found"

    log.info("  [tos] Not found for %s", site.id)
    return "", "not_found"


def fetch_tos_text(
    url:       str,
    site_id:   str,
    fetch_log: list[FetchAttempt],
    cache_dir: Path,
) -> str:
    if not url:
        return ""
    _polite_sleep()
    resp = _fetch(url, "tos_page", fetch_log)
    if resp is None or resp.status_code != 200:
        return ""
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(separator=" ", strip=True)[:10_000]
    _cache_write(cache_dir, site_id, "tos_snippet.txt", text)
    return text


# ---------------------------------------------------------------------------
# Keyword scoring — context extracted for BOTH allow and block signals
# ---------------------------------------------------------------------------
def _extract_context(text: str, signal: str, window: int = CONTEXT_WINDOW) -> str:
    """Return ±window-char snippet around first occurrence of signal."""
    idx = text.lower().find(signal.lower())
    if idx < 0:
        return ""
    start   = max(0, idx - window)
    end     = min(len(text), idx + len(signal) + window)
    snippet = re.sub(r"\s+", " ", text[start:end].strip())
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."
    return snippet


def score_tos(
    text: str,
) -> tuple[list[str], dict[str, str], list[str], dict[str, str], int]:
    """
    Returns:
      allow_hits, allow_contexts, block_hits, block_contexts, net_score

    Both allow and block contexts contain ±CONTEXT_WINDOW-char snippets
    around each matched keyword, for human review in the report.
    """
    text_lower = text.lower()
    allow_hits:     list[str]      = []
    allow_contexts: dict[str, str] = {}
    block_hits:     list[str]      = []
    block_contexts: dict[str, str] = {}

    for sig in ALLOW_SIGNALS:
        if sig in text_lower:
            allow_hits.append(sig)
            allow_contexts[sig] = _extract_context(text, sig)

    for sig in BLOCK_SIGNALS:
        if sig in text_lower:
            block_hits.append(sig)
            block_contexts[sig] = _extract_context(text, sig)

    return allow_hits, allow_contexts, block_hits, block_contexts, len(allow_hits) - len(block_hits)


# ---------------------------------------------------------------------------
# License detection
# ---------------------------------------------------------------------------
def detect_license(html: str) -> str:
    for pattern, label in LICENSE_PATTERNS:
        if re.search(pattern, html, re.IGNORECASE):
            return label
    return ""


# ---------------------------------------------------------------------------
# Verdict logic
# ---------------------------------------------------------------------------
def compute_verdict(
    site:             SiteRecord,
    robots_allows:    bool,
    robots_denies:    bool,
    robots_status:    str,
    allow_hits:       list[str],
    block_hits:       list[str],
    score:            int,
    license_detected: str,
    fetch_log:        list[FetchAttempt],
) -> tuple[str, str, str]:
    """
    Returns (verdict, confidence, reason).

    IDENTITY-BASED OVERRIDES (before any connectivity checks):
      1. API-only              -> ALLOWED_VIA_API  / high
      2. Public domain/.gov.in -> ALLOWED           / high  (access issues noted)
      3. Explicit open license -> ALLOWED           / high

    CONNECTIVITY-BASED (non-gov, non-API sites only):
      4a. All retries failed   -> UNREACHABLE       / high
      4b. 403 bot-block        -> SERP_ONLY         / high
      5.  robots found+denies  -> depends on T&C
      6.  robots unreachable   -> MANUAL_REVIEW     / low
      7.  robots not found     -> conventional allow, capped medium
      8.  robots found+allows  -> depends on T&C
    """
    domain   = urlparse(site.base_url).hostname or ""
    stripped = domain.lstrip("www.")

    # ── 1: API-only ──
    if stripped in API_ONLY_OVERRIDES or domain in API_ONLY_OVERRIDES:
        return (
            "ALLOWED_VIA_API", "high",
            f"Official API available ({site.extraction}). No direct scraping needed or permitted.",
        )

    # ── 2: Public domain / government ──
    is_gov_in     = stripped.endswith(".gov.in")
    is_gov_us     = stripped.endswith(".gov")
    is_known_open = stripped in PUBLIC_DOMAIN_OVERRIDES
    if is_gov_in or is_gov_us or is_known_open:
        reason = "Government portal — public domain" if (is_gov_in or is_gov_us) \
                 else "Known open-access institution"
        if license_detected:
            reason += f"; open license: {license_detected}"
        access_issues = sorted({
            f.error_type or f"HTTP {f.status_code}"
            for f in fetch_log
            if f.error_type or (f.status_code and f.status_code >= 400)
        })
        if access_issues:
            reason += (
                f". NOTE: access issues during check ({', '.join(access_issues)})"
                " — scraper may need custom headers or retry logic"
            )
        return "ALLOWED", "high", reason

    # ── 3: Explicit open license ──
    if license_detected in ("CC0 / Public Domain", "MIT", "Apache 2.0", "CC BY"):
        return "ALLOWED", "high", f"Explicit open license detected: {license_detected}"

    # ── 4a: Site completely unreachable ──
    net_errs     = sum(1 for f in fetch_log if f.purpose == "homepage"
                       and f.error_type in ("timeout", "connection", "ssl", "other")
                       and f.status_code is None)
    home_attempts = sum(1 for f in fetch_log if f.purpose == "homepage")
    if home_attempts > 0 and net_errs == home_attempts:
        return (
            "UNREACHABLE", "high",
            f"Homepage unreachable after {home_attempts} attempt(s): "
            + ", ".join(f.error_type for f in fetch_log if f.purpose == "homepage"),
        )

    # ── 4b: Server actively blocks bot (403 homepage + 403/401 all T&C) ──
    home_403 = any(f.purpose == "homepage" and f.status_code == 403 for f in fetch_log)
    tos_attempts = [f for f in fetch_log if f.purpose == "tos_page"]
    tos_all_4xx  = (
        bool(tos_attempts)
        and all(f.status_code in (401, 403) for f in tos_attempts)
    )
    if home_403 and tos_all_4xx:
        return (
            "SERP_ONLY", "high",
            "Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). "
            "robots.txt may say 'allow' but practical access is blocked — use SERP API only.",
        )

    # ── 5: robots found AND denies ──
    if robots_status == "found" and robots_denies:
        if score <= -3:
            return (
                "BLOCKED", "high",
                f"robots.txt disallows scraping; T&C strongly prohibits (score={score}, "
                f"block signals: {block_hits})",
            )
        if score <= -1:
            return (
                "SERP_ONLY", "high",
                f"robots.txt disallows scraping; T&C restricts reproduction (score={score})",
            )
        return (
            "MANUAL_REVIEW", "medium",
            f"robots.txt disallows scraping BUT T&C is neutral/positive (score={score}) "
            "— contact site owner for written permission",
        )

    # ── 6: robots unreachable ──
    if robots_status == "unreachable":
        if score >= 2 and license_detected:
            return (
                "MANUAL_REVIEW", "medium",
                f"robots.txt unreachable; T&C positive (score={score}) + license={license_detected} "
                "— promising but not confirmed; contact site owner",
            )
        if score <= -1:
            return (
                "SERP_ONLY", "medium",
                f"robots.txt unreachable AND T&C restricts (score={score})",
            )
        return (
            "MANUAL_REVIEW", "low",
            "robots.txt unreachable — cannot determine crawling policy; "
            "contact site owner before scraping",
        )

    # ── 7: robots not found (404) — RFC 9309 conventional allow ──
    if robots_status == "not_found":
        if score <= -2:
            return (
                "SERP_ONLY", "medium",
                f"No robots.txt (conventional allow, NOT explicit); T&C restricts (score={score})",
            )
        if score == -1:
            return (
                "MANUAL_REVIEW", "medium",
                f"No robots.txt; T&C mildly restrictive (score={score}) — verify before scraping",
            )
        if score >= 1:
            return (
                "ALLOWED", "medium",
                f"No robots.txt (conventional allow); T&C positive (score={score}); "
                f"license={license_detected or 'none'} — confidence capped at medium",
            )
        return (
            "MANUAL_REVIEW", "medium",
            "No robots.txt; T&C ambiguous (score=0) — contact site owner before scraping",
        )

    # ── 8: robots found AND allows ──
    if robots_status == "found" and robots_allows:
        if score <= -2:
            return (
                "SERP_ONLY", "medium",
                f"robots.txt allows BUT T&C restricts reproduction (score={score}) "
                "— technical access != legal permission",
            )
        if score == -1:
            return (
                "MANUAL_REVIEW", "medium",
                f"robots.txt allows; T&C mildly restrictive (score={score}) "
                "— seek written confirmation for any reproduction",
            )
        if score >= 2:
            conf = "high" if license_detected else "medium"
            return (
                "ALLOWED", conf,
                f"robots.txt allows; T&C positive (score={score}); "
                f"license={license_detected or 'none'}",
            )
        if score == 1:
            return (
                "ALLOWED", "medium",
                f"robots.txt allows; T&C mildly positive (score={score}); "
                f"license={license_detected or 'none'} — monitor for policy changes",
            )
        return (
            "MANUAL_REVIEW", "medium",
            "robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping",
        )

    return (
        "MANUAL_REVIEW", "low",
        f"Unhandled case: robots_status={robots_status} robots_allows={robots_allows} score={score}",
    )


# ---------------------------------------------------------------------------
# Cache helpers (thread-safe)
# ---------------------------------------------------------------------------
def _cache_write(cache_dir: Path, site_id: str, filename: str, content: str) -> None:
    with _cache_lock:
        site_cache = cache_dir / site_id
        site_cache.mkdir(exist_ok=True)
        (site_cache / filename).write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Per-site check  (called from thread pool workers)
# ---------------------------------------------------------------------------
def check_site(site: SiteRecord, dry_run: bool = False) -> CheckResult:
    now    = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    result = CheckResult(
        id           = site.id,
        name         = site.name,
        base_url     = site.base_url,
        scrape_url   = site.scrape_url,
        tier         = site.tier,
        extraction   = site.extraction,
        category     = site.category,
        checked_at   = now,
        source_notes = site.notes,
    )

    domain   = urlparse(site.base_url).hostname or ""
    stripped = domain.lstrip("www.")

    # ── Fast-path: API-only ──
    if stripped in API_ONLY_OVERRIDES or domain in API_ONLY_OVERRIDES:
        result.robots_status   = "skipped"
        result.homepage_status = "skipped"
        result.tos_status      = "skipped"
        result.robots_allows   = True
        result.verdict         = "ALLOWED_VIA_API"
        result.confidence      = "high"
        result.verdict_reason  = f"Official API available ({site.extraction}). No direct scraping needed."
        log.info("  [verdict] %s -> ALLOWED_VIA_API", site.id)
        return result

    if dry_run:
        result.robots_status   = "skipped"
        result.tos_status      = "skipped"
        result.homepage_status = "skipped"
        result.verdict         = "DRY_RUN"
        result.confidence      = "n/a"
        result.verdict_reason  = "Dry-run — no HTTP requests made"
        return result

    try:
        # Step 1 — Homepage
        log.info("  [home] %s", site.base_url)
        _polite_sleep()
        home_resp = _fetch(site.base_url, "homepage", result.fetch_log)
        if home_resp and home_resp.status_code == 200:
            homepage_html           = home_resp.text
            result.homepage_status  = "ok"
            result.license_detected = detect_license(homepage_html)
        else:
            homepage_html           = ""
            result.homepage_status  = "error"

        # Step 2 — robots.txt
        r_allows, r_denies, r_delay, r_status = check_robots(site, result.fetch_log, CACHE_DIR)
        result.robots_allows       = r_allows
        result.robots_denies       = r_denies
        result.crawl_delay_seconds = r_delay
        result.robots_status       = r_status

        # Step 3 — T&C URL discovery
        tos_url, tos_status = discover_tos_url(site, result.fetch_log, homepage_html)
        result.tos_url    = tos_url
        result.tos_status = tos_status

        # Step 4 — T&C text + keyword scoring
        tos_text = fetch_tos_text(tos_url, site.id, result.fetch_log, CACHE_DIR)
        allow_hits, allow_ctx, block_hits, block_ctx, score = score_tos(tos_text)

        result.allow_signals         = allow_hits
        result.allow_signal_contexts = allow_ctx
        result.block_signals         = block_hits
        result.block_signal_contexts = block_ctx
        result.permission_score      = score
        result.tos_denies            = bool(block_hits)

        # Step 5 — Verdict
        verdict, confidence, reason = compute_verdict(
            site, r_allows, r_denies, r_status,
            allow_hits, block_hits, score,
            result.license_detected, result.fetch_log,
        )
        result.verdict        = verdict
        result.confidence     = confidence
        result.verdict_reason = reason

    except Exception as exc:
        log.error("  [error] %s: %s", site.id, exc, exc_info=True)
        result.verdict        = "UNREACHABLE"
        result.confidence     = "high"
        result.verdict_reason = f"Unexpected exception: {exc}"

    log.info(
        "  [verdict] %-35s -> %-20s confidence=%-6s score=%+d "
        "robots=%s tos=%s license=%s",
        site.id, result.verdict, result.confidence, result.permission_score,
        result.robots_status, result.tos_status, result.license_detected or "none",
    )
    return result


# ---------------------------------------------------------------------------
# TOML output
# ---------------------------------------------------------------------------
VERDICT_ORDER = ["ALLOWED", "ALLOWED_VIA_API", "MANUAL_REVIEW", "SERP_ONLY", "BLOCKED", "UNREACHABLE"]


def _toml_safe(obj: object) -> object:
    """
    Recursively replace values that TOML cannot serialise.
    TOML has no null type — None becomes "" (string context) or 0 (numeric context).
    We default to "" which is safe for all string/mixed fields.
    Booleans must stay as bool (not coerced to int by mistake), so check bool first.
    """
    if obj is None:
        return ""
    if isinstance(obj, bool):
        return obj
    if isinstance(obj, dict):
        return {k: _toml_safe(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_toml_safe(v) for v in obj]
    return obj


def write_toml(results: list[CheckResult]) -> None:
    by_verdict: dict[str, list[dict]] = {v: [] for v in VERDICT_ORDER}
    for r in results:
        key = r.verdict if r.verdict in by_verdict else "MANUAL_REVIEW"
        by_verdict[key].append(r.to_dict())

    counts = {
        "allowed":         len(by_verdict["ALLOWED"]),
        "allowed_via_api": len(by_verdict["ALLOWED_VIA_API"]),
        "manual_review":   len(by_verdict["MANUAL_REVIEW"]),
        "serp_only":       len(by_verdict["SERP_ONLY"]),
        "blocked":         len(by_verdict["BLOCKED"]),
        "unreachable":     len(by_verdict["UNREACHABLE"]),
    }
    doc = {
        "meta": {
            "generated_at":  datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
            "tool_version":  TOOL_VERSION,
            "total_checked": len(results),
            **counts,
        },
        "sites": {v.lower(): by_verdict[v] for v in VERDICT_ORDER},
    }
    # Sanitise: TOML has no null type; replace all None values before serialising
    doc = _toml_safe(doc)
    OUTPUT_TOML.write_bytes(tomli_w.dumps(doc).encode("utf-8"))
    log.info("Written: %s", OUTPUT_TOML)


# ---------------------------------------------------------------------------
# Markdown report  — full per-site audit cards
# ---------------------------------------------------------------------------
VERDICT_LABELS = {
    "ALLOWED":         "Allowed — Direct Scraping Permitted",
    "ALLOWED_VIA_API": "Allowed via Official API Only",
    "MANUAL_REVIEW":   "Manual Review Required Before Any Scraping",
    "SERP_ONLY":       "SERP / Reference Only (no direct scraping)",
    "BLOCKED":         "Blocked — Do Not Scrape",
    "UNREACHABLE":     "Unreachable (retry later)",
}

_BOOL = {True: "YES", False: "NO", None: "N/A"}


def _yn(val: bool) -> str:
    return "**YES**" if val else "NO"


def _status_badge(status: str) -> str:
    return {
        "found":       "FOUND",
        "not_found":   "NOT FOUND (404)",
        "unreachable": "UNREACHABLE",
        "skipped":     "SKIPPED (API/dry-run)",
        "ok":          "OK",
        "error":       "ERROR / BLOCKED",
        "unknown":     "UNKNOWN",
    }.get(status, status)


def write_report(results: list[CheckResult]) -> None:
    ts = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    counts = Counter(r.verdict for r in results)

    lines: list[str] = [
        "# fin-aware — Site Permission Report",
        "",
        f"_Generated: {ts}_ | _Tool: v{TOOL_VERSION}_",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Verdict | Count |",
        "|---------|------:|",
    ]
    for v in VERDICT_ORDER:
        lines.append(f"| `{v}` | {counts.get(v, 0)} |")
    lines += [
        f"| **Total** | **{len(results)}** |",
        "",
        "> **Key:**",
        "> - `MANUAL_REVIEW` — contact site owner before any scraping",
        "> - `SERP_ONLY` — reference via SerpAPI only; never direct-scrape",
        "> - `UNREACHABLE` — retry later; do **not** assume allowed",
        "> - `ALLOWED` with access issues — legal basis is clear; scraper needs headers/auth work",
        "",
        "---",
        "",
    ]

    # Group by verdict
    by_verdict: dict[str, list[CheckResult]] = {v: [] for v in VERDICT_ORDER}
    for r in results:
        key = r.verdict if r.verdict in by_verdict else "MANUAL_REVIEW"
        by_verdict[key].append(r)

    for verdict in VERDICT_ORDER:
        group = by_verdict[verdict]
        if not group:
            continue

        lines += [
            f"## {VERDICT_LABELS.get(verdict, verdict)}",
            "",
        ]

        for r in sorted(group, key=lambda x: (x.tier, x.category, x.id)):
            # ── Site header ──
            lines += [
                f"### `{r.id}` — {r.name}",
                "",
                f"> **Verdict: `{r.verdict}`** | Confidence: `{r.confidence}` | "
                f"Tier {r.tier} | Category {r.category}",
                "",
            ]

            # ── robots.txt audit ──
            lines += [
                "#### robots.txt",
                "",
                "| Check | Result | Detail |",
                "|-------|--------|--------|",
                f"| Present? | `{_status_badge(r.robots_status)}` | "
                + (
                    "Fetched and parsed" if r.robots_status == "found" else
                    "No robots.txt file — RFC 9309 conventional allow applies" if r.robots_status == "not_found" else
                    "All retries failed — permission unknown" if r.robots_status == "unreachable" else
                    r.robots_status
                ) + " |",
            ]
            if r.robots_status == "found":
                lines += [
                    f"| Permits our purpose? | {'**YES**' if r.robots_allows else '**NO** — denies scraping'} | "
                    f"Checked against `*` wildcard and `FinAwareBot` agent |",
                ]
            elif r.robots_status == "not_found":
                lines += [
                    f"| Permits our purpose? | Conventional YES (not explicit) | "
                    f"Absent robots.txt = conventional allow under RFC 9309, NOT written permission |",
                ]
            else:
                lines += [
                    f"| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |",
                ]
            if r.crawl_delay_seconds:
                lines.append(f"| Crawl-delay | {r.crawl_delay_seconds}s | Must respect between requests |")
            lines.append("")

            # ── T&C audit ──
            tos_deny_str = (
                "**YES** — block signals found" if r.tos_denies else
                "NO — no block signals found" if r.tos_status == "found" else
                "UNKNOWN — T&C not accessible"
            )
            lines += [
                "#### Terms & Conditions",
                "",
                "| Check | Result | Detail |",
                "|-------|--------|--------|",
                f"| T&C page found? | `{_status_badge(r.tos_status)}` | "
                + (f"`{r.tos_url}`" if r.tos_url else "Checked 6 common paths — none accessible") + " |",
                f"| Denies scraping/reproduction? | {tos_deny_str} | "
                f"Net keyword score: `{r.permission_score:+d}` "
                f"({len(r.allow_signals)} allow, {len(r.block_signals)} block) |",
                "",
            ]

            # ── License ──
            lines += [
                "#### License / Open Access",
                "",
                f"Detected: **{r.license_detected or 'None'}**",
                "",
            ]

            # ── Allow signal contexts ──
            if r.allow_signals:
                lines += [
                    "#### Allow Signals — Context for Human Review",
                    "",
                    f"_{len(r.allow_signals)} allow keyword(s) found in T&C text:_",
                    "",
                ]
                for sig in r.allow_signals:
                    ctx = r.allow_signal_contexts.get(sig, "")
                    lines.append(f"**`{sig}`**")
                    if ctx:
                        lines.append(f"> {ctx}")
                    lines.append("")
            else:
                if r.tos_status == "found":
                    lines += ["#### Allow Signals", "", "_No allow keywords found in T&C._", ""]

            # ── Block signal contexts ──
            if r.block_signals:
                lines += [
                    "#### Block Signals — Context for Human Review",
                    "",
                    f"_{len(r.block_signals)} block keyword(s) found in T&C text:_",
                    "",
                ]
                for sig in r.block_signals:
                    ctx = r.block_signal_contexts.get(sig, "")
                    lines.append(f"**`{sig}`**")
                    if ctx:
                        lines.append(f"> {ctx}")
                    lines.append("")
            else:
                if r.tos_status == "found":
                    lines += ["#### Block Signals", "", "_No block keywords found in T&C._", ""]

            # ── Verdict reason ──
            lines += [
                "#### Verdict Reason",
                "",
                f"> {r.verdict_reason}",
                "",
            ]

            # ── HTTP fetch log ──
            has_issues = any(f.error_type or (f.status_code and f.status_code >= 400) for f in r.fetch_log)
            if r.fetch_log:
                lines += [
                    "#### HTTP Fetch Log",
                    "",
                    "| Purpose | Status | Error | Latency | URL |",
                    "|---------|--------|-------|---------|-----|",
                ]
                for f in r.fetch_log:
                    code = str(f.status_code) if f.status_code else "-"
                    err  = f"`{f.error_type}`" if f.error_type else "-"
                    short_url = (f.url[:65] + "...") if len(f.url) > 65 else f.url
                    lines.append(
                        f"| {f.purpose} | {code} | {err} | {f.latency_ms}ms | `{short_url}` |"
                    )
                lines.append("")

            # ── Source notes ──
            if r.source_notes:
                lines += [f"_Source note: {r.source_notes}_", ""]

            lines += ["---", ""]

    OUTPUT_REPORT.write_text("\n".join(lines), encoding="utf-8")
    log.info("Written: %s", OUTPUT_REPORT)


# ---------------------------------------------------------------------------
# Site loader
# ---------------------------------------------------------------------------
def load_sites() -> list[SiteRecord]:
    with SITES_FILE.open("rb") as fh:
        data = tomllib.load(fh)
    return [SiteRecord(**s) for s in data.get("site", [])]


def filter_sites(
    sites:    list[SiteRecord],
    site_id:  str | None,
    tier:     int | None,
    category: str | None,
) -> list[SiteRecord]:
    if site_id:
        sites = [s for s in sites if s.id == site_id]
    if tier:
        sites = [s for s in sites if s.tier == tier]
    if category:
        sites = [s for s in sites if s.category.upper() == category.upper()]
    return sites


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Check scraping permissions for fin-aware KB sites. "
                    "Safe defaults: unknown = MANUAL_REVIEW."
    )
    p.add_argument("--site",     help="Check a single site by ID")
    p.add_argument("--tier",     type=int, choices=[1, 2, 3])
    p.add_argument("--category", help="Filter by category A-I")
    p.add_argument("--dry-run",  action="store_true")
    p.add_argument("--workers",  type=int, default=DEFAULT_WORKERS,
                   help=f"Parallel worker threads (default: {DEFAULT_WORKERS})")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    sites = load_sites()
    log.info("Loaded %d sites from %s", len(sites), SITES_FILE)

    sites = filter_sites(sites, args.site, args.tier, args.category)
    total = len(sites)

    if not sites:
        log.error("No sites matched the given filters.")
        sys.exit(1)

    # Cap the pool size: no point spinning up more threads than sites
    actual_workers = min(args.workers, total)
    log.info(
        "Checking %d site(s) | pool size: %d worker(s) "
        "(requested %d, capped to site count)",
        total, actual_workers, args.workers,
    )

    results: list[CheckResult] = []
    completed = 0
    progress_lock = threading.Lock()

    # Each site gets a submission index (1-based) so we can show [site 3/7] in logs
    # independently of completion order reported by as_completed().
    def _worker(site: SiteRecord, submission_idx: int) -> CheckResult:
        wid = _assign_worker_id()          # stable W-NN for this physical thread
        log.info(
            "[W-%02d | job %d/%d] START  %s  (%s)",
            wid, submission_idx, total, site.name, site.id,
        )
        result = check_site(site, dry_run=args.dry_run)
        log.info(
            "[W-%02d | job %d/%d] DONE   %-30s -> %s (%s)",
            wid, submission_idx, total, site.id, result.verdict, result.confidence,
        )
        return result

    with ThreadPoolExecutor(max_workers=actual_workers) as executor:
        futures = {
            executor.submit(_worker, site, idx): site
            for idx, site in enumerate(sites, 1)
        }
        for future in as_completed(futures):
            site = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                log.error("Worker crashed for %s: %s", site.id, exc, exc_info=True)
                result = CheckResult(
                    id=site.id, name=site.name, base_url=site.base_url,
                    scrape_url=site.scrape_url, tier=site.tier,
                    extraction=site.extraction, category=site.category,
                    verdict="UNREACHABLE", confidence="high",
                    verdict_reason=f"Worker exception: {exc}",
                    checked_at=datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
                )
            with progress_lock:
                results.append(result)
                completed += 1
                log.info(
                    "[progress %d/%d] %-35s -> %s (%s)",
                    completed, total, result.id, result.verdict, result.confidence,
                )

    # Sort output by tier → category → id for stable ordering
    results.sort(key=lambda r: (r.tier, r.category, r.id))

    write_toml(results)
    write_report(results)

    counts = Counter(r.verdict for r in results)
    print("\n+--------------------------------------+")
    print("|     fin-aware Permission Summary     |")
    print("+----------------------+--------------+")
    for v in VERDICT_ORDER:
        c = counts.get(v, 0)
        if c:
            print(f"| {v:<20} | {c:>4} sites   |")
    print("+----------------------+--------------+")
    print(f"| {'TOTAL':<20} | {total:>4} sites   |")
    print("+----------------------+--------------+")
    print(f"\nDetailed TOML  : {OUTPUT_TOML}")
    print(f"Markdown report: {OUTPUT_REPORT}")
    print(f"Audit cache    : {CACHE_DIR}/")
    print(f"Log file       : {LOGS_DIR}/permission_check.log\n")


if __name__ == "__main__":
    main()
