from app.config.groq_client import client


def medical_agent(state):

    prompt = f"""
Review this healthcare interaction.

Summary:

{state['summary']}

Provide medical insights only.
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

    state["medical_insights"] = response.choices[0].message.content

    return state