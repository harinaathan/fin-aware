# fin-aware — Site Permission Report

_Generated: 2026-04-16T01:40:53+00:00_ | _Tool: v1.2.0_

---

## Summary

| Verdict | Count |
|---------|------:|
| `ALLOWED` | 41 |
| `ALLOWED_VIA_API` | 12 |
| `MANUAL_REVIEW` | 30 |
| `SERP_ONLY` | 12 |
| `BLOCKED` | 0 |
| `UNREACHABLE` | 1 |
| **Total** | **96** |

> **Key:**
> - `MANUAL_REVIEW` — contact site owner before any scraping
> - `SERP_ONLY` — reference via SerpAPI only; never direct-scrape
> - `UNREACHABLE` — retry later; do **not** assume allowed
> - `ALLOWED` with access issues — legal basis is clear; scraper needs headers/auth work

---

## Allowed — Direct Scraping Permitted

### `gst_portal` — GST Portal — Public FAQs & Guides

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 375ms | `https://www.gst.gov.in` |
| robots | 403 | `http_4xx` | 47ms | `https://www.gst.gov.in/robots.txt` |
| tos_page | 403 | `http_4xx` | 47ms | `https://www.gst.gov.in/tos` |
| tos_page | 403 | `http_4xx` | 47ms | `https://www.gst.gov.in/terms-of-use` |
| tos_page | 403 | `http_4xx` | 46ms | `https://www.gst.gov.in/terms-of-service` |
| tos_page | 403 | `http_4xx` | 47ms | `https://www.gst.gov.in/terms` |
| tos_page | 403 | `http_4xx` | 46ms | `https://www.gst.gov.in/privacy-policy` |
| tos_page | 403 | `http_4xx` | 47ms | `https://www.gst.gov.in/privacy` |

_Source note: Public domain. GST registration, returns, and taxpayer education FAQs._

---

### `nism` — NISM — National Institute of Securities Markets

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.nism.ac.in/privacy-policy/` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 8500ms | `https://www.nism.ac.in` |
| robots | 200 | - | 202ms | `https://www.nism.ac.in/robots.txt` |
| tos_page | 200 | - | 6155ms | `https://www.nism.ac.in/privacy-policy/` |
| tos_page | 200 | - | 3968ms | `https://www.nism.ac.in/privacy-policy/` |

_Source note: Public domain. Free NISM courseware and certifications content._

---

### `sebi_investor_ed` — SEBI Investor Education Portal

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 827ms | `https://investor.sebi.gov.in` |
| robots | 404 | `http_4xx` | 61ms | `https://investor.sebi.gov.in/robots.txt` |
| tos_page | 404 | `http_4xx` | 30ms | `https://investor.sebi.gov.in/tos` |
| tos_page | 404 | `http_4xx` | 47ms | `https://investor.sebi.gov.in/terms-of-use` |
| tos_page | 404 | `http_4xx` | 47ms | `https://investor.sebi.gov.in/terms-of-service` |
| tos_page | 404 | `http_4xx` | 31ms | `https://investor.sebi.gov.in/terms` |
| tos_page | 404 | `http_4xx` | 30ms | `https://investor.sebi.gov.in/privacy-policy` |
| tos_page | 404 | `http_4xx` | 31ms | `https://investor.sebi.gov.in/privacy` |

_Source note: Public domain. Excellent foundational material explicitly for public education._

---

### `freefincal` — Freefincal — M. Pattabiraman

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |
| Crawl-delay | 20s | Must respect between requests |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://freefincal.com/terms-of-service/` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+1` (1 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-profit`**
> ...pically includes online courses, Excel data sheets, or PDF documents. The revenue is used to cover the costs of hosting and managing the website in a non-profit manner. The buyer will use a payment platform, such as Instamojo, to make a purchase of these items. Cancellation , Refund, or Exchange Policy: Since...

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 765ms | `https://freefincal.com` |
| robots | 200 | - | 155ms | `https://freefincal.com/robots.txt` |
| tos_page | 200 | - | 186ms | `https://freefincal.com/terms-of-service/` |
| tos_page | 200 | - | 172ms | `https://freefincal.com/terms-of-service/` |

_Source note: Freely accessible. Evidence-based personal finance blog. Heavy on Indian context._

---

### `nse_pathshala` — NSE Pathshala — Investor Education

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (timeout) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `timeout` | 12219ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12219ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12233ms | `https://www.nseindia.com` |
| robots | 200 | - | 344ms | `https://www.nseindia.com/robots.txt` |
| tos_page | - | `timeout` | 12000ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12327ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12327ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12203ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12250ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12234ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12250ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12218ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12281ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12171ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12219ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12343ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12187ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12219ms | `https://www.nseindia.com/privacy` |

_Source note: Public domain (NSE). Structured modules on markets, derivatives, MFs._

---

### `oecd_finance` — OECD — Financial Education

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 422ms | `https://www.oecd.org` |
| robots | 200 | - | 405ms | `https://www.oecd.org/robots.txt` |
| tos_page | 403 | `http_4xx` | 15ms | `https://www.oecd.org/tos` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.oecd.org/terms-of-use` |
| tos_page | 403 | `http_4xx` | 327ms | `https://www.oecd.org/terms-of-service` |
| tos_page | 403 | `http_4xx` | 327ms | `https://www.oecd.org/terms` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.oecd.org/privacy-policy` |
| tos_page | 403 | `http_4xx` | 219ms | `https://www.oecd.org/privacy` |

_Source note: OECD/INFE financial literacy publications. Many are free to access._

---

### `sec_edu` — SEC — Investor Education

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.sec.gov/about/privacy-information` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 719ms | `https://www.sec.gov` |
| robots | 200 | - | 312ms | `https://www.sec.gov/robots.txt` |
| tos_page | 200 | - | 1108ms | `https://www.sec.gov/about/privacy-information` |
| tos_page | 200 | - | 16ms | `https://www.sec.gov/about/privacy-information` |

_Source note: US Federal government. Public domain. SEC investor education guides._

---

### `backtrader_docs` — Backtrader Documentation

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **MIT**

#### Verdict Reason

> Explicit open license detected: MIT

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 530ms | `https://www.backtrader.com` |
| robots | 200 | - | 77ms | `https://www.backtrader.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 78ms | `https://www.backtrader.com/tos` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.backtrader.com/terms-of-use` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.backtrader.com/terms-of-service` |
| tos_page | 404 | `http_4xx` | 78ms | `https://www.backtrader.com/terms` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.backtrader.com/privacy-policy` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.backtrader.com/privacy` |

_Source note: Open source Python backtesting framework documentation._

---

### `prmia` — PRMIA — Professional Risk Managers' International Association

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://prmia.org/Public/About/Terms_of_Use.aspx ` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+1` (2 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`free to use`**
> ...oduce, use, disclose and distribute the information to others without limitation, except as otherwise set forth in the Privacy Policy. PRMIA shall be free to use any ideas, concepts, know-how or techniques contained in such information for any purpose whatsoever, and you agree to waive any rights you may have...

**`non-profit`**
> Terms of Use Skip to main content Sign in Join Cart Toggle search Keyword search Toggle navigation Keyword search Terms of Use PRMIA is a non-profit corporation which provides information and resources to risk management professionals worldwide. Throughout the explanation of this policy, PRMIA som...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...bsite. You must keep intact all copyright, trademark and other proprietary notices that are part of this content when sharing Content with others and you may not use Content for commercial purposes, except within your company, without the prior written consent of PRMIA and/or Providers. Requests for such conse...

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1719ms | `https://prmia.org` |
| robots | 200 | - | 296ms | `https://prmia.org/robots.txt` |
| tos_page | 200 | - | 577ms | `https://prmia.org/Public/About/Terms_of_Use.aspx ` |
| tos_page | 200 | - | 344ms | `https://prmia.org/Public/About/Terms_of_Use.aspx ` |

_Source note: Risk management professional body. Free educational resources._

---

### `quantecon` — QuantEcon

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 484ms | `https://quantecon.org` |
| robots | 404 | `http_4xx` | 250ms | `https://quantecon.org/robots.txt` |
| tos_page | 404 | `http_4xx` | 265ms | `https://quantecon.org/tos` |
| tos_page | 404 | `http_4xx` | 250ms | `https://quantecon.org/terms-of-use` |
| tos_page | 404 | `http_4xx` | 250ms | `https://quantecon.org/terms-of-service` |
| tos_page | 404 | `http_4xx` | 312ms | `https://quantecon.org/terms` |
| tos_page | 404 | `http_4xx` | 266ms | `https://quantecon.org/privacy-policy` |
| tos_page | 404 | `http_4xx` | 265ms | `https://quantecon.org/privacy` |

_Source note: Thomas Sargent & John Stachurski. CC BY-ND 4.0. Rigorous quant economics, free._

---

### `amfi_india` — AMFI India — Association of Mutual Funds in India

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.amfiindia.com/terms-of-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-2` (1 allow, 3 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...vocable right to access, use and display this Site on any computers or other electronic display device of which you are a user, for your personal and non-commercial use only (the "Permitted Uses"). You agree to use the Site only for lawful purposes, for the Permitted Uses, and not for the Prohibited Uses. No oth...

#### Block Signals — Context for Human Review

_3 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...ks Schedule of Investor Awareness Program AMC Branches Locate a MF Distributor SEBI Useful Links View More TERMS OF USE | PRIVACY NOTICE © 2025 AMFI. All Rights Reserved Quick Access Latest NAV Download NAV Disclosure of Risk Parameters New Fund Offer View All

**`prohibited from`**
> ...gh a link. Limited linking to the Site is permitted if done in full compliance with all applicable laws, these Terms of Use. Prohibited uses. You are prohibited from any use of the Site that would give rise to liability or otherwise violate any applicable laws or regulations or the Terms of Use. You may not public...

**`you may not`**
> ...re prohibited from any use of the Site that would give rise to liability or otherwise violate any applicable laws or regulations or the Terms of Use. You may not publicly perform, publicly display, transmit, publish, participate in the sale or transfer of, modify, or create derivative works based on anything a...

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 750ms | `https://www.amfiindia.com` |
| robots | 404 | `http_4xx` | 141ms | `https://www.amfiindia.com/robots.txt` |
| tos_page | 200 | - | 77ms | `https://www.amfiindia.com/terms-of-use` |
| tos_page | 200 | - | 62ms | `https://www.amfiindia.com/terms-of-use` |

