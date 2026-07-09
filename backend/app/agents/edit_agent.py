from app.config.groq_client import client
import json
import re


def edit_agent(state):

    interaction = state.get("interaction", {})
    user_message = state["message"]

    prompt = f"""
You are an AI CRM Assistant.

The user is editing an already extracted Healthcare Professional interaction.

Current Interaction

{json.dumps(interaction, indent=2)}

User Request

{user_message}

Rules:

- Understand natural language.
- Modify ONLY the requested fields.
- Preserve every other field exactly.
- Never remove unrelated data.
- If the user says remove/delete, replace that field with an empty string.
- If the user changes time/date, update only that field.
- If the user changes doctor name, update only hcp_name.
- If the user adds another discussion topic, append it naturally.
- Return ONLY valid JSON.
- Return the COMPLETE interaction.
- No markdown.
- No explanation.
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

    content = response.choices[0].message.content.strip()
    content = re.sub(r"```json|```", "", content).strip()

    try:
        state["interaction"] = json.loads(content)

    except Exception:
        # If parsing fails, keep the previous interaction
        pass

    return state