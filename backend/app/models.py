from typing import TypedDict, List, Dict

class ResearchState(TypedDict):
    query: str
    papers: List[Dict]
    extracted_data: List[Dict]
    gaps: str
    final_output: str