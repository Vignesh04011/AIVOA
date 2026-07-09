from app.config.groq_client import client


VALID_TOOLS = [
    "extract",
    "edit",
    "summary",
    "medical",
    "recommendation",
    "save",
]


def supervisor_agent(state):

    message = state["message"]

    prompt = f"""
You are the Supervisor of an AI Healthcare CRM.

Your ONLY job is to decide which tool should execute.

Return ONLY ONE WORD.

Allowed outputs:

extract
edit
summary
medical
recommendation
save

Examples

User: I met Dr Smith yesterday.
Output:
extract

User: Change meeting time to 7 PM.
Output:
edit

User: Delete brochure.
Output:
edit

User: Summarize.
Output:
summary

User: Give medical insights.
Output:
medical

User: Recommend follow up.
Output:
recommendation

User: Log interaction.
Output:
save

User:

{message}
"""

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    tool = (
        response.choices[0]
        .message.content.strip()
        .lower()
        .replace(".", "")
        .replace("`", "")
    )

    tool = tool.split()[0]

    if tool not in VALID_TOOLS:
        tool = "extract"

    state["tool"] = tool

    return state