_Source note: Public domain. NAV data, fund classifications, investor education._

---

### `bse_archive` — BSE Data Archive

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 266ms | `https://www.bseindia.com` |
| robots | 404 | `http_4xx` | 47ms | `https://www.bseindia.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.bseindia.com/tos` |
| tos_page | 404 | `http_4xx` | 94ms | `https://www.bseindia.com/terms-of-use` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.bseindia.com/terms-of-service` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.bseindia.com/terms` |
| tos_page | 404 | `http_4xx` | 280ms | `https://www.bseindia.com/privacy-policy` |
| tos_page | 404 | `http_4xx` | 47ms | `https://www.bseindia.com/privacy` |

_Source note: Public domain. Historical OHLCV archives._

---

### `bse_india` — BSE India — Bombay Stock Exchange

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 734ms | `https://www.bseindia.com` |
| robots | 404 | `http_4xx` | 77ms | `https://www.bseindia.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.bseindia.com/tos` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.bseindia.com/terms-of-use` |
| tos_page | 404 | `http_4xx` | 62ms | `https://www.bseindia.com/terms-of-service` |
| tos_page | 404 | `http_4xx` | 61ms | `https://www.bseindia.com/terms` |
| tos_page | 404 | `http_4xx` | 94ms | `https://www.bseindia.com/privacy-policy` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.bseindia.com/privacy` |

_Source note: Public domain. Market data and press releases._

---

### `epfo` — EPFO — Employees' Provident Fund Organisation

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 750ms | `https://www.epfindia.gov.in` |
| robots | 200 | - | 47ms | `https://www.epfindia.gov.in/robots.txt` |
| tos_page | 200 | - | 375ms | `https://www.epfindia.gov.in/Disclaimer.php` |
| tos_page | 200 | - | 437ms | `https://www.epfindia.gov.in/Copyright.php` |
| tos_page | 200 | - | 547ms | `https://www.epfindia.gov.in/tos` |
| tos_page | 200 | - | 437ms | `https://www.epfindia.gov.in/terms-of-use` |
| tos_page | 200 | - | 405ms | `https://www.epfindia.gov.in/terms-of-service` |
| tos_page | 200 | - | 343ms | `https://www.epfindia.gov.in/terms` |

_Source note: Public domain. EPF, EPS, gratuity educational content._

---

### `gst_council` — GST Council — India

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://gstcouncil.gov.in/terms-and-conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...ecretariat[at]gov.in Suggestions Page last updated on : 16/04/2026 Total Visitors: 6458635 Copyright © 2024 Ministry of Finance, Government of India. All rights reserved

#### Verdict Reason

> Government portal — public domain

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1734ms | `https://gstcouncil.gov.in` |
| robots | 200 | - | 31ms | `https://gstcouncil.gov.in/robots.txt` |
| tos_page | 200 | - | 1171ms | `https://gstcouncil.gov.in/terms-and-conditions` |
| tos_page | 200 | - | 1172ms | `https://gstcouncil.gov.in/terms-and-conditions` |

_Source note: Public domain. GST rate notifications, council meeting outcomes._

---

### `ibbi` — IBBI — Insolvency and Bankruptcy Board of India

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://ibbi.gov.in/uploads/legalframwork/2ef94517f459de71a10782eb4be01d1a.pdf` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 8953ms | `https://ibbi.gov.in` |
| robots | 404 | `http_4xx` | 62ms | `https://ibbi.gov.in/robots.txt` |
| tos_page | 200 | - | 671ms | `https://ibbi.gov.in/uploads/legalframwork/2ef94517f459de71a10782e...` |
| tos_page | 200 | - | 436ms | `https://ibbi.gov.in/uploads/legalframwork/2ef94517f459de71a10782e...` |

_Source note: Public domain. IBC, insolvency proceedings education._

---

### `incometax_efiling` — Income Tax e-Filing Portal

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_5xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 375ms | `https://www.incometax.gov.in` |
| robots | 503 | `http_5xx` | 172ms | `https://www.incometax.gov.in/robots.txt` |
| tos_page | 503 | `http_5xx` | 172ms | `https://www.incometax.gov.in/tos` |
| tos_page | 503 | `http_5xx` | 171ms | `https://www.incometax.gov.in/terms-of-use` |
| tos_page | 503 | `http_5xx` | 172ms | `https://www.incometax.gov.in/terms-of-service` |
| tos_page | 503 | `http_5xx` | 62ms | `https://www.incometax.gov.in/terms` |
| tos_page | 503 | `http_5xx` | 187ms | `https://www.incometax.gov.in/privacy-policy` |
| tos_page | 503 | `http_5xx` | 187ms | `https://www.incometax.gov.in/privacy` |

_Source note: Public domain. Tax filing guides, FAQs, forms._

---

### `incometax_india` — Income Tax India — Official Portal

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 327ms | `https://www.incometaxindia.gov.in` |
| robots | 403 | `http_4xx` | 281ms | `https://www.incometaxindia.gov.in/robots.txt` |
| tos_page | 403 | `http_4xx` | 234ms | `https://www.incometaxindia.gov.in/tos` |
| tos_page | 403 | `http_4xx` | 280ms | `https://www.incometaxindia.gov.in/terms-of-use` |
| tos_page | 403 | `http_4xx` | 375ms | `https://www.incometaxindia.gov.in/terms-of-service` |
| tos_page | 403 | `http_4xx` | 202ms | `https://www.incometaxindia.gov.in/terms` |
| tos_page | 403 | `http_4xx` | 202ms | `https://www.incometaxindia.gov.in/privacy-policy` |
| tos_page | 403 | `http_4xx` | 234ms | `https://www.incometaxindia.gov.in/privacy` |

_Source note: Public domain. Income tax acts, rules, press releases._

---

### `irdai` — IRDAI — Insurance Regulatory and Development Authority

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **NO** — denies scraping | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Standard+Individual+Term+Life+Insurance+Product%2C+“Saral+Jeeva.pdf/f3ee6335-157d-5978-6531-f27d5f729bf8?t=1631551394531` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (ssl, ssl_fallback) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `ssl` | 672ms | `https://www.irdai.gov.in` |
| homepage | - | `ssl` | 218ms | `https://www.irdai.gov.in` |
| homepage | - | `ssl` | 219ms | `https://www.irdai.gov.in` |
| homepage | 200 | `ssl_fallback` | 546ms | `https://www.irdai.gov.in` |
| robots | - | `ssl` | 297ms | `https://www.irdai.gov.in/robots.txt` |
| robots | - | `ssl` | 265ms | `https://www.irdai.gov.in/robots.txt` |
| robots | - | `ssl` | 234ms | `https://www.irdai.gov.in/robots.txt` |
| robots | 200 | `ssl_fallback` | 93ms | `https://www.irdai.gov.in/robots.txt` |
| tos_page | - | `ssl` | 328ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | - | `ssl` | 186ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | - | `ssl` | 172ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | 200 | `ssl_fallback` | 327ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | - | `ssl` | 280ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | - | `ssl` | 219ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | - | `ssl` | 469ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |
| tos_page | 200 | `ssl_fallback` | 296ms | `https://www.irdai.gov.in/documents/37343/365525/Guidelines+on+Sta...` |

_Source note: Public domain. Insurance product guidelines and consumer education._

---

### `itat` — ITAT — Income Tax Appellate Tribunal

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (ssl) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `ssl` | 297ms | `https://www.itat.gov.in` |
| homepage | - | `ssl` | 1140ms | `https://www.itat.gov.in` |
| homepage | - | `ssl` | 452ms | `https://www.itat.gov.in` |
| homepage | - | `ssl` | 156ms | `https://www.itat.gov.in` |
| robots | - | `ssl` | 327ms | `https://www.itat.gov.in/robots.txt` |
| robots | - | `ssl` | 375ms | `https://www.itat.gov.in/robots.txt` |
| robots | - | `ssl` | 281ms | `https://www.itat.gov.in/robots.txt` |
| robots | - | `ssl` | 250ms | `https://www.itat.gov.in/robots.txt` |
| tos_page | - | `ssl` | 265ms | `https://www.itat.gov.in/tos` |
| tos_page | - | `ssl` | 390ms | `https://www.itat.gov.in/tos` |
| tos_page | - | `ssl` | 453ms | `https://www.itat.gov.in/tos` |
| tos_page | - | `ssl` | 280ms | `https://www.itat.gov.in/tos` |
| tos_page | - | `ssl` | 297ms | `https://www.itat.gov.in/terms-of-use` |
| tos_page | - | `ssl` | 280ms | `https://www.itat.gov.in/terms-of-use` |
| tos_page | - | `ssl` | 406ms | `https://www.itat.gov.in/terms-of-use` |
| tos_page | - | `ssl` | 202ms | `https://www.itat.gov.in/terms-of-use` |
| tos_page | - | `ssl` | 297ms | `https://www.itat.gov.in/terms-of-service` |
| tos_page | - | `ssl` | 327ms | `https://www.itat.gov.in/terms-of-service` |
| tos_page | - | `ssl` | 375ms | `https://www.itat.gov.in/terms-of-service` |
| tos_page | - | `ssl` | 234ms | `https://www.itat.gov.in/terms-of-service` |
| tos_page | - | `ssl` | 250ms | `https://www.itat.gov.in/terms` |
| tos_page | - | `ssl` | 312ms | `https://www.itat.gov.in/terms` |
| tos_page | - | `ssl` | 297ms | `https://www.itat.gov.in/terms` |
| tos_page | - | `ssl` | 265ms | `https://www.itat.gov.in/terms` |
| tos_page | - | `ssl` | 422ms | `https://www.itat.gov.in/privacy-policy` |
| tos_page | - | `ssl` | 312ms | `https://www.itat.gov.in/privacy-policy` |
| tos_page | - | `ssl` | 359ms | `https://www.itat.gov.in/privacy-policy` |
| tos_page | - | `ssl` | 218ms | `https://www.itat.gov.in/privacy-policy` |
| tos_page | - | `ssl` | 312ms | `https://www.itat.gov.in/privacy` |
| tos_page | - | `ssl` | 280ms | `https://www.itat.gov.in/privacy` |
| tos_page | - | `ssl` | 437ms | `https://www.itat.gov.in/privacy` |
| tos_page | - | `ssl` | 202ms | `https://www.itat.gov.in/privacy` |

