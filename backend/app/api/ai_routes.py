from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.builder import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    state = {

        "message": request.message,

        "tool": "",

        "interaction": {},

        "summary": "",

        "medical_insights": "",

        "recommendations": "",

        "final_response": {},

    }

    result = graph.invoke(state)

    return result["final_response"]