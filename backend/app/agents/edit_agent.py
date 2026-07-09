from app.config.groq_client import client
import json
import re


def edit_agent(state):

    interaction = state["interaction"]
    command = state["message"]

    prompt = f"""
You are an AI CRM assistant.

Current interaction:

{interaction}

User wants to edit it:

{command}

Update ONLY the requested fields.

Return ONLY valid JSON.

Do not explain.

Return the complete updated interaction.
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

    state["interaction"] = json.loads(content)

    return state