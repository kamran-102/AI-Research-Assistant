from app.llm.groq_client import generate_response

def format_node(state):

    evidence_text = ""
    urls = set()

    for item in state["extracted_data"]:
        paper = item["paper"]
        urls.add(paper["url"])

        evidence_text += f"""
Title: {paper['title']}
Source: {paper['source']}
URL: {paper['url']}

Analysis:
{item['analysis']}
"""

    prompt = f"""
    Answer the biomedical question using ONLY the provided evidence.

    Question:
    {state['query']}

    Evidence:
    {evidence_text}

    Write structured sections:

    Introduction

    Methods (briefly describe search strategy and selection process)

    Description
    - Provide a detailed synthesis of findings.
    - Provide description ensuring coherence and cohesion so that a reader can easily comprehend the content
    - Compare and contrast studies where possible.
    - Explain patterns, consistencies, and disagreements.
    - Minimum 2 to 3 well-developed paragraphs.
    - Avoid mentioning any reference in the description
    - Avoid generic statements.
    - Use analytical language.

    Conclusion

    Research Gaps (based only on analyses)

    References
    - Include ONLY the provided URLs.
    - Do NOT invent references.
    - Do NOT duplicate references.
    - Just add URLs in the references

    Do NOT add funding or conflict sections.
    """

    final_output = generate_response(prompt)

    return {**state, "final_output": final_output}