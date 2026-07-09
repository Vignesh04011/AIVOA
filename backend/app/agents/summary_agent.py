from app.config.groq_client import client


def summary_agent(state):

    interaction = state["interaction"]

    prompt = f"""
You are an AI Healthcare CRM assistant.

Generate a concise professional summary of this HCP interaction.

Interaction:

{interaction}

Return only the summary.
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

    state["summary"] = response.choices[0].message.content.strip()

    return state