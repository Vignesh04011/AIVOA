from app.config.groq_client import client


def recommendation_agent(state):

    interaction = state.get("interaction", {})

    prompt = f"""
You are an AI CRM Assistant.

Interaction:

{interaction}

Generate practical follow-up actions.

Rules:

- Only recommendations.
- No summary.
- No medical insights.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    state["recommendations"] = (
        response.choices[0].message.content.strip()
    )

    return state