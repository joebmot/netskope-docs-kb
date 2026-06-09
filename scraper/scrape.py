"""
Netskope Docs Scraper
---------------------
Reads 3 sitemaps, scrapes each page, extracts full clean text,
categorizes by product/topic, and writes per-topic .md files
plus a master index.json to /data/.

Run locally:  python scraper/scrape.py
Run in CI:    triggered by GitHub Actions (.github/workflows/daily_scrape.yml)
"""

import os
import json
import time
import hashlib
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from bs4 import BeautifulSoup

# ── Config ────────────────────────────────────────────────────────────────────

SITEMAPS = [
    "https://docs.netskope.com/topic-sitemap.xml",
    "https://docs.netskope.com/products-sitemap.xml",
    "https://docs.netskope.com/release_note-sitemap.xml",
]

DATA_DIR = Path(__file__).parent.parent / "data"
TOPICS_DIR = DATA_DIR / "topics"
INDEX_FILE = DATA_DIR / "index.json"
CHANGELOG_FILE = DATA_DIR / "changelog.md"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; NetskopeDocsBot/1.0; "
        "+https://github.com/joebmot/netskope-docs-kb)"
    )
}

REQUEST_DELAY = 1.0
MAX_RETRIES = 3

# ── Topic categorisation ──────────────────────────────────────────────────────

TOPIC_MAP = [
    (["ztna", "private-access", "zero-trust"],               "ztna"),
    (["casb", "api-connectors", "api-monitor", "api-observe"],"casb"),
    (["dlp", "data-loss", "exact-data-match", "edm"],        "dlp"),
    (["swg", "web-gateway", "real-time-protection"],          "swg"),
    (["firewall", "cloud-firewall", "nfw"],                   "firewall"),
    (["sase", "borderless-wan", "sd-wan"],                    "sase"),
    (["threat", "malware", "advanced-threat"],                "threat_protection"),
    (["uba", "user-behavior", "ueba"],                        "uba"),
    (["client", "netskope-client", "ns-client"],              "client"),
    (["release", "release-note", "whats-new"],                "release_notes"),
    (["admin", "console", "tenant"],                          "admin"),
    (["log", "siem", "export"],                               "logging_siem"),
    (["identity", "idp", "saml", "sso"],                      "identity"),
    (["network", "steering", "traffic"],                      "network_steering"),
]

DEFAULT_TOPIC = "general"


def categorise(url: str) -> str:
    url_lower = url.lower()
    for keywords, topic in TOPIC_MAP:
        if any(kw in url_lower for kw in keywords):
            return topic
    return DEFAULT_TOPIC


# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch(url: str, retries: int = MAX_RETRIES):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            print(f"  ⚠ Attempt {attempt}/{retries} failed for {url}: {e}")
            if attempt < retries:
                time.sleep(2 ** attempt)
    return None


def parse_sitemap(url: str) -> list:
    print(f"📋 Parsing sitemap: {url}")
    r = fetch(url)
    if not r:
        print(f"  ✗ Could not fetch sitemap: {url}")
        return []
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    try:
        root = ET.fromstring(r.text)
    except ET.ParseError as e:
        print(f"  ✗ XML parse error: {e}")
        return []
    entries = []
    for url_el in root.findall("sm:url", ns):
        loc = url_el.findtext("sm:loc", namespaces=ns, default="").strip()
        lastmod = url_el.findtext("sm:lastmod", namespaces=ns, default="").strip()
        if loc:
            entries.append({"loc": loc, "lastmod": lastmod})
    print(f"  ✓ Found {len(entries)} URLs")
    return entries


def extract_text(html: str, url: str):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select(
        "nav, header, footer, .site-header, .site-footer, "
        ".sidebar, .nav-menu, .breadcrumb, #wpadminbar, "
        ".wp-block-navigation, script, style, [aria-hidden='true']"
    ):
        tag.decompose()
    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else url.rstrip("/").split("/")[-1]
    body = (
        soup.find("article")
        or soup.find("main")
        or soup.find(class_=["entry-content", "post-content", "article-body"])
        or soup.find("body")
    )
    text = body.get_text(separator="\n", strip=True) if body else soup.get_text(separator="\n", strip=True)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return title, "\n".join(lines)


def content_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()[:12]


# ── Main ──────────────────────────────────────────────────────────────────────

def scrape_all():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    existing_index = {}
    if INDEX_FILE.exists():
        try:
            existing_index = {e["url"]: e for e in json.loads(INDEX_FILE.read_text())}
        except Exception:
            existing_index = {}

    all_entries = {}
    for sitemap_url in SITEMAPS:
        for entry in parse_sitemap(sitemap_url):
            all_entries[entry["loc"]] = entry

    print(f"\n🔍 Total unique URLs to scrape: {len(all_entries)}\n")

    new_index = []
    topic_pages = {}
    changed = []
    added = []
    errors = []

    for i, (url, entry) in enumerate(all_entries.items(), 1):
        print(f"[{i}/{len(all_entries)}] {url}")
        r = fetch(url)
        if not r:
            errors.append(url)
            continue
        title, text = extract_text(r.text, url)
        topic = categorise(url)
        chash = content_hash(text)
        lastmod = entry.get("lastmod", "")
        scraped_at = datetime.now(timezone.utc).isoformat()

        index_entry = {
            "url": url, "title": title, "topic": topic,
            "lastmod": lastmod, "scraped_at": scraped_at, "hash": chash,
        }
        new_index.append(index_entry)

        prev = existing_index.get(url)
        if prev is None:
            added.append(url)
        elif prev.get("hash") != chash:
            changed.append(url)

        page_block = (
            f"---\n## {title}\n"
            f"**URL:** {url}\n"
            f"**Last Modified:** {lastmod or 'unknown'}\n"
            f"**Scraped:** {scraped_at}\n\n{text}\n"
        )
        topic_pages.setdefault(topic, []).append(page_block)
        time.sleep(REQUEST_DELAY)

    print(f"\n✍ Writing {len(topic_pages)} topic files...")
    for topic, pages in topic_pages.items():
        topic_file = TOPICS_DIR / f"{topic}.md"
        header = (
            f"# Netskope Docs — {topic.replace('_', ' ').title()}\n"
            f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_\n"
            f"_Pages: {len(pages)}_\n\n"
        )
        topic_file.write_text(header + "\n".join(pages), encoding="utf-8")
        print(f"  ✓ {topic}.md ({len(pages)} pages)")

    INDEX_FILE.write_text(json.dumps(new_index, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ index.json written ({len(new_index)} entries)")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# Changelog — {ts}",
        f"\n**Total pages:** {len(new_index)}",
        f"**New:** {len(added)}  |  **Updated:** {len(changed)}  |  **Errors:** {len(errors)}",
        "",
    ]
    if added:
        lines += ["## New Pages"] + [f"- {u}" for u in added[:50]] + [""]
    if changed:
        lines += ["## Updated Pages"] + [f"- {u}" for u in changed[:50]] + [""]
    if errors:
        lines += ["## Errors"] + [f"- {u}" for u in errors] + [""]
    CHANGELOG_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ changelog.md written")
    print(f"\n✅ Done. {len(new_index)} pages | {len(added)} new | {len(changed)} changed | {len(errors)} errors")


if __name__ == "__main__":
    scrape_all()
