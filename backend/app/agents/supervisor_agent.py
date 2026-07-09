import json
import re

from app.config.groq_client import client


def supervisor_agent(state):

    message = state["message"]

    prompt = f"""
You are the Planner of an AI Healthcare CRM.

Your job is NOT to be helpful.
Your job is ONLY to identify what the user explicitly requested.

Rules:

1. Never add extra actions.
2. Never assume the user wants a summary.
3. Never assume the user wants recommendations.
4. Never assume the user wants medical insights.
5. Never assume the user wants to save.
6. Execute ONLY what the user explicitly asks.

Available tools:

extract
edit
summary
medical
recommendation
search
save

Examples

User:
I met Dr Smith yesterday around 8 PM.
Output:
{{"plan":["extract"]}}

User:
Summarize this interaction.
Output:
{{"plan":["summary"]}}

User:
Give medical insights.
Output:
{{"plan":["medical"]}}

User:
Recommend follow-up actions.
Output:
{{"plan":["recommendation"]}}

User:
Log this interaction.
Output:
{{"plan":["save"]}}

User:
Change the meeting time to 7 PM.
Output:
{{"plan":["edit"]}}

User:
Show all meetings with Dr Smith.
Output:
{{"plan":["search"]}}

User:
I met Dr Smith yesterday and summarize it.
Output:
{{"plan":["extract","summary"]}}

User:
{message}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    content = re.sub(r"```json|```", "", content).strip()

    try:

        plan = json.loads(content)["plan"]

        if not isinstance(plan, list):
            plan = ["extract"]

    except Exception:

        plan = ["extract"]

    state["plan"] = plan

    # Reset tool execution status
    state["tool_result"] = ""

    return state