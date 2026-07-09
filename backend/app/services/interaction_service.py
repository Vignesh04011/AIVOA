from app.graph.workflow import graph


def process_interaction(interaction):

    state = {
        "interaction": interaction,
        "summary": "",
        "medical_insights": "",
        "recommendations": "",
        "final_response": {},
    }

    result = graph.invoke(state)

    return result["final_response"]