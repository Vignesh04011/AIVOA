def formatter_agent(state):

    tool = state.get("tool", "")

    response = {
        "tool": tool,
        "form_data": state.get("interaction", {}),
        "summary": state.get("summary", ""),
        "medical_insights": state.get("medical_insights", ""),
        "recommendations": state.get("recommendations", ""),
        "message": "",
    }

    if tool == "extract":
        response["message"] = "Interaction extracted successfully."

    elif tool == "edit":
        response["message"] = "Interaction updated successfully."

    elif tool == "summary":
        response["message"] = "Summary generated."

    elif tool == "medical":
        response["message"] = "Medical insights generated."

    elif tool == "recommendation":
        response["message"] = "Recommendations generated."

    elif tool == "save":
        response["message"] = "Interaction logged successfully."

    state["final_response"] = response

    return state