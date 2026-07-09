from app.config.groq_client import client


def medical_agent(state):

    interaction = state["interaction"]

    prompt = f"""
You are a medical affairs AI assistant.

Below is a healthcare professional interaction.

Interaction:

{interaction}

Provide concise medical insights based ONLY on the interaction.

Do not recommend follow-up actions.
Do not summarize the interaction.

Return only the medical insights.
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

    state["medical_insights"] = (
        response.choices[0].message.content.strip()
    )

    return state