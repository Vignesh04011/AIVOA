from app.config.groq_client import client


def medical_agent(state):

    interaction = state.get("interaction", {})

    prompt = f"""
You are a Medical Affairs AI Assistant.

Analyze ONLY this interaction.

Interaction:

{interaction}

Provide:

- Medical insights
- Therapy discussion observations
- Scientific discussion observations
- Educational opportunities

Do NOT summarize.

Do NOT recommend follow-up actions.

Return only the medical insights.
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

    state["medical_insights"] = (
        response.choices[0].message.content.strip()
    )

    return state