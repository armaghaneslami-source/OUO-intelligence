# OUO Intelligence - Scanner
# Scans all org lists, extracts job posting details, saves results.json

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
from config import (
    EUROPE_ORGS,
    EUROPE_UNIVERSITIES,
    EUROPE_ORGS_EXPANDED,
    JAPAN_ORGS,
    JAPAN_UNIVERSITIES,
    JAPAN_ORGS_EXPANDED,
    JAPAN_ACADEMIC_BOARDS,
    POSTDOC_BOARDS,
    POSTDOC_BOARDS_EXPANDED,
    NEWS_SOURCES,
)
from keywords import (
    ACADEMIA_TITLES,
    ACADEMIA_FIELDS,
    INDUSTRY_STRONG,
)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}


# ── KEYWORD MATCHING ──────────────────────────────────────────────────────────
#
# Two modes:
#
# "academia" -- used for universities, postdoc boards, academic job boards.
#   Requires BOTH:
#     - at least one ACADEMIA_TITLES term (e.g. "postdoc", "research fellow")
#     - at least one ACADEMIA_FIELDS term (e.g. "organizational psychology", "workplace")
#   This prevents false positives from MBA programs or IT research jobs.
#
# "industry" -- used for think tanks, institutes, survey firms, consultancies.
#   Requires at least one INDUSTRY_STRONG phrase (e.g. "people analytics",
#   "workforce research", "labor policy").
#   These phrases are specific enough that a single match is sufficient.

def check_keywords_academia(text):
    """
    Returns matched keywords if the text looks like a relevant academic posting.
    Requires at least one title term AND at least one field term.
    """
    text_lower = text.lower()

    titles_found = [t for t in ACADEMIA_TITLES if t.lower() in text_lower]
    fields_found = [f for f in ACADEMIA_FIELDS if f.lower() in text_lower]

    if titles_found and fields_found:
        # Return a combined list for display on the dashboard
        return titles_found[:2] + fields_found[:3]
    return []


def check_keywords_industry(text):
    """
    Returns matched keywords if the text contains a strong industry phrase.
    One match is sufficient.
    """
    text_lower = text.lower()
    return [phrase for phrase in INDUSTRY_STRONG if phrase.lower() in text_lower]


# ── POSTING EXTRACTION ────────────────────────────────────────────────────────

DEADLINE_PATTERNS = [
    r'deadline[:\s]+([A-Za-z0-9 ,]+\d{4})',
    r'closing date[:\s]+([A-Za-z0-9 ,]+\d{4})',
    r'apply by[:\s]+([A-Za-z0-9 ,]+\d{4})',
    r'applications? (due|by|before)[:\s]+([A-Za-z0-9 ,]+\d{4})',
    r'(\d{1,2}\s+[A-Za-z]+\s+\d{4})',
    r'([A-Za-z]+\s+\d{1,2},?\s+\d{4})',
]

JOB_TITLE_TAGS = [
    'h1', 'h2', 'h3', 'h4',
]

JOB_LINK_PATTERNS = [
    r'(job|vacanc|position|role|researcher|postdoc|fellow|analyst|officer|scientist)',
]


def extract_deadline(text):
    """Try to find a deadline date in a block of text."""
    for pattern in DEADLINE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip() if match.lastindex == 1 else match.group(2).strip()
    return None


def looks_like_job_title(text):
    """Return True if a heading looks like a job posting title."""
    text_lower = text.lower()
    return any(re.search(p, text_lower) for p in JOB_LINK_PATTERNS)


def extract_postings(soup, base_url, keywords_found):
    """
    Try to extract individual job postings from a page.
    Returns a list of dicts with title, url, deadline.
    Falls back to a single generic entry if nothing structured is found.
    """
    postings = []

    # Strategy 1: find headings that look like job titles
    for tag in JOB_TITLE_TAGS:
        for heading in soup.find_all(tag):
            title = heading.get_text(strip=True)
            if not title or len(title) < 8 or len(title) > 200:
                continue
            if not looks_like_job_title(title):
                continue

            # Try to find a nearby link
            link = None
            parent = heading.parent
            a_tag = heading.find('a') or (parent.find('a') if parent else None)
            if a_tag and a_tag.get('href'):
                href = a_tag['href']
                if href.startswith('http'):
                    link = href
                elif href.startswith('/'):
                    from urllib.parse import urlparse
                    parsed = urlparse(base_url)
                    link = f"{parsed.scheme}://{parsed.netloc}{href}"

            # Try to find a nearby deadline
            sibling_text = ""
            for sib in heading.next_siblings:
                sib_str = sib.get_text(strip=True) if hasattr(sib, 'get_text') else str(sib)
                sibling_text += " " + sib_str
                if len(sibling_text) > 400:
                    break
            deadline = extract_deadline(sibling_text)

            postings.append({
                "title": title,
                "url": link or base_url,
                "deadline": deadline,
            })

        if postings:
            break  # found something with h2/h3, stop here

    # Strategy 2: look for <a> items that look like job titles
    if not postings:
        for a in soup.find_all('a', href=True):
            title = a.get_text(strip=True)
            if not title or len(title) < 10 or len(title) > 180:
                continue
            if not looks_like_job_title(title):
                continue
            href = a['href']
            if href.startswith('http'):
                link = href
            elif href.startswith('/'):
                from urllib.parse import urlparse
                parsed = urlparse(base_url)
                link = f"{parsed.scheme}://{parsed.netloc}{href}"
            else:
                continue

            postings.append({
                "title": title,
                "url": link,
                "deadline": None,
            })

        # Cap at 5 link-based results
        postings = postings[:5]

    # Deduplicate by title
    seen = set()
    deduped = []
    for p in postings:
        key = p['title'].lower()[:60]
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    return deduped


