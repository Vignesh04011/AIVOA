from app.config.groq_client import client


def recommendation_agent(state):

    prompt = f"""
Based on this interaction summary,

{state['summary']}

Generate follow-up recommendations.
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

    state["recommendations"] = response.choices[0].message.content

    return state