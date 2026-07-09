from typing import TypedDict


class GraphState(TypedDict):
    interaction: dict | str

    summary: str

    medical_insights: str

    recommendations: str

    final_response: dict