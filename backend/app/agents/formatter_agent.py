def formatter_agent(state):

    state["final_response"] = {
        "summary": state["summary"],
        "medical_insights": state["medical_insights"],
        "recommendations": state["recommendations"],
    }

    return state