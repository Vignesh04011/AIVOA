from app.config.groq_client import client


def summary_agent(state):

    interaction = state.get("interaction", {})

    prompt = f"""
You are an AI Healthcare CRM assistant.

Generate a concise professional summary of this HCP interaction.

Interaction:

{interaction}

Rules:

- Only summarize the interaction.
- Do not generate recommendations.
- Do not generate medical insights.
- Return only the summary.
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

    state["summary"] = response.choices[0].message.content.strip()

    return state