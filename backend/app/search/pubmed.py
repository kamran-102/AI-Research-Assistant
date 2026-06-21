import requests
import xml.etree.ElementTree as ET
from app.config import MAX_RESULTS, REQUEST_TIMEOUT

def search_pubmed(query: str):
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    try:
        search_resp = requests.get(
            search_url,
            params={
                "db": "pubmed",
                "term": query,
                "retmax": MAX_RESULTS,
                "retmode": "json"
            },
            timeout=REQUEST_TIMEOUT
        )

        ids = search_resp.json()["esearchresult"]["idlist"]

        if not ids:
            return []

        fetch_resp = requests.get(
            fetch_url,
            params={
                "db": "pubmed",
                "id": ",".join(ids),
                "retmode": "xml"
            },
            timeout=REQUEST_TIMEOUT
        )

        root = ET.fromstring(fetch_resp.text)

    except Exception:
        return []

    papers = []

    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle", default="No Title")
        abstract = article.findtext(".//Abstract/AbstractText")
        pmid = article.findtext(".//PMID")

        if abstract:
            papers.append({
                "title": title,
                "abstract": abstract.strip(),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "source": "PubMed"
            })

    return papers