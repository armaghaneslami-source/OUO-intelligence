# OUO Intelligence - Scanner
# Monitors target organizations for jobs and news

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from config import KEYWORDS, EUROPE_ORGS, JAPAN_ORGS, POSTDOC_BOARDS, NEWS_SOURCES

def check_keywords(text):
    """Check if any of our keywords appear in the text"""
    text_lower = text.lower()
    found = []
    for keyword in KEYWORDS:
        if keyword.lower() in text_lower:
            found.append(keyword)
    return found

def scan_page(name, url):
    """Visit a page and look for relevant content"""
    print(f"Scanning {name}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get all text from the page
        text = soup.get_text(separator=' ', strip=True)
        
        # Check for our keywords
        matches = check_keywords(text)
        
        if matches:
            return {
                "name": name,
                "url": url,
                "keywords_found": matches,
                "status": "RELEVANT",
                "scanned_at": datetime.now().isoformat()
            }
        else:
            return {
                "name": name,
                "url": url,
                "keywords_found": [],
                "status": "nothing relevant",
                "scanned_at": datetime.now().isoformat()
            }
    except Exception as e:
        return {
            "name": name,
            "url": url,
            "keywords_found": [],
            "status": f"error: {str(e)}",
            "scanned_at": datetime.now().isoformat()
        }

def scan_news(query):
    """Search Google News for relevant developments"""
    print(f"Searching news: {query}...")
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')[:3]  # Top 3 results
        
        results = []
        for item in items:
            results.append({
                "title": item.title.text if item.title else "No title",
                "link": item.link.text if item.link else "",
                "published": item.pubDate.text if item.pubDate else "",
                "query": query
            })
        return results
    except Exception as e:
        print(f"News error for {query}: {e}")
        return []

def run_scan():
    """Run the full OUO Intelligence scan"""
    print("\n🦚 OUO Intelligence scan starting...\n")
    results = {
        "scan_date": datetime.now().isoformat(),
        "europe_jobs": [],
        "japan_jobs": [],
        "postdoc_boards": [],
        "news": []
    }
    
    # Scan Europe organizations
    print("--- EUROPE ORGANIZATIONS ---")
    for name, url in EUROPE_ORGS.items():
        result = scan_page(name, url)
        results["europe_jobs"].append(result)
    
    # Scan Japan organizations
    print("\n--- JAPAN ORGANIZATIONS ---")
    for name, url in JAPAN_ORGS.items():
        result = scan_page(name, url)
        results["japan_jobs"].append(result)
    
    # Scan postdoc boards
    print("\n--- POSTDOC BOARDS ---")
    for name, url in POSTDOC_BOARDS.items():
        result = scan_page(name, url)
        results["postdoc_boards"].append(result)
    
    # Scan news
    print("\n--- NEWS ---")
    for query in NEWS_SOURCES:
        news = scan_news(query)
        results["news"].extend(news)
    
    # Save results
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n🦚 SCAN COMPLETE - Summary:")
    print("\nEUROPE - Relevant findings:")
    for r in results["europe_jobs"]:
        if r["status"] == "RELEVANT":
            print(f"  ✅ {r['name']}: {r['keywords_found']}")
    
    print("\nJAPAN - Relevant findings:")
    for r in results["japan_jobs"]:
        if r["status"] == "RELEVANT":
            print(f"  ✅ {r['name']}: {r['keywords_found']}")
    
    print(f"\nNews items found: {len(results['news'])}")
    print("\nFull results saved to results.json")
    
    return results

if __name__ == "__main__":
    run_scan()