# ── PAGE SCANNER ──────────────────────────────────────────────────────────────

def scan_page(name, url, mode="academia"):
    """
    Scan one page and return a result dict.
    mode: "academia" or "industry" -- controls which keyword logic is used.
    """
    print(f"  Scanning {name}...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        if mode == "industry":
            keywords_found = check_keywords_industry(text)
        else:
            keywords_found = check_keywords_academia(text)

        result = {
            "name": name,
            "url": url,
            "keywords_found": keywords_found,
            "status": "RELEVANT" if keywords_found else "nothing relevant",
            "postings_found": [],
            "scanned_at": datetime.now().isoformat(),
        }

        if keywords_found:
            result["postings_found"] = extract_postings(soup, url, keywords_found)

        return result

    except Exception as e:
        return {
            "name": name,
            "url": url,
            "keywords_found": [],
            "status": f"error: {str(e)}",
            "postings_found": [],
            "scanned_at": datetime.now().isoformat(),
        }


# ── NEWS SCANNER ──────────────────────────────────────────────────────────────

def scan_news(query):
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')[:3]
        results = []
        for item in items:
            results.append({
                "title": item.title.text if item.title else "No title",
                "link": item.link.text if item.link else "",
                "published": item.pubDate.text if item.pubDate else "",
                "query": query,
            })
        return results
    except Exception:
        return []


# ── MAIN RUN ──────────────────────────────────────────────────────────────────

def run_scan():
    print("\n🦚 OUO Intelligence scan starting...\n")

    results = {
        "scan_date": datetime.now().isoformat(),
        "europe_jobs": [],
        "europe_universities": [],
        "japan_jobs": [],
        "japan_universities": [],
        "japan_academic_boards": [],
        "postdoc_boards": [],
        "news": [],
        "europe_orgs_expanded": [],
        "japan_orgs_expanded": [],
        "postdoc_boards_expanded": [],
    }

    # Each section: (display label, org dict, results key, keyword mode)
    sections = [
        ("EUROPE — Think Tanks & Institutes", EUROPE_ORGS,          "europe_jobs",           "industry"),
        ("EUROPE — Universities",             EUROPE_UNIVERSITIES,   "europe_universities",   "academia"),
        ("EUROPE — Expanded Orgs",            EUROPE_ORGS_EXPANDED,  "europe_orgs_expanded",  "industry"),
        ("JAPAN — Orgs & Think Tanks",        JAPAN_ORGS,            "japan_jobs",            "industry"),
        ("JAPAN — Universities",              JAPAN_UNIVERSITIES,    "japan_universities",    "academia"),
        ("JAPAN — Academic Boards",           JAPAN_ACADEMIC_BOARDS, "japan_academic_boards", "academia"),
        ("JAPAN — Expanded Orgs",             JAPAN_ORGS_EXPANDED,   "japan_orgs_expanded",   "industry"),
        ("POSTDOC BOARDS",                    POSTDOC_BOARDS,        "postdoc_boards",        "academia"),
        ("POSTDOC BOARDS EXPANDED",           POSTDOC_BOARDS_EXPANDED, "postdoc_boards_expanded", "academia"),
    ]

    for label, org_dict, key, mode in sections:
        print(f"\n--- {label} ---")
        for name, url in org_dict.items():
            result = scan_page(name, url, mode=mode)
            results[key].append(result)

    print("\n--- NEWS ---")
    for query in NEWS_SOURCES:
        news = scan_news(query)
        results["news"].extend(news)
        if news:
            print(f"  {query}: {len(news)} items")

    # Save results
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n🦚 SCAN COMPLETE\n")

    # Summary
    total_relevant = 0
    total_postings = 0
    all_keys = ["europe_jobs", "europe_universities", "europe_orgs_expanded",
                "japan_jobs", "japan_universities", "japan_academic_boards",
                "japan_orgs_expanded", "postdoc_boards", "postdoc_boards_expanded"]

    for key in all_keys:
        for r in results[key]:
            if r["status"] == "RELEVANT":
                total_relevant += 1
                n = len(r.get("postings_found", []))
                total_postings += n
                posting_str = (
                    f" ({n} posting{'s' if n != 1 else ''} extracted)"
                    if n else " (keywords matched, no structured postings found)"
                )
                print(f"  RELEVANT: {r['name']}{posting_str}")
                for p in r.get("postings_found", []):
                    deadline_str = f" — deadline: {p['deadline']}" if p.get('deadline') else ""
                    print(f"    - {p['title']}{deadline_str}")

    print(f"\nTotal relevant orgs: {total_relevant}")
    print(f"Total postings extracted: {total_postings}")
    print(f"News items: {len(results['news'])}")

    return results


if __name__ == "__main__":
    run_scan()
