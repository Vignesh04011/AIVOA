from langgraph.graph import StateGraph, END

from app.state.graph_state import GraphState

from app.agents.supervisor_agent import supervisor_agent
from app.agents.interaction_agent import interaction_agent
from app.agents.edit_agent import edit_agent
from app.agents.summary_agent import summary_agent
from app.agents.medical_agent import medical_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.formatter_agent import formatter_agent


def router(state):

    tool = state["tool"]

    if tool == "extract":
        return "interaction"

    elif tool == "edit":
        return "edit"

    elif tool == "summary":
        return "summary"

    elif tool == "medical":
        return "medical"

    elif tool == "recommendation":
        return "recommendation"

    return "formatter"


def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("interaction", interaction_agent)
    workflow.add_node("edit", edit_agent)
    workflow.add_node("summary", summary_agent)
    workflow.add_node("medical", medical_agent)
    workflow.add_node("recommendation", recommendation_agent)
    workflow.add_node("formatter", formatter_agent)

    workflow.set_entry_point("supervisor")

    workflow.add_conditional_edges(
        "supervisor",
        router,
        {
            "interaction": "interaction",
            "edit": "edit",
            "summary": "summary",
            "medical": "medical",
            "recommendation": "recommendation",
            "formatter": "formatter",
        },
    )

    workflow.add_edge("interaction", "formatter")
    workflow.add_edge("edit", "formatter")
    workflow.add_edge("summary", "formatter")
    workflow.add_edge("medical", "formatter")
    workflow.add_edge("recommendation", "formatter")

    workflow.add_edge("formatter", END)

    return workflow.compile()


graph = build_graph()