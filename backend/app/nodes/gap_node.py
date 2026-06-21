from app.llm.groq_client import generate_response

def gap_node(state):
    combined = "\n\n".join(
        item["analysis"] for item in state["extracted_data"]
    )

    prompt = f"""
    Based only on the analyses below, identify recurring research gaps:

    {combined}
    """

    gaps = generate_response(prompt)

    return {**state, "gaps": gaps}