from concurrent.futures import ThreadPoolExecutor
from app.search.pubmed import search_pubmed
from app.search.arxiv import search_arxiv

def search_node(state):
    query = state["query"]

    with ThreadPoolExecutor(max_workers=2) as executor:
        pubmed_future = executor.submit(search_pubmed, query)
        arxiv_future = executor.submit(search_arxiv, query)

        papers = pubmed_future.result() + arxiv_future.result()

    return {**state, "papers": papers}