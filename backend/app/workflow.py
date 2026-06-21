from langgraph.graph import StateGraph, END
from app.models import ResearchState
from app.nodes.search_node import search_node
from app.nodes.extract_node import extract_node
from app.nodes.gap_node import gap_node
from app.nodes.format_node import format_node

def build_workflow():
    workflow = StateGraph(ResearchState)

    workflow.add_node("search", search_node)
    workflow.add_node("extract", extract_node)
    workflow.add_node("gap", gap_node)
    workflow.add_node("format", format_node)

    workflow.set_entry_point("search")

    workflow.add_edge("search", "extract")
    workflow.add_edge("extract", "gap")
    workflow.add_edge("gap", "format")
    workflow.add_edge("format", END)

    return workflow.compile()