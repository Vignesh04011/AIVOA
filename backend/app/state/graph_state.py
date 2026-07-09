from typing import TypedDict


class GraphState(TypedDict):
    interaction: dict

    summary: str

    medical_insights: str

    recommendations: str

    final_response: dict