_Source note: Public domain. Case law and tribunal orders — advanced tax reference._

---

### `mca` — MCA — Ministry of Corporate Affairs

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 219ms | `https://www.mca.gov.in` |
| robots | 403 | `http_4xx` | 265ms | `https://www.mca.gov.in/robots.txt` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.mca.gov.in/tos` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.mca.gov.in/terms-of-use` |
| tos_page | 403 | `http_4xx` | 202ms | `https://www.mca.gov.in/terms-of-service` |
| tos_page | 403 | `http_4xx` | 203ms | `https://www.mca.gov.in/terms` |
| tos_page | 403 | `http_4xx` | 202ms | `https://www.mca.gov.in/privacy-policy` |
| tos_page | 403 | `http_4xx` | 202ms | `https://www.mca.gov.in/privacy` |

_Source note: Public domain. Company law, compliance, corporate governance._

---

### `mof_india` — Ministry of Finance — India

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (connection) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `connection` | 47ms | `https://finmin.nic.in` |
| homepage | - | `connection` | 0ms | `https://finmin.nic.in` |
| homepage | - | `connection` | 0ms | `https://finmin.nic.in` |
| robots | - | `connection` | 0ms | `https://finmin.nic.in/robots.txt` |
| robots | - | `connection` | 0ms | `https://finmin.nic.in/robots.txt` |
| robots | - | `connection` | 0ms | `https://finmin.nic.in/robots.txt` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/tos` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/tos` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/tos` |
| tos_page | - | `connection` | 15ms | `https://finmin.nic.in/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/terms` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy` |
| tos_page | - | `connection` | 0ms | `https://finmin.nic.in/privacy` |

_Source note: Public domain. Budget documents, economic surveys, policy circulars._

---

### `mospi` — MOSPI — Ministry of Statistics and Programme Implementation

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://mospi.gov.in/tos` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1234ms | `https://mospi.gov.in` |
| robots | 200 | - | 46ms | `https://mospi.gov.in/robots.txt` |
| tos_page | 200 | - | 47ms | `https://mospi.gov.in/tos` |
| tos_page | 200 | - | 718ms | `https://mospi.gov.in/tos` |

_Source note: Public domain. GDP, CPI, IIP macroeconomic datasets._

---

### `nabard` — NABARD — National Bank for Agriculture and Rural Development

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.nabard.org/auth/writereaddata/File/gender-policy-of-nabard.pdf` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 530ms | `https://www.nabard.org` |
| robots | 200 | - | 93ms | `https://www.nabard.org/robots.txt` |
| tos_page | 200 | - | 250ms | `https://www.nabard.org/auth/writereaddata/File/gender-policy-of-n...` |
| tos_page | 200 | - | 172ms | `https://www.nabard.org/auth/writereaddata/File/gender-policy-of-n...` |

_Source note: Public domain. Rural finance, agricultural credit education._

---

### `nps_trust` — NPS Trust

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.npstrust.org.in/results-providing-professional-indemnity-insurance-policy-trustees-national-pension-system-trust-0` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...RTI Tenders Contact Us iOS Android Social Connections Twitter Facebook Instagram LinkedIn Copyright © 2024 National Pension System Trust (NPS Trust). All rights reserved Last Updated : 13 April 2026 Loading... Visitors : Top Your browser does not support Javascript Your browser does not support Javascript Your brows...

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 2265ms | `https://www.npstrust.org.in` |
| robots | 403 | `http_4xx` | 78ms | `https://www.npstrust.org.in/robots.txt` |
| tos_page | 200 | - | 140ms | `https://www.npstrust.org.in/results-providing-professional-indemn...` |
| tos_page | 200 | - | 140ms | `https://www.npstrust.org.in/results-providing-professional-indemn...` |

_Source note: Public domain. NPS scheme details, calculators, subscriber education._

---

### `nse_bhavcopy` — NSE Bhavcopy — EOD Data Archives

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (timeout) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `timeout` | 12281ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12250ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12327ms | `https://www.nseindia.com` |
| robots | 200 | - | 234ms | `https://www.nseindia.com/robots.txt` |
| tos_page | - | `timeout` | 12000ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12233ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12281ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12297ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12281ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12312ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12234ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12172ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12233ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12250ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12218ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12218ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12203ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12311ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12234ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12219ms | `https://www.nseindia.com/privacy` |

_Source note: Public domain. Daily EOD price/volume data for backtesting._

---

### `nse_india` — NSE India — National Stock Exchange

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Known open-access institution. NOTE: access issues during check (timeout) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `timeout` | 12702ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12219ms | `https://www.nseindia.com` |
| homepage | - | `timeout` | 12312ms | `https://www.nseindia.com` |
| robots | 200 | - | 327ms | `https://www.nseindia.com/robots.txt` |
| tos_page | - | `timeout` | 12047ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12280ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12234ms | `https://www.nseindia.com/tos` |
| tos_page | - | `timeout` | 12359ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12219ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12233ms | `https://www.nseindia.com/terms-of-use` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12172ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12266ms | `https://www.nseindia.com/terms-of-service` |
| tos_page | - | `timeout` | 12187ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12172ms | `https://www.nseindia.com/terms` |
| tos_page | - | `timeout` | 12218ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12266ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12202ms | `https://www.nseindia.com/privacy-policy` |
| tos_page | - | `timeout` | 12203ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12233ms | `https://www.nseindia.com/privacy` |
| tos_page | - | `timeout` | 12281ms | `https://www.nseindia.com/privacy` |

_Source note: Public domain. Market data, press releases, derivatives analytics._

---

### `pfrda` — PFRDA — Pension Fund Regulatory and Development Authority

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **NO** — denies scraping | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.pfrda.org.in/web/pfrda/terms-and-conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...PFRDA. The content posted on this website is owned and maintained by the respective divisions and departments under PFRDA. © 2025 - Copyright PFRDA. All rights reserved. Visitor Count: Visitor Count : 2459551 Visitor Count: Sitemap | Terms & Conditions | Privacy Policy Hidden We use cookies to enhance your browsing e...

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1047ms | `https://www.pfrda.org.in` |
| robots | 200 | - | 47ms | `https://www.pfrda.org.in/robots.txt` |
| tos_page | 200 | - | 187ms | `https://www.pfrda.org.in/web/pfrda/terms-and-conditions` |
| tos_page | 200 | - | 140ms | `https://www.pfrda.org.in/web/pfrda/terms-and-conditions` |

_Source note: Public domain. NPS, APY, retirement planning regulatory content._

---

### `rbi_main` — RBI — Reserve Bank of India

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.rbi.org.in/scripts/Annualpolicy.aspx` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **Public Domain**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...Information Act Tenders Follow RBI RSS Twitter YouTube Instagram Facebook LinkedIn Download Mobile App Play Store App Store © Reserve Bank of India. All Rights Reserved. Sitemap | Disclaimer Website owned and managed by Reserve Bank of India. Contact us on helpdoc[at]rbi[dot]org[dot]in Website last updated date: Apr...

#### Verdict Reason

> Known open-access institution; open license: Public Domain. NOTE: access issues during check (http_4xx, other) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1187ms | `https://www.rbi.org.in` |
| robots | 418 | `http_4xx` | 77ms | `https://www.rbi.org.in/robots.txt` |
| tos_page | - | `other` | 0ms | `javascript:void(0);` |
| tos_page | - | `other` | 0ms | `javascript:void(0);` |
| tos_page | - | `other` | 0ms | `javascript:void(0);` |
| tos_page | 200 | - | 281ms | `https://www.rbi.org.in/scripts/Annualpolicy.aspx` |
| tos_page | 200 | - | 15ms | `https://www.rbi.org.in/scripts/Annualpolicy.aspx` |

_Source note: Public domain. Circulars, monetary policy reports, financial stability reports._

---

### `sebi_main` — SEBI — Main Portal (Notifications & Circulars)

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category A

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListingAll=yes&cid=7` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 812ms | `https://www.sebi.gov.in` |
| robots | 200 | - | 47ms | `https://www.sebi.gov.in/robots.txt` |
| tos_page | 200 | - | 297ms | `https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListingAll=y...` |
| tos_page | 200 | - | 344ms | `https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListingAll=y...` |

_Source note: Public domain (.gov.in). Circulars and notifications on regulations._

---

### `tijori_finance` — Tijori Finance

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 2 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://tijorifinance.com/terms-of-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+1` (2 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...use of this Website or its contents, including copying or storing it or them in whole or part, other than for your own personal, non-commercial use is prohibited without the prior written permission of us. You may not reproduce, publish, transmit, distribute, display, modify, crea...

**`free to use`**
> ...e in the Privacy Policy. Account/Subscription – We provide access to the Services in the following manner: Free to browse information on the website. Free to use features after logging in Subscription to a paid plan for availing Services (paid user) For the second and third manner of Services, as mentioned abo...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...Privacy Policy Terms of Use Cancellation Policy ABOUT Features What's New Pricing CONNECT WITH US © 2026 Tijori Financial Services Private Limited | All rights reserved (formerly known as “Tijori Advisory Services Private Limited”) CONNECT WITH US |

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1109ms | `https://tijorifinance.com` |
| robots | 200 | - | 219ms | `https://tijorifinance.com/robots.txt` |
| tos_page | 200 | - | 452ms | `https://tijorifinance.com/terms-of-use` |
| tos_page | 200 | - | 202ms | `https://tijorifinance.com/terms-of-use` |

_Source note: Sector analysis and company breakdown guides. Check T&C._

---

