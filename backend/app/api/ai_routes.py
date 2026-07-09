from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel


from app.graph.builder import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    interaction: Optional[dict] = None


@router.post("/chat")
def chat(request: ChatRequest):

    state = {

        # User input
        "message": request.message,

        # Planner
        "plan": [],

        # Executor
        "current_step": 0,

        # CRM Data
        "interaction": request.interaction or {},

        # Search
        "search_results": [],

        # AI Outputs
        "summary": "",
        "medical_insights": "",
        "recommendations": "",

        # Execution status
        "tool_result": "",

        # Final response
        "final_response": {},

    }

    result = graph.invoke(state)

    return result.get("final_response", {})