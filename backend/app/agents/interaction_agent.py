from app.config.groq_client import client


def interaction_agent(state):

    interaction = state["interaction"]

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

Summarize this interaction.

Interaction:

{interaction}
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

    state["summary"] = response.choices[0].message.content

    return state