### `bis_research` — BIS — Bank for International Settlements Working Papers

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.bis.org/terms_conditions.htm` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+2` (2 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...conditions without obtaining written permission from the BIS: Users may download, display, print out, photocopy or redistribute any BIS Material for non-commercial purposes. Users may reproduce a limited extract of BIS Material (other than the statistics published in the BIS Data Portal ) in other publications o...

**`may reproduce`**
> ...ritten permission from the BIS: Users may download, display, print out, photocopy or redistribute any BIS Material for non-commercial purposes. Users may reproduce a limited extract of BIS Material (other than the statistics published in the BIS Data Portal ) in other publications or products free of charge, pro...

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 672ms | `https://www.bis.org` |
| robots | 200 | - | 155ms | `https://www.bis.org/robots.txt` |
| tos_page | 200 | - | 172ms | `https://www.bis.org/terms_conditions.htm` |
| tos_page | 200 | - | 156ms | `https://www.bis.org/terms_conditions.htm` |

_Source note: BIS working papers are freely downloadable. Check copyright notice._

---

### `ecb_research` — ECB — European Central Bank Research

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |
| Crawl-delay | 5s | Must respect between requests |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.ecb.europa.eu/services/using-our-site/language-policy/html/index.en.html` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1265ms | `https://www.ecb.europa.eu` |
| robots | 200 | - | 218ms | `https://www.ecb.europa.eu/robots.txt` |
| tos_page | 200 | - | 281ms | `https://www.ecb.europa.eu/services/using-our-site/language-policy...` |
| tos_page | 200 | - | 233ms | `https://www.ecb.europa.eu/services/using-our-site/language-policy...` |

_Source note: ECB working papers freely accessible. Check copyright._

---

### `imf` — IMF — International Monetary Fund

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.imf.org/en/publications/search#cf-type=POPPRS` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...pyright and Usage Privacy Notice Contact Us Careers Glossary Scam Alert IMF Brand عربي 中文 Français 日本語 Русский Español @ International Monetary Fund. All rights reserved.

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1546ms | `https://www.imf.org` |
| robots | 200 | - | 328ms | `https://www.imf.org/robots.txt` |
| tos_page | 200 | - | 594ms | `https://www.imf.org/external/terms.htm` |
| tos_page | 200 | - | 390ms | `https://www.imf.org/en/publications/search#cf-type=POPPRS` |
| tos_page | 200 | - | 140ms | `https://www.imf.org/en/publications/search#cf-type=POPPRS` |

_Source note: Open access working papers and research. IMF T&C allows educational use._

---

### `us_fed` — US Federal Reserve — Research & Data

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.federalreserve.gov/data/scoos.htm` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Government portal — public domain. NOTE: access issues during check (http_4xx) — scraper may need custom headers or retry logic

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 702ms | `https://www.federalreserve.gov` |
| robots | 404 | `http_4xx` | 327ms | `https://www.federalreserve.gov/robots.txt` |
| tos_page | 200 | - | 311ms | `https://www.federalreserve.gov/data/scoos.htm` |
| tos_page | 200 | - | 47ms | `https://www.federalreserve.gov/data/scoos.htm` |

_Source note: US Federal government. Public domain by definition. Working papers and FEDS notes._

---

### `arxiv_qfin` — arXiv — q-fin Section

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 2 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |
| Crawl-delay | 15s | Must respect between requests |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://info.arxiv.org/help/policies/privacy_policy.html` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Known open-access institution

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 530ms | `https://arxiv.org` |
| robots | 200 | - | 234ms | `https://arxiv.org/robots.txt` |
| tos_page | 200 | - | 750ms | `https://info.arxiv.org/help/policies/privacy_policy.html` |
| tos_page | 200 | - | 77ms | `https://info.arxiv.org/help/policies/privacy_policy.html` |

_Source note: Open access preprints. Cornell University. Public domain._

---

### `trading_qna` — TradingQnA — Zerodha Community

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 3 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://tradingqna.com/tos` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+1` (2 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`creative commons`**
> ...ses and effects of the materials, whether requested to do so by Zerodha or otherwise. 3. User Content License User contributions are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License . Without limiting any of those representations or warranties, Zerodha has the right (thoug...

**`attribution`**
> ...f the materials, whether requested to do so by Zerodha or otherwise. 3. User Content License User contributions are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License . Without limiting any of those representations or warranties, Zerodha has the right (though not the ob...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...you agree to become bound by the terms and conditions of this agreement. If you do not agree to all the terms and conditions of this agreement, then you may not access the Website or use any services. If these terms and conditions are considered an offer by Zerodha, acceptance is expressly limited to these te...

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 500ms | `https://tradingqna.com` |
| robots | 200 | - | 46ms | `https://tradingqna.com/robots.txt` |
| tos_page | 200 | - | 47ms | `https://tradingqna.com/tos` |
| tos_page | 200 | - | 46ms | `https://tradingqna.com/tos` |

_Source note: Zerodha community Q&A. Permission required per CONTEXT.md — contact for educational/non-commercial use._

---

### `livelaw_tax` — Livelaw — Tax & Finance Section

> **Verdict: `ALLOWED`** | Confidence: `high` | Tier 3 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.livelaw.in/law-firms/litigation/madras-high-court-quashes-covid-19-lockdown-case-as-time-barred-notes-state-policy-to-withdraw-such-cases-530357` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **MIT**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> Explicit open license detected: MIT

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 281ms | `https://www.livelaw.in` |
| robots | 200 | - | 46ms | `https://www.livelaw.in/robots.txt` |
| tos_page | 200 | - | 47ms | `https://www.livelaw.in/law-firms/litigation/madras-high-court-qua...` |
| tos_page | 200 | - | 15ms | `https://www.livelaw.in/law-firms/litigation/madras-high-court-qua...` |

_Source note: Legal reporting on ITAT, High Court, SC tax rulings. Check T&C._

---

### `economic_times` — Economic Times — Markets

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://economictimes.indiatimes.com/terms-conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+1` (2 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...the Company hereby grants you a personal, limited, non-exclusive, non-transferable, freely revocable license to use the Services for the personal and non-commercial use only. Except for the foregoing limited license, no right, title or interest shall be transferred to you. Content on the Site and/or the Services...

**`personal use`**
> ...no right, title or interest shall be transferred to you. Content on the Site and/or the Services is provided to you “AS IS” for your information and personal use only and may not be used, copied, reproduced, distributed, transmitted, broadcast, displayed, sold, licensed, or otherwise exploited for any other pu...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...ively own all right, title and interest in and to the Site, Services, and the Company Content, including all associated intellectual property rights. You may not remove, alter or obscure any copyright, trademark, service mark or other proprietary rights notices incorporated in or accompanying the Site, Service...

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 327ms | `https://economictimes.indiatimes.com` |
| robots | 200 | - | 0ms | `https://economictimes.indiatimes.com/robots.txt` |
| tos_page | 200 | - | 62ms | `https://economictimes.indiatimes.com/terms-conditions` |
| tos_page | 200 | - | 15ms | `https://economictimes.indiatimes.com/terms-conditions` |

_Source note: Times Group. Likely SERP_ONLY. Rich financial news for news synthesizer agent._

---

### `hindu_business_line` — The Hindu BusinessLine

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.thehindugroup.com/termsofuse.html` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+1` (3 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_3 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...permit the use of materials on this Site & Service subject to due credit is given to THG PUBLISHING PRIVATE LIMITED. The use shall also be subject to non-commercial use and limited to personal or academic dissemination. (Including on social media and use on all kinds of media). Copyright should be acknowledged. S...

**`attribution`**
> ...ld be acknowledged. Such use should not infringe on the Intellectual Property Rights of any person When using material on the Site or Service, proper attribution to authors and/or copyright holders must be given. User is granted a limited, revocable and non-exclusive right to create hyperlinks to the home page...

**`personal use`**
> ...tor (Collectively referred to as Users) automatically confirm your acknowledgment & acceptance of these T&C & R&R of this agreement. Usage Rights For personal use only: Your account and password are personal to you and may not be used by anyone else to access the Site or Service. You will not do anything which...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`prohibited from`**
> ...emarks, logos & service marks ("Marks") displayed on the Site & Service are the property of THG PUBLISHING PRIVATE LIMITED & other parties. Users are prohibited from using any Marks for any purpose including, but not limited to use as metatags on other pages or sites on the World Wide Web without the written permi...

**`you may not`**
> ...links do not portray THG PUBLISHING PRIVATE LIMITED or their podcast or products or services in a false, misleading, derogatory or offensive manner. You may not use THG PUBLISHING PRIVATE LIMITED's logos or proprietary graphics or trademarks as part of the link without express permission. No Warranties All co...

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 265ms | `https://www.thehindubusinessline.com` |
| robots | 200 | - | 30ms | `https://www.thehindubusinessline.com/robots.txt` |
| tos_page | 200 | - | 515ms | `https://www.thehindugroup.com/termsofuse.html` |
| tos_page | 200 | - | 31ms | `https://www.thehindugroup.com/termsofuse.html` |

_Source note: The Hindu Group. Check T&C — some free articles._

---

### `livemint` — Livemint

> **Verdict: `ALLOWED`** | Confidence: `medium` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.livemint.com/terms-of-use` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+1` (1 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...llowed to do (licence) We grant you a revocable, nonexclusive, nontransferable licence to access the Services and view content strictly for personal, non-commercial use. Prohibited Uses: Copy, reproduce, republish, distribute, publicly display/perform, adapt, translate, or create derivative works from our content...

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C mildly positive (score=1); license=none — monitor for policy changes

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 280ms | `https://www.livemint.com` |
| robots | 200 | - | 15ms | `https://www.livemint.com/robots.txt` |
| tos_page | 200 | - | 62ms | `https://www.livemint.com/terms-of-use` |
| tos_page | 200 | - | 30ms | `https://www.livemint.com/terms-of-use` |

_Source note: HT Media / WSJ partnership. Likely SERP_ONLY._

---

## Allowed via Official API Only

### `finrl` — FinRL Library — GitHub

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 1 | Category H

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (github_api). No direct scraping needed.

_Source note: MIT license. Reinforcement learning for trading._

---

### `pyfolio` — PyFolio — GitHub

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 1 | Category H

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (github_api). No direct scraping needed.

_Source note: Apache 2.0 license. Performance analysis tearsheets._

---

### `quantconnect_lean` — QuantConnect LEAN — GitHub (README & Wiki)

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 1 | Category H

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (github_api). No direct scraping needed.

_Source note: Apache 2.0 license. README, wiki, and release notes via GitHub API._

---

### `quantstats` — QuantStats — GitHub

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 1 | Category H

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (github_api). No direct scraping needed.

_Source note: Apache 2.0 license._

---

### `zipline_reloaded` — Zipline Reloaded — GitHub

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 1 | Category H

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (github_api). No direct scraping needed.

_Source note: Apache 2.0 license._

---

### `reddit_algotrading` — r/algotrading

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW)._

---

### `reddit_fire_india` — r/FIREIndia

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW). Financial Independence / Early Retirement India._

---

### `reddit_india_investments` — r/IndiaInvestments

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW). No direct scraping. Terms permit API access._

---

### `reddit_mf_india` — r/mutualfunds

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW)._

---

### `reddit_pf_india` — r/personalfinanceindia

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW)._

