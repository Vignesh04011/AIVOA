import json
import re

from app.config.groq_client import client


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

Your job is to update ONLY what the user requested.

Rules:

- Preserve every existing field unless the user explicitly changes it.
- Never remove unrelated information.
- If the user says remove/delete/clear, return an empty string for ONLY that field.
- If the user changes the doctor name, update ONLY hcp_name.
- If the user changes date/time, update ONLY those fields.
- If the user adds discussion topics, append naturally.
- Return the COMPLETE interaction.
- Return ONLY valid JSON.
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

        updated = json.loads(content)

        merged = interaction.copy()

        lower = user_message.lower()

        remove_words = [
            "remove",
            "delete",
            "clear",
            "erase",
        ]

        removing = any(word in lower for word in remove_words)

        for key, value in updated.items():

            # Skip nulls
            if value is None:
                continue

            # Ignore accidental empty strings unless user is removing data
            if value == "" and not removing:
                continue

            merged[key] = value

        state["interaction"] = merged

    except Exception as e:

        print("Edit Agent JSON Error:", e)
        print(content)

        # Preserve previous interaction
        state["interaction"] = interaction

    return state