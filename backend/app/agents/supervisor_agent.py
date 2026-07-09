import json
import re

from app.config.groq_client import client


def supervisor_agent(state):

    message = state["message"]
    interaction = state.get("interaction", {})

    prompt = f"""
You are the Planner of an AI Healthcare CRM.

You receive:

1. The current interaction (may be empty).
2. The latest user message.

Your ONLY job is to decide which tool(s) should execute.

Current Interaction:

{json.dumps(interaction, indent=2)}

Latest User Message:

{message}

Available tools:

extract
edit
summary
medical
recommendation
search
save

Rules:

1. If there is NO interaction yet and the user is describing a meeting,
choose:

{{"plan":["extract"]}}

2. If an interaction already exists and the user is correcting or modifying it,
choose:

{{"plan":["edit"]}}

Examples of edit requests:

- actually...
- sorry...
- change...
- update...
- remove...
- delete...
- make it...
- it was...
- attendees were...
- instead...
- also add...

3. If the user asks for a summary:

{{"plan":["summary"]}}

4. If the user asks for medical insights:

{{"plan":["medical"]}}

5. If the user asks for recommendations:

{{"plan":["recommendation"]}}

6. If the user asks to search previous interactions:

{{"plan":["search"]}}

7. If the user asks to save/log the interaction:

{{"plan":["save"]}}

8. If multiple actions are requested, return them in order.

Examples:

User:
I met Dr Smith yesterday around 8 PM.

Output:
{{"plan":["extract"]}}

---------------------

Current Interaction:
{{"hcp_name":"Dr Smith"}}

User:
Actually it was Dr Eva.

Output:
{{"plan":["edit"]}}

---------------------

Current Interaction:
{{"hcp_name":"Dr Smith"}}

User:
Change the meeting time to 7 PM.

Output:
{{"plan":["edit"]}}

---------------------

User:
Show all meetings with Dr Smith.

Output:
{{"plan":["search"]}}

---------------------

User:
Summarize this interaction.

Output:
{{"plan":["summary"]}}

Return ONLY valid JSON.
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

    # -----------------------------
    # Safety fallback for edits
    # -----------------------------
    lower = message.lower()

    edit_keywords = [
        "change",
        "update",
        "remove",
        "delete",
        "actually",
        "sorry",
        "instead",
        "make it",
        "it was",
        "correct",
        "edit",
        "rename",
        "replace",
        "modify",
        "also add",
    ]

    if interaction and any(word in lower for word in edit_keywords):
        plan = ["edit"]

    state["plan"] = plan
    state["current_step"] = 0
    state["tool_result"] = ""

    return state