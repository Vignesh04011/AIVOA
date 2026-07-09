from app.config.groq_client import client


def recommendation_agent(state):

    interaction = state["interaction"]

    prompt = f"""
You are an AI Healthcare CRM assistant.

Below is an HCP interaction.

Interaction:

{interaction}

Generate professional follow-up recommendations for the sales representative.

Rules:

- Suggest practical next actions.
- Do NOT summarize the interaction.
- Do NOT generate medical insights.
- Return only the recommendations.
"""

    response = client.chat.completions.create(
        model="gemma2-9b-it",
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