from langgraph.graph import StateGraph, END

from app.state.graph_state import GraphState

from app.agents.supervisor_agent import supervisor_agent
from app.agents.executor_agent import executor_agent
from app.agents.formatter_agent import formatter_agent


def build_graph():

    workflow = StateGraph(GraphState)

    # Nodes
    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("executor", executor_agent)
    workflow.add_node("formatter", formatter_agent)

    # Entry Point
    workflow.set_entry_point("supervisor")

    # Flow
    workflow.add_edge("supervisor", "executor")
    workflow.add_edge("executor", "formatter")
    workflow.add_edge("formatter", END)

    return workflow.compile()


graph = build_graph()