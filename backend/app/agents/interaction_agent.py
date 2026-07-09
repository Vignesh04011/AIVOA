from app.config.groq_client import client
import json
import re


def interaction_agent(state):

    interaction = state["interaction"]

    prompt = f"""
You are an AI Healthcare CRM assistant.

Extract the interaction AND generate a short summary.

Today's date is 2026-07-09.

Return interaction_date in YYYY-MM-DD format.

Return interaction_time in 24-hour HH:MM:SS format.

Example:
20:00:00
09:30:00

For interaction_type use one of:
Meeting
Call
Email
Conference

IMPORTANT:
Return ONLY valid JSON.
Do not explain anything.
Do not use markdown.
Do not wrap the JSON in ```.

Return exactly in this format:

{{
    "interaction": {{
        "hcp_name": "",
        "interaction_type": "",
        "interaction_date": "",
        "interaction_time": "",
        "attendees": "",
        "topics_discussed": "",
        "materials_shared": "",
        "sentiment": "",
        "outcomes": "",
        "follow_up_actions": ""
    }},
    "summary": ""
}}

User Input:

{interaction}
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

    content = response.choices[0].message.content.strip()
    content = re.sub(r"```json|```", "", content).strip()

    data = json.loads(content)

    state["interaction"] = data["interaction"]
    state["summary"] = data["summary"]

    return state