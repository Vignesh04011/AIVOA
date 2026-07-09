from langgraph.graph import StateGraph, END

from app.state.graph_state import GraphState

from app.agents.interaction_agent import interaction_agent
from app.agents.supervisor import supervisor
from app.agents.medical_agent import medical_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.formatter_agent import formatter_agent


def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("interaction", interaction_agent)
    workflow.add_node("supervisor", supervisor)
    workflow.add_node("medical", medical_agent)
    workflow.add_node("recommendation", recommendation_agent)
    workflow.add_node("formatter", formatter_agent)

    workflow.set_entry_point("interaction")

    workflow.add_edge("interaction", "supervisor")
    workflow.add_edge("supervisor", "medical")
    workflow.add_edge("medical", "recommendation")
    workflow.add_edge("recommendation", "formatter")
    workflow.add_edge("formatter", END)

    return workflow.compile()