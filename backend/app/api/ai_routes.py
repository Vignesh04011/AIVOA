from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.builder import build_graph

router = APIRouter()

graph = build_graph()


class ParseRequest(BaseModel):
    text: str


@router.post("/parse-interaction")
def parse_interaction(request: ParseRequest):

    state = {

        "interaction": request.text,

        "summary": "",

        "medical_insights": "",

        "recommendations": "",

        "final_response": {},

    }

    result = graph.invoke(state)

    return result["final_response"]