---

### `reddit_quant` — r/quant

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW)._

---

### `reddit_stocks` — r/stocks (India context)

> **Verdict: `ALLOWED_VIA_API`** | Confidence: `high` | Tier 3 | Category I

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `SKIPPED (API/dry-run)` | skipped |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `SKIPPED (API/dry-run)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Official API available (praw). No direct scraping needed.

_Source note: Official Reddit API (PRAW). Filter for India-relevant posts._

---

## Manual Review Required Before Any Scraping

### `advisorkhoj` — Advisorkhoj

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.advisorkhoj.com/terms-of-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...with their mutual fund distributors or financial advisor before investing. © 2024 Advisorkhoj - A Gamechanger Business Services (I) Pvt. Ltd. Brand - All Rights Reserved

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 219ms | `https://www.advisorkhoj.com` |
| robots | 200 | - | 15ms | `https://www.advisorkhoj.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 47ms | `https://www.advisorkhoj.com/tos` |
| tos_page | 200 | - | 31ms | `https://www.advisorkhoj.com/terms-of-use` |
| tos_page | 200 | - | 30ms | `https://www.advisorkhoj.com/terms-of-use` |

_Source note: MF analytics, portfolio overlap tools. Educational articles freely accessible._

---

### `elearnmarkets` — Elearnmarkets

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.elearnmarkets.com/terms-of-use` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 531ms | `https://www.elearnmarkets.com` |
| robots | 200 | - | 62ms | `https://www.elearnmarkets.com/robots.txt` |
| tos_page | 200 | - | 155ms | `https://www.elearnmarkets.com/terms-of-use` |
| tos_page | 200 | - | 109ms | `https://www.elearnmarkets.com/terms-of-use` |

_Source note: StockEdge parent. Large free library of trading and investing education articles._

---

### `etmoney_learn` — ET Money — Learn

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.etmoney.com/terms-and-condition` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 296ms | `https://www.etmoney.com` |
| robots | 200 | - | 47ms | `https://www.etmoney.com/robots.txt` |
| tos_page | 200 | - | 93ms | `https://www.etmoney.com/terms-and-condition` |
| tos_page | 200 | - | 172ms | `https://www.etmoney.com/terms-and-condition` |

_Source note: Times Group. Free educational section. Check T&C for scraping._

---

### `groww_learn` — Groww — Learn

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://groww.in/terms-and-conditions/` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 265ms | `https://groww.in` |
| robots | 200 | - | 77ms | `https://groww.in/robots.txt` |
| tos_page | 200 | - | 297ms | `https://groww.in/terms-and-conditions/` |
| tos_page | 200 | - | 187ms | `https://groww.in/terms-and-conditions/` |

_Source note: Large library of beginner-friendly articles. Freely accessible._

---

### `jagoinvestor` — Jagoinvestor — Manish Chauhan

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.jagoinvestor.com/terms` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (1 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...re is no guarantee or promise of returns or targets of how much wealth you can generate. 3. Use of Service You may use our Service for your personal, non-commercial use only. You may not use our Service for any illegal or unauthorized purpose. 4. Investment Risks Investing involves risks, including the risk of lo...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...9922535 [email protected] +919979922535 We are AMFI Registered Mutual Fund Distributors : ARN-97534 Disclaimer Privacy Policy Terms & Conditions 2025 All rights Reserved - Jagoinvestor Designed & Developed- Leo9Studio

**`you may not`**
> ...r financial portfolio. By accessing or using our Service, you agree to these Terms and Disclosures. If you do not agree with any part of these terms, you may not use our Service. 1. Eligibility You must be at least 18 years old to use our Service. By using our Service, you represent and warrant that you are at...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 547ms | `https://www.jagoinvestor.com` |
| robots | 200 | - | 46ms | `https://www.jagoinvestor.com/robots.txt` |
| tos_page | 200 | - | 125ms | `https://www.jagoinvestor.com/terms` |
| tos_page | 200 | - | 108ms | `https://www.jagoinvestor.com/terms` |

_Source note: Pioneer Indian personal finance blog. Extensively covers insurance, goals, tax._

---

### `moneyworks4me` — Moneyworks4me

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.moneyworks4me.com/stock-market/about/terms-of-use/?from=footermenu` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1390ms | `https://www.moneyworks4me.com` |
| robots | 200 | - | 140ms | `https://www.moneyworks4me.com/robots.txt` |
| tos_page | 200 | - | 811ms | `https://www.moneyworks4me.com/stock-market/about/terms-of-use/?fr...` |
| tos_page | 200 | - | 812ms | `https://www.moneyworks4me.com/stock-market/about/terms-of-use/?fr...` |

_Source note: Free personal finance and investment education articles._

---

### `personalfn` — PersonalFN

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.personalfn.com/terms-of-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+0` (1 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...recourse to us; and agree not to allow any third party directly or indirectly to use your subscription, user name or password. Limits on Personal and Non-Commercial Use The User expressly agrees to use the Service strictly for personal purpose. The User shall not recompile, disassemble, copy, modify, distribute,...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`expressly prohibited`**
> ...web site or any part thereof including but not limited to text content and graphics to any other server or location including caching of any kind is expressly prohibited. The Service is licensed to the User not sold to him. PersonalFN owns the Service, its applications and Trademarks. Links to third Party Sites This W...

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1468ms | `https://www.personalfn.com` |
| robots | 200 | - | 47ms | `https://www.personalfn.com/robots.txt` |
| tos_page | 200 | - | 47ms | `https://www.personalfn.com/terms-of-use` |
| tos_page | 200 | - | 47ms | `https://www.personalfn.com/terms-of-use` |

_Source note: Large library of personal finance articles for India. Check T&C._

---

### `screener_in` — Screener.in — Educational Content

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.screener.in/guides/terms/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (1 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...applicable copyright and trademark law. Service License a. Permission is granted to use the materials (information or software) on Site for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not: modify or copy the materials; u...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`prohibited from`**
> ...d regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site. The materials contained in this website are protected by applicable copyright and trademark law. Service License a. Per...

**`you may not`**
> ...ftware) on Site for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not: modify or copy the materials; use the materials for any commercial purpose, or for any public display (commercial or non-commercial); attempt to dec...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 281ms | `https://www.screener.in` |
| robots | 200 | - | 30ms | `https://www.screener.in/robots.txt` |
| tos_page | 200 | - | 77ms | `https://www.screener.in/guides/terms/` |
| tos_page | 200 | - | 16ms | `https://www.screener.in/guides/terms/` |

_Source note: Free fundamental data and guide articles. Check T&C — data scraping likely restricted, articles may be OK._

---

### `sensibull_blog` — Sensibull Blog — Options Education

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://s3.ap-south-1.amazonaws.com/sensibull-public-documents/T%26C.pdf` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 406ms | `https://sensibull.com` |
| robots | 200 | - | 155ms | `https://sensibull.com/robots.txt` |
| tos_page | 200 | - | 391ms | `https://s3.ap-south-1.amazonaws.com/sensibull-public-documents/T%...` |
| tos_page | 200 | - | 93ms | `https://s3.ap-south-1.amazonaws.com/sensibull-public-documents/T%...` |

_Source note: Zerodha-backed. Options education content. Check T&C._

---

### `stockedge_blog` — StockEdge Learn

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://stockedge.com/terms` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+0` (1 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...e, posting and conduct restrictions: You agree that you will not under any circumstances: access the Service for any reason other than your personal, non-commercial use solely as permitted by the normal functionality of the Service, collect or harvest any personal data of any user of the Site or the Service use t...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...sing or using the Service, you signify your agreement to these Terms of Use. If you do not agree to be bound by these Terms of Use in their entirety, you may not access or use the Service . (1) PRIVACY POLICY The Company respects the privacy of its Service users. Please refer to the Company’s Privacy Policy wh...

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 890ms | `https://stockedge.com` |
| robots | 200 | - | 47ms | `https://stockedge.com/robots.txt` |
| tos_page | 200 | - | 250ms | `https://stockedge.com/terms` |
| tos_page | 200 | - | 187ms | `https://stockedge.com/terms` |

_Source note: Free blog content. Check T&C for scraping rights._

---

### `zerodha_varsity` — Zerodha Varsity

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://zerodha.com/terms-and-conditions/` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 452ms | `https://zerodha.com` |
| robots | 200 | - | 47ms | `https://zerodha.com/robots.txt` |
| tos_page | 200 | - | 62ms | `https://zerodha.com/terms-and-conditions/` |
| tos_page | 200 | - | 47ms | `https://zerodha.com/terms-and-conditions/` |

_Source note: Openly licensed for educational use. Highest priority Tier 1 source._

---

### `cleartax` — ClearTax — Articles & Guides

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.clear.in/meta/terms` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 250ms | `https://cleartax.in` |
| robots | 200 | - | 30ms | `https://cleartax.in/robots.txt` |
| tos_page | 200 | - | 468ms | `https://www.clear.in/meta/terms` |
| tos_page | 200 | - | 156ms | `https://www.clear.in/meta/terms` |

_Source note: India's largest tax education resource. Freely accessible articles._

---

### `icai` — ICAI — Knowledge Portal

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `NOT FOUND (404)` | No robots.txt file — RFC 9309 conventional allow applies |
| Permits our purpose? | Conventional YES (not explicit) | Absent robots.txt = conventional allow under RFC 9309, NOT written permission |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.icai.org/post/16566` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> No robots.txt; T&C ambiguous (score=0) — contact site owner before scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 422ms | `https://www.icai.org` |
| robots | 404 | `http_4xx` | 46ms | `https://www.icai.org/robots.txt` |
| tos_page | 200 | - | 77ms | `https://www.icai.org/post/16566` |
| tos_page | 200 | - | 62ms | `https://www.icai.org/post/16566` |

