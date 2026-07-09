def formatter_agent(state):

    state["final_response"] = {

        "form_data": state["interaction"],

        "summary": state["summary"],

        "medical_insights": state["medical_insights"],

        "recommendations": state["recommendations"],

    }

    return state