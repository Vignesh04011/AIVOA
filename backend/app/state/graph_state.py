from typing import TypedDict


class GraphState(TypedDict):

    message: str

    tool: str

    interaction: dict

    summary: str

    medical_insights: str

    recommendations: str

    final_response: dict