_Source note: Institute of Chartered Accountants of India. Free publications._

---

### `icsi` — ICSI — Institute of Company Secretaries

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.icsi.edu/terms/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+0` (1 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`attribution`**
> ...user of a Communication Service that you know, or reasonably should know, cannot be legally distributed in such manner. Falsify or delete any author attributions, legal or other proper notices or proprietary designations or labels of the origin or source of software or other material contained in a file that...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...ICSI: The Institute of Company Secretaries of India Web Site for any purpose that is unlawful or prohibited by these terms, conditions, and notices. You may not use the ICSI: The Institute of Company Secretaries of India Web Site in any manner which could damage, disable, overburden, or impair the ICSI: The I...

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 952ms | `https://www.icsi.edu` |
| robots | 200 | - | 125ms | `https://www.icsi.edu/robots.txt` |
| tos_page | 200 | - | 405ms | `https://www.icsi.edu/terms/` |
| tos_page | 200 | - | 530ms | `https://www.icsi.edu/terms/` |

_Source note: Company secretaries institute. Free study materials and guidance notes._

---

### `caia` — CAIA Association — Free Education

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://caia.org/terms-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (1 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...in the Content, and the Content is protected by US and international copyright laws. You may view, download and print the Content for your personal, non-commercial use, provided you retain all copyright and other proprietary notices contained in the original Content on any copy. The Content may not be used in an...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`you may not`**
> ...nt or future access and/or use of the Website. User name and Password. As part of the registration process, you must select a user name and password. You may not (a) select or use a user name or email address of another person with the intention of impersonating such person or (b) use a member name or email ad...

**`expressly prohibited`**
> ...l purpose. Deep linking, framing, and the use or posting of the Content on any other website or in a network computer environment for any purpose are expressly prohibited. Trademarks, service marks, and logos, including but not limited to CAIA, CAIAA, Chartered Alternative Investment Analyst, and Chartered Alternative...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 797ms | `https://caia.org` |
| robots | 200 | - | 0ms | `https://caia.org/robots.txt` |
| tos_page | 200 | - | 266ms | `https://caia.org/terms-use` |
| tos_page | 200 | - | 31ms | `https://caia.org/terms-use` |

_Source note: Alternative investment education. Some free content._

---

### `cfa_institute` — CFA Institute — Free Research Foundation

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.cfainstitute.org/about/governance/policies/terms-conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...ercial use. You must retain all copyright and other proprietary notices contained in the original material on any copy you make of the site material. You may not sell or modify our site material or reproduce, display, publicly perform, distribute, or otherwise use the material in any way for any public or comm...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 437ms | `https://www.cfainstitute.org` |
| robots | 200 | - | 47ms | `https://www.cfainstitute.org/robots.txt` |
| tos_page | 200 | - | 30ms | `https://www.cfainstitute.org/about/governance/policies/terms-cond...` |
| tos_page | 200 | - | 16ms | `https://www.cfainstitute.org/about/governance/policies/terms-cond...` |

_Source note: CFA Institute publishes free research monographs. Open access publications._

---

### `khan_academy_finance` — Khan Academy — Finance & Economics

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.khanacademy.org/tos` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 655ms | `https://www.khanacademy.org` |
| robots | 200 | - | 281ms | `https://www.khanacademy.org/robots.txt` |
| tos_page | 200 | - | 265ms | `https://www.khanacademy.org/tos` |
| tos_page | 200 | - | 297ms | `https://www.khanacademy.org/tos` |

_Source note: Free education mandate (CC BY-NC-SA). Excellent foundational content._

---

### `morningstar` — Morningstar — Free Articles

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 202 | - | 391ms | `https://www.morningstar.com` |
| robots | 200 | - | 718ms | `https://www.morningstar.com/robots.txt` |
| tos_page | 202 | - | 15ms | `https://www.morningstar.com/tos` |
| tos_page | 202 | - | 0ms | `https://www.morningstar.com/terms-of-use` |
| tos_page | 202 | - | 15ms | `https://www.morningstar.com/terms-of-service` |
| tos_page | 202 | - | 0ms | `https://www.morningstar.com/terms` |
| tos_page | 202 | - | 0ms | `https://www.morningstar.com/privacy-policy` |
| tos_page | 202 | - | 15ms | `https://www.morningstar.com/privacy` |

_Source note: Free educational articles on MFs, ETFs, investing basics. Check T&C._

---

