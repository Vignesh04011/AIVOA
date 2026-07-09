def formatter_agent(state):

    plan = state.get("plan", [])

    response = {

        "success": True,

        "plan": plan,

        "message": "",

        "form_data": state.get("interaction", {}),

        "summary": state.get("summary", ""),

        "medical_insights": state.get("medical_insights", ""),

        "recommendations": state.get("recommendations", ""),

        "search_results": state.get("search_results", []),

    }

    messages = []

    if "extract" in plan:
        messages.append("Interaction extracted successfully.")

    if "edit" in plan:
        messages.append("Interaction updated successfully.")

    if "summary" in plan:
        messages.append("Summary generated.")

    if "medical" in plan:
        messages.append("Medical insights generated.")

    if "recommendation" in plan:
        messages.append("Recommendations generated.")

    if "search" in plan:
        messages.append("Search completed successfully.")

    if "save" in plan:

     messages.append(

        state.get(
            "tool_result",
            "Interaction logged successfully."
        )

    )

    response["message"] = "\n".join(messages)

    # ⭐ THIS WAS MISSING
    state["final_response"] = response

    return state