import requests
import xml.etree.ElementTree as ET
from app.config import MAX_RESULTS, REQUEST_TIMEOUT

def search_arxiv(query: str):
    base_url = "http://export.arxiv.org/api/query"
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    try:
        response = requests.get(
            base_url,
            params={
                "search_query": query,
                "start": 0,
                "max_results": MAX_RESULTS
            },
            timeout=REQUEST_TIMEOUT
        )

        root = ET.fromstring(response.text)

    except Exception:
        return []

    papers = []

    for entry in root.findall("atom:entry", ns):
        title = entry.findtext("atom:title", namespaces=ns)
        summary = entry.findtext("atom:summary", namespaces=ns)
        link = entry.findtext("atom:id", namespaces=ns)

        if summary:
            papers.append({
                "title": title.strip(),
                "abstract": summary.strip(),
                "url": link.strip(),
                "source": "ArXiv"
            })

    return papers