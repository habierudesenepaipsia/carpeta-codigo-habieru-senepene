
#URL_MED = "https://wsearch.nlm.nih.gov/ws/query"
#URL_MED = "https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=asthma"

#PARAMETERS
#db = Database to search -> healthTopics ? healthTopicsSpanish
#term = Text query submitted to the Web service ->
#EXAMPLE URL
#https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=asthma 

import re
import requests
import xml.etree.ElementTree as ET

URL_MED = "https://wsearch.nlm.nih.gov/ws/query"

def clean(text):
    # Strip leftover HTML tags and tidy whitespace
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()

def search_condition(term, lang_db="healthTopics", max_results=3):
    params = {
        "db": lang_db,
        "term": term,
        "retmax": max_results,
        "tool": "my_school_project",   # recommended by NLM
    }
    resp = requests.get(URL_MED, params=params, timeout=5)
    resp.raise_for_status()

    root = ET.fromstring(resp.content)
    results = []
    for doc in root.iter("document"):
        item = {"url": doc.get("url")}
        for content in doc.findall("content"):
            name = content.get("name")
            if name in ("title", "FullSummary"):
                item[name] = clean("".join(content.itertext()))
        results.append(item)
    return results

if __name__ == "__main__":
    for r in search_condition("tourette syndrome"):
        print("TITLE:  ", r.get("title"))
        print("URL:    ", r.get("url"))
        print("SUMMARY:", r.get("FullSummary"))
        print("-" * 60)

