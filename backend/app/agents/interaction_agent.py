from app.config.groq_client import client
import json
import re


def interaction_agent(state):

    message = state["message"]

    prompt = f"""
You are an AI Healthcare CRM assistant.

Your ONLY job is to extract structured interaction information.

DO NOT summarize.
DO NOT generate recommendations.
DO NOT generate medical insights.

Today's date is 2026-07-09.

Return interaction_date in YYYY-MM-DD format.

Return interaction_time in HH:MM:SS (24-hour).

Examples:
20:00:00
09:30:00

interaction_type must be exactly one of:

Meeting
Call
Email
Conference

If any field is unknown, return an empty string.

Return ONLY valid JSON.

{{
    "hcp_name":"",
    "interaction_type":"",
    "interaction_date":"",
    "interaction_time":"",
    "attendees":"",
    "topics_discussed":"",
    "materials_shared":"",
    "sentiment":"",
    "outcomes":"",
    "follow_up_actions":""
}}

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
    )

    content = response.choices[0].message.content.strip()
    content = re.sub(r"```json|```", "", content).strip()

    try:

        state["interaction"] = json.loads(content)

    except Exception:

        state["interaction"] = {
            "hcp_name": "",
            "interaction_type": "",
            "interaction_date": "",
            "interaction_time": "",
            "attendees": "",
            "topics_discussed": "",
            "materials_shared": "",
            "sentiment": "",
            "outcomes": "",
            "follow_up_actions": "",
        }

    return state