### `aqr_research` — AQR Capital — Research Papers

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.aqr.com/Terms-of-Use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`unauthorized access`**
> ...ith access to the Website or portions of it using your user name, password, or other security information. You agree to notify AQR immediately of any unauthorized access to or use of your user name or password or any other breach of security (https://www.aqr.com/Contact-Us). You also agree to ensure that you exit from...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 3483ms | `https://www.aqr.com` |
| robots | 200 | - | 3750ms | `https://www.aqr.com/robots.txt` |
| tos_page | 200 | - | 875ms | `https://www.aqr.com/Terms-of-Use` |
| tos_page | 200 | - | 594ms | `https://www.aqr.com/Terms-of-Use` |

_Source note: Free research papers on factor investing, momentum, risk parity._

---

### `garp` — GARP — Global Association of Risk Professionals

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.garp.org/terms-of-use` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...ercial use. You must retain all copyright and other proprietary notices contained in the original material on any copy you make of the site material. You may not sell or modify our site material or reproduce, display, publicly perform, distribute, or otherwise use the material in any way for any public or comm...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 344ms | `https://www.garp.org` |
| robots | 200 | - | 578ms | `https://www.garp.org/robots.txt` |
| tos_page | 200 | - | 812ms | `https://www.garp.org/terms-of-use` |
| tos_page | 200 | - | 31ms | `https://www.garp.org/terms-of-use` |

_Source note: Risk education body. Free articles and resources._

---

### `rupeevest` — Rupeevest — MF Overlap Analyzer

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 2 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.rupeevest.com/Terms-and-Conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...91-8777416306 Mail to careAtrupeevestDotcom AMFI Registered Mutual Fund Distributor: ARN-110558 Privacy Policy Terms and Conditions © Copyright 2026. All rights reserved. Mutual fund investments are subject to market risks. Please read the scheme information and other related documents carefully before investing. Past...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 327ms | `https://www.rupeevest.com` |
| robots | 200 | - | 16ms | `https://www.rupeevest.com/robots.txt` |
| tos_page | 200 | - | 15ms | `https://www.rupeevest.com/Terms-and-Conditions` |
| tos_page | 200 | - | 31ms | `https://www.rupeevest.com/Terms-and-Conditions` |

_Source note: Portfolio overlap and MF analytics. Educational guides._

---

### `world_bank` — World Bank — Finance Research

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 2 | Category F

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 625ms | `https://www.worldbank.org` |
| robots | 200 | - | 62ms | `https://www.worldbank.org/robots.txt` |
| tos_page | 404 | `http_4xx` | 1062ms | `https://www.worldbank.org/tos` |
| tos_page | 404 | `http_4xx` | 1047ms | `https://www.worldbank.org/terms-of-use` |
| tos_page | 404 | `http_4xx` | 1062ms | `https://www.worldbank.org/terms-of-service` |
| tos_page | 404 | `http_4xx` | 1047ms | `https://www.worldbank.org/terms` |
| tos_page | 404 | `http_4xx` | 1047ms | `https://www.worldbank.org/privacy-policy` |
| tos_page | 404 | `http_4xx` | 1062ms | `https://www.worldbank.org/privacy` |

_Source note: Open access research papers. CC BY 3.0 IGO license on most publications._

---

### `nber_finance` — NBER — Working Papers (Finance)

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 2 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.nber.org/programs-projects/programs-working-groups%23Groups/innovation-policy` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`all rights reserved`**
> ...@nber.org webaccessibility@nber.org Homepage Accessibility Policy Diversity Policy Privacy Policy Follow © 2026 National Bureau of Economic Research. All Rights Reserved.

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 672ms | `https://www.nber.org` |
| robots | 200 | - | 296ms | `https://www.nber.org/robots.txt` |
| tos_page | 200 | - | 452ms | `https://www.nber.org/programs-projects/programs-working-groups%23...` |
| tos_page | 200 | - | 422ms | `https://www.nber.org/programs-projects/programs-working-groups%23...` |

_Source note: National Bureau of Economic Research. Abstracts free; some papers behind paywall._

---

### `paytmmoney_blog` — Paytm Money Blog

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 468ms | `https://www.paytmmoney.com` |
| robots | 200 | - | 62ms | `https://www.paytmmoney.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 77ms | `https://www.paytmmoney.com/tos` |
| tos_page | 404 | `http_4xx` | 93ms | `https://www.paytmmoney.com/terms-of-use` |
| tos_page | 404 | `http_4xx` | 94ms | `https://www.paytmmoney.com/terms-of-service` |
| tos_page | 404 | `http_4xx` | 109ms | `https://www.paytmmoney.com/terms` |
| tos_page | 404 | `http_4xx` | 125ms | `https://www.paytmmoney.com/privacy-policy` |
| tos_page | 404 | `http_4xx` | 93ms | `https://www.paytmmoney.com/privacy` |

_Source note: Paytm Money educational blog. Check T&C._

---

### `caclubindia` — CA Club India

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.caclubindia.com/terms_of_use.asp` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (1 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...have made. CA clubindia.com hereby grants you a limited, non-transferable license to access and use the Site and Content solely for your personal, non-commercial purposes. Except for the license in this Section 6, caclubindia.com retains all right, title, and interest in and to the Site and Content. Subjec...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`unauthorized access`**
> ...r Account to submit questions at the Site or to answer questions through the Site. If you know or suspect that anyone other than you knows or has unauthorized access to your Account Information or any part of it, you must promptly notify us by sending us an e-mail at [INSERT EMAIL OR CONTACT DETAILS]. If we chan...

**`expressly prohibited`**
> ...law. Except as provided in this Agreement, permission to reprint or electronically reproduce any Content in whole or in part for any purpose is expressly prohibited, unless prior written consent is obtained from caclubindia.com. You may contact us if you wish to obtain such consent. The Content on this Site i...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 2406ms | `https://www.caclubindia.com` |
| robots | 200 | - | 250ms | `https://www.caclubindia.com/robots.txt` |
| tos_page | 200 | - | 719ms | `https://www.caclubindia.com/terms_of_use.asp` |
| tos_page | 200 | - | 718ms | `https://www.caclubindia.com/terms_of_use.asp` |

_Source note: Community articles on taxation, compliance, company law. Check T&C._

---

### `taxguru` — Tax Guru

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |
| Crawl-delay | 1s | Must respect between requests |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://taxguru.in/finance/disclaimer-for-www-taxguru-in.html` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+0` (1 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`freely available`**
> ...ous laws in excel and word format. Please refer here in the About Us section of the website for more details. The access to the website/mobile app is freely available, in addition you can subscribe to our Newsletter at no cost. TaxGuru also provides an opportunity to the legal experts in specific field of Income Ta...

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`you may not`**
> ...o be the legal equivalent of your signature on a written contract, and equally binding. If you do not wish to be bound by these terms and conditions, you may not access or use the site. Furthermore, TaxGuru services owned and operated by Taxguru Consultancy & Online Publication LLP, Mumbai, India is provided t...

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 343ms | `https://taxguru.in` |
| robots | 200 | - | 30ms | `https://taxguru.in/robots.txt` |
| tos_page | 200 | - | 62ms | `https://taxguru.in/finance/disclaimer-for-www-taxguru-in.html` |
| tos_page | 200 | - | 62ms | `https://taxguru.in/finance/disclaimer-for-www-taxguru-in.html` |

_Source note: Deep CA-authored tax articles, circulars analysis. Freely accessible._

---

### `the_tax_talk` — The Tax Talk

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://thetaxtalk.com/terms` |
| Denies scraping/reproduction? | NO — no block signals found | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals

_No block keywords found in T&C._

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 2187ms | `https://thetaxtalk.com` |
| robots | 200 | - | 968ms | `https://thetaxtalk.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 718ms | `https://thetaxtalk.com/tos` |
| tos_page | 404 | `http_4xx` | 687ms | `https://thetaxtalk.com/terms-of-use` |
| tos_page | 404 | `http_4xx` | 671ms | `https://thetaxtalk.com/terms-of-service` |
| tos_page | 200 | - | 1313ms | `https://thetaxtalk.com/terms` |
| tos_page | 200 | - | 1250ms | `https://thetaxtalk.com/terms` |

_Source note: Tax practitioner articles and updates. Check T&C._

---

### `cnbc_tv18` — CNBC TV18 — News Text

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.cnbctv18.com/termsofuse/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (0 allow, 1 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_1 block keyword(s) found in T&C text:_

**`unauthorized access`**
> ...serves the right, in its sole discretion, to deny you access to this Site or any portion thereof without notice for the following reasons (a) for any unauthorized access or use by you (b) if you assign or transfer (or attempt the same) any rights granted to you under this User Agreement; (c) immediately, if you violat...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 469ms | `https://www.cnbctv18.com` |
| robots | 200 | - | 15ms | `https://www.cnbctv18.com/robots.txt` |
| tos_page | 200 | - | 94ms | `https://www.cnbctv18.com/termsofuse/` |
| tos_page | 200 | - | 30ms | `https://www.cnbctv18.com/termsofuse/` |

_Source note: Network18 / CNBC. Check T&C._

---

### `financial_express` — Financial Express

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.financialexpress.com/terms-and-conditions/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `+0` (2 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_2 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...s herein, we hereby grant you a personal, limited, non-exclusive, non-transferable, freely revocable license to use the Services for the personal and non-commercial use only. Except for the foregoing limited license, no right, title or interest shall be transferred to you. Content on the Site and/or the Services...

**`personal use`**
> ...no right, title or interest shall be transferred to you. Content on the Site and/or the Services is provided to you “AS IS” for your information and personal use only and may not be used, copied, reproduced, distributed, transmitted, broadcast, displayed, sold, licensed, or otherwise exploited for any other pu...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`unauthorized access`**
> ...of the Sites, or other users; nor do you seek to pass yourself off as another user. (iv) You specifically agree that we shall not be responsible for unauthorized access to or alteration of your transmissions or data, any material or data sent or received or not sent or received through the Sites. (v) You shall comply...

**`you may not`**
> ...owners. We reserve all rights not expressly granted in and to the Sites and/or the Services and the content. These Terms do not authorize you to, and you may not, reproduce, distribute, publicly display, publicly perform, communicate to the public, make available, create derivative works of or otherwise use or...

#### Verdict Reason

> robots.txt allows; T&C ambiguous (score=0) — verify before large-scale scraping

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 422ms | `https://www.financialexpress.com` |
| robots | 200 | - | 31ms | `https://www.financialexpress.com/robots.txt` |
| tos_page | 200 | - | 77ms | `https://www.financialexpress.com/terms-and-conditions/` |
| tos_page | 200 | - | 77ms | `https://www.financialexpress.com/terms-and-conditions/` |

_Source note: IE Group. Check T&C._

---

### `quantconnect_forum` — QuantConnect Forum

> **Verdict: `MANUAL_REVIEW`** | Confidence: `medium` | Tier 3 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.quantconnect.com/terms/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-1` (1 allow, 2 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`personal use`**
> ...s, Company grants you a non-sublicensable, non-transferable, non-exclusive, revocable, limited license to use and access the Site solely for your own personal use. 2.2 Certain Restrictions. The rights granted to you in these Terms are subject to the following restrictions: (a) you shall not license, sell, rent,...

#### Block Signals — Context for Human Review

_2 block keyword(s) found in T&C text:_

**`prohibited from`**
> ...ny cannot and will not be liable for any loss or damage arising from your failure to comply with the above requirements. 1.3 Non-Solicitation You are prohibited from soliciting or recruit any other users or members of the Site, including Alpha Stream Authors, for anyreason, unless you have requested and received p...

**`you may not`**
> ...SENT AND WARRANT THAT YOU HAVE THE RIGHT, AUTHORITY, AND CAPACITY TO ENTER INTO THESE TERMS (ON BEHALF OF YOURSELF OR THE ENTITY THAT YOU REPRESENT). YOU MAY NOT ACCESS OR USE THE SITE OR ACCEPT THE TERMS IF YOU ARE NOT AT LEAST 18 YEARS OLD. IF YOU DO NOT AGREE WITH ALL OF THE PROVISIONS OF THESE TERMS, DO NO...

#### Verdict Reason

> robots.txt allows; T&C mildly restrictive (score=-1) — seek written confirmation for any reproduction

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1405ms | `https://www.quantconnect.com` |
| robots | 200 | - | 218ms | `https://www.quantconnect.com/robots.txt` |
| tos_page | 200 | - | 500ms | `https://www.quantconnect.com/terms/` |
| tos_page | 200 | - | 468ms | `https://www.quantconnect.com/terms/` |

_Source note: Open backtesting platform community. Check T&C._

---

## SERP / Reference Only (no direct scraping)

### `tax2win` — Tax2Win — Guides

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 1 | Category C

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 718ms | `https://tax2win.in` |
| robots | 200 | - | 344ms | `https://tax2win.in/robots.txt` |
| tos_page | 403 | `http_4xx` | 47ms | `https://tax2win.in/tos` |
| tos_page | 403 | `http_4xx` | 765ms | `https://tax2win.in/terms-of-use` |
| tos_page | 403 | `http_4xx` | 718ms | `https://tax2win.in/terms-of-service` |
| tos_page | 403 | `http_4xx` | 765ms | `https://tax2win.in/terms` |
| tos_page | 403 | `http_4xx` | 655ms | `https://tax2win.in/privacy-policy` |
| tos_page | 403 | `http_4xx` | 703ms | `https://tax2win.in/privacy` |

_Source note: Beginner tax education articles. Freely accessible._

---

### `bogleheads` — Bogleheads Wiki & Forum

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 890ms | `https://www.bogleheads.org` |
| robots | 200 | - | 641ms | `https://www.bogleheads.org/robots.txt` |
| tos_page | 403 | `http_4xx` | 671ms | `https://www.bogleheads.org/tos` |
| tos_page | 403 | `http_4xx` | 703ms | `https://www.bogleheads.org/terms-of-use` |
| tos_page | 403 | `http_4xx` | 765ms | `https://www.bogleheads.org/terms-of-service` |
| tos_page | 403 | `http_4xx` | 687ms | `https://www.bogleheads.org/terms` |
| tos_page | 403 | `http_4xx` | 702ms | `https://www.bogleheads.org/privacy-policy` |
| tos_page | 403 | `http_4xx` | 688ms | `https://www.bogleheads.org/privacy` |

_Source note: Passive investing philosophy wiki. Community-edited, open access._

---

### `investopedia` — Investopedia

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 343ms | `https://www.investopedia.com` |
| robots | 200 | - | 547ms | `https://www.investopedia.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 109ms | `https://www.investopedia.com/tos` |
| tos_page | 403 | `http_4xx` | 390ms | `https://www.investopedia.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 359ms | `https://www.investopedia.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.investopedia.com/terms` |
| tos_page | 403 | `http_4xx` | 406ms | `https://www.investopedia.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 437ms | `https://www.investopedia.com/privacy` |

_Source note: Gold standard financial education dictionary. Likely SERP_ONLY or MANUAL_REVIEW._

---

### `portfolio_visualizer` — Portfolio Visualizer — Guides

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 1 | Category E

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 1343ms | `https://www.portfoliovisualizer.com` |
| robots | 403 | `http_4xx` | 250ms | `https://www.portfoliovisualizer.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.portfoliovisualizer.com/tos` |
| tos_page | 403 | `http_4xx` | 234ms | `https://www.portfoliovisualizer.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.portfoliovisualizer.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.portfoliovisualizer.com/terms` |
| tos_page | 403 | `http_4xx` | 266ms | `https://www.portfoliovisualizer.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.portfoliovisualizer.com/privacy` |

_Source note: Quantitative portfolio analysis tools with educational documentation._

---

### `alpha_architect` — Alpha Architect Blog

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 1 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 811ms | `https://alphaarchitect.com` |
| robots | 403 | `http_4xx` | 688ms | `https://alphaarchitect.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 671ms | `https://alphaarchitect.com/tos` |
| tos_page | 403 | `http_4xx` | 828ms | `https://alphaarchitect.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 733ms | `https://alphaarchitect.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 843ms | `https://alphaarchitect.com/terms` |
| tos_page | 403 | `http_4xx` | 640ms | `https://alphaarchitect.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 655ms | `https://alphaarchitect.com/privacy` |

_Source note: Evidence-based factor investing research blog. Freely accessible._

---

### `ssrn_finance` — SSRN — Finance Section

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 2 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |
| Crawl-delay | 5s | Must respect between requests |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 250ms | `https://www.ssrn.com` |
| robots | 200 | - | 343ms | `https://www.ssrn.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 15ms | `https://www.ssrn.com/tos` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.ssrn.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 359ms | `https://www.ssrn.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 296ms | `https://www.ssrn.com/terms` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.ssrn.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.ssrn.com/privacy` |

_Source note: Social Science Research Network. Preprints freely downloadable. Elsevier owned — check T&C._

---

### `capitalmind` — Capitalmind

> **Verdict: `SERP_ONLY`** | Confidence: `medium` | Tier 3 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.capitalmind.in/terms-and-conditions` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-3` (0 allow, 3 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals

_No allow keywords found in T&C._

#### Block Signals — Context for Human Review

_3 block keyword(s) found in T&C text:_

**`strictly prohibited`**
> ...is protected by copyright and other intellectual property laws. Unauthorized use, reproduction, or distribution of any material from this website is strictly prohibited. No Warranties: Capitalmind makes no warranties or representations about the accuracy, completeness, or suitability of the information on its website...

**`unauthorized access`**
> ...mages. This exclusion applies to damages from the use of or reliance on any information provided, any transactions conducted through the website, and unauthorized access or alteration of your transmissions or data. Governing Law: These Terms and Conditions are governed by the laws of India. Any disputes arising out of...

**`all rights reserved`**
> ...Policy Terms & Conditions Disclosure Notice Board PMS FAQ Contact SMART ODR Portal Copyright © 2026 Capitalmind Financial Services Private Limited • All rights reserved Capitalmind Financial Services Private Limited [Capitalmind Wealth (PMS)] SEBI Regd. Portfolio Manager INP000005847 Capitalmind Select India One (Cat...

#### Verdict Reason

> robots.txt allows BUT T&C restricts reproduction (score=-3) — technical access != legal permission

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 733ms | `https://www.capitalmind.in` |
| robots | 200 | - | 280ms | `https://www.capitalmind.in/robots.txt` |
| tos_page | 200 | - | 750ms | `https://www.capitalmind.in/terms-and-conditions` |
| tos_page | 200 | - | 30ms | `https://www.capitalmind.in/terms-and-conditions` |

_Source note: Some free content. Check T&C for non-commercial educational scraping._

---

### `valuepickr` — ValuePickr — Forum

> **Verdict: `SERP_ONLY`** | Confidence: `medium` | Tier 3 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `FOUND` | Fetched and parsed |
| Permits our purpose? | **YES** | Checked against `*` wildcard and `FinAwareBot` agent |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `FOUND` | `https://www.valuepickr.com/policies/terms-and-conditions/` |
| Denies scraping/reproduction? | **YES** — block signals found | Net keyword score: `-2` (1 allow, 3 block) |

#### License / Open Access

Detected: **None**

#### Allow Signals — Context for Human Review

_1 allow keyword(s) found in T&C text:_

**`non-commercial`**
> ...oards, charts, software, our articles and writings, graphics, and any and all other features. You may make one copy of the Content for your personal, non-commercial use, provided that any material copied remains intact and includes the following notice: ” © Copyright 2010 ValuePickr.com. All rights reserved.” Any...

#### Block Signals — Context for Human Review

_3 block keyword(s) found in T&C text:_

**`unauthorized access`**
> ...ture or disrupts the functioning of our systems or Services; and Take any action that damages or disrupts the functioning of our systems or Services. Unauthorized access of our sites is a breach of these Terms and Conditions and a violation of the law. You agree not to access our sites by any means other than through...

**`all rights reserved`**
> ...personal, non-commercial use, provided that any material copied remains intact and includes the following notice: ” © Copyright 2010 ValuePickr.com. All rights reserved.” Any other copying, distribution, storing, or transmission of any kind, or any commercial use of our Content, is prohibited without ValuePickr.com’s...

**`you may not`**
> ...oring, or transmission of any kind, or any commercial use of our Content, is prohibited without ValuePickr.com’s prior written permission. That means you may not sell, auction, transfer or barter your subscription or any individual publication. You also may not republish, post, transmit or distribute the Conte...

#### Verdict Reason

> robots.txt allows BUT T&C restricts reproduction (score=-2) — technical access != legal permission

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 200 | - | 1202ms | `https://www.valuepickr.com` |
| robots | 200 | - | 47ms | `https://www.valuepickr.com/robots.txt` |
| tos_page | 404 | `http_4xx` | 281ms | `https://www.valuepickr.com/terms/` |
| tos_page | 200 | - | 421ms | `https://www.valuepickr.com/policies/terms-and-conditions/` |
| tos_page | 200 | - | 422ms | `https://www.valuepickr.com/policies/terms-and-conditions/` |

_Source note: Deep fundamental analysis community. Permission required per CONTEXT.md._

---

### `bq_prime` — BQ Prime (BloombergQuint)

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 796ms | `https://www.bqprime.com` |
| robots | 403 | `http_4xx` | 422ms | `https://www.bqprime.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.bqprime.com/tos` |
| tos_page | 403 | `http_4xx` | 452ms | `https://www.bqprime.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 422ms | `https://www.bqprime.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.bqprime.com/terms` |
| tos_page | 403 | `http_4xx` | 281ms | `https://www.bqprime.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 297ms | `https://www.bqprime.com/privacy` |

_Source note: Bloomberg partnership. Check T&C — likely SERP_ONLY._

---

### `business_standard` — Business Standard

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 250ms | `https://www.business-standard.com` |
| robots | 403 | `http_4xx` | 390ms | `https://www.business-standard.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.business-standard.com/tos` |
| tos_page | 403 | `http_4xx` | 219ms | `https://www.business-standard.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.business-standard.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.business-standard.com/terms` |
| tos_page | 403 | `http_4xx` | 250ms | `https://www.business-standard.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 312ms | `https://www.business-standard.com/privacy` |

_Source note: Likely SERP_ONLY. High-quality financial and regulatory news._

---

### `moneycontrol` — Moneycontrol

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 3 | Category D

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 265ms | `https://www.moneycontrol.com` |
| robots | 403 | `http_4xx` | 297ms | `https://www.moneycontrol.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 265ms | `https://www.moneycontrol.com/tos` |
| tos_page | 403 | `http_4xx` | 281ms | `https://www.moneycontrol.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 234ms | `https://www.moneycontrol.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 327ms | `https://www.moneycontrol.com/terms` |
| tos_page | 403 | `http_4xx` | 390ms | `https://www.moneycontrol.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 234ms | `https://www.moneycontrol.com/privacy` |

_Source note: Major Indian financial news portal. Likely SERP_ONLY due to T&C restrictions._

---

### `wilmott` — Wilmott.com — Quant Forums

> **Verdict: `SERP_ONLY`** | Confidence: `high` | Tier 3 | Category G

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Server actively blocks our user-agent (HTTP 403 on homepage and all T&C paths). robots.txt may say 'allow' but practical access is blocked — use SERP API only.

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | 403 | `http_4xx` | 437ms | `https://wilmott.com` |
| robots | 403 | `http_4xx` | 46ms | `https://wilmott.com/robots.txt` |
| tos_page | 403 | `http_4xx` | 47ms | `https://wilmott.com/tos` |
| tos_page | 403 | `http_4xx` | 46ms | `https://wilmott.com/terms-of-use` |
| tos_page | 403 | `http_4xx` | 47ms | `https://wilmott.com/terms-of-service` |
| tos_page | 403 | `http_4xx` | 47ms | `https://wilmott.com/terms` |
| tos_page | 403 | `http_4xx` | 47ms | `https://wilmott.com/privacy-policy` |
| tos_page | 403 | `http_4xx` | 77ms | `https://wilmott.com/privacy` |

_Source note: Quant professional community. Check T&C for scraping._

---

## Unreachable (retry later)

### `bse_institute` — BSE Institute — Free Resources

> **Verdict: `UNREACHABLE`** | Confidence: `high` | Tier 1 | Category B

#### robots.txt

| Check | Result | Detail |
|-------|--------|--------|
| Present? | `UNREACHABLE` | All retries failed — permission unknown |
| Permits our purpose? | UNKNOWN | Cannot determine — unreachable |

#### Terms & Conditions

| Check | Result | Detail |
|-------|--------|--------|
| T&C page found? | `NOT FOUND (404)` | Checked 6 common paths — none accessible |
| Denies scraping/reproduction? | UNKNOWN — T&C not accessible | Net keyword score: `+0` (0 allow, 0 block) |

#### License / Open Access

Detected: **None**

#### Verdict Reason

> Homepage unreachable after 3 attempt(s): connection, connection, connection

#### HTTP Fetch Log

| Purpose | Status | Error | Latency | URL |
|---------|--------|-------|---------|-----|
| homepage | - | `connection` | 47ms | `https://www.bse-institute.com` |
| homepage | - | `connection` | 15ms | `https://www.bse-institute.com` |
| homepage | - | `connection` | 0ms | `https://www.bse-institute.com` |
| robots | - | `connection` | 0ms | `https://www.bse-institute.com/robots.txt` |
| robots | - | `connection` | 0ms | `https://www.bse-institute.com/robots.txt` |
| robots | - | `connection` | 0ms | `https://www.bse-institute.com/robots.txt` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/tos` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/tos` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/tos` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-use` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms-of-service` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/terms` |
| tos_page | - | `connection` | 15ms | `https://www.bse-institute.com/terms` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy-policy` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy` |
| tos_page | - | `connection` | 0ms | `https://www.bse-institute.com/privacy` |

_Source note: BSE subsidiary. Free courses and articles on capital markets._

---
