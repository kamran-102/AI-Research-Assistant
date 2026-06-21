from concurrent.futures import ThreadPoolExecutor
from app.config import MAX_WORKERS
from app.llm.groq_client import generate_response

def analyze_paper(paper):
    prompt = f"""
    Extract:
    - Methods used
    - Key findings
    - Limitations

    Text:
    {paper['abstract']}
    """
    return {
        "paper": paper,
        "analysis": generate_response(prompt)
    }

def extract_node(state):
    papers = state["papers"]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        extracted = list(executor.map(analyze_paper, papers))

    return {**state, "extracted_data": extracted}