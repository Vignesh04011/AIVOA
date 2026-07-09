from app.config.groq_client import client


def supervisor_agent(state):

    message = state["message"]

    prompt = f"""
You are an AI CRM routing agent.

Determine which tool should handle the user's request.

Return ONLY one word.

Available tools:

extract
edit
summary
medical
recommendation
save

Examples:

"I met Dr Smith yesterday."
-> extract

"Change the meeting time to 7 PM."
-> edit

"Delete brochure."
-> edit

"Summarize."
-> summary

"Give medical insights."
-> medical

"Recommend follow up."
-> recommendation

"Log interaction."
-> save

User:

{message}
"""

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["tool"] = response.choices[0].message.content.strip().lower()

    return state