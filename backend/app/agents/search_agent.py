import json
import re

from sqlalchemy import func

from app.database.database import SessionLocal
from app.database.models import Interaction
from app.config.groq_client import client


def search_agent(state):

    db = SessionLocal()

    try:

        message = state["message"]

        # -----------------------------
        # Step 1 : AI extracts filters
        # -----------------------------

        extraction_prompt = f"""
You are an AI CRM Search Assistant.

Understand the user's request and extract search filters.

Return ONLY valid JSON.

Format:

{{
    "hcp_name":"",
    "interaction_type":"",
    "topic":"",
    "sentiment":"",
    "materials_shared":"",
    "follow_up":"",
    "date_filter":""
}}

Examples

User:
Show all meetings with Dr Smith.

Output:
{{
    "hcp_name":"Dr Smith",
    "interaction_type":"Meeting",
    "topic":"",
    "sentiment":"",
    "materials_shared":"",
    "follow_up":"",
    "date_filter":""
}}

----------------

User:
Show doctors interested in diabetes.

Output:
{{
    "hcp_name":"",
    "interaction_type":"",
    "topic":"diabetes",
    "sentiment":"",
    "materials_shared":"",
    "follow_up":"",
    "date_filter":""
}}

----------------

User:
Show positive interactions this month.

Output:
{{
    "hcp_name":"",
    "interaction_type":"",
    "topic":"",
    "sentiment":"Positive",
    "materials_shared":"",
    "follow_up":"",
    "date_filter":"this month"
}}

----------------

User:

{message}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": extraction_prompt}],
            temperature=0,
        )

        content = response.choices[0].message.content.strip()

        content = re.sub(r"```json|```", "", content).strip()

        filters = json.loads(content)

        # -----------------------------
        # Step 2 : Build SQL Query
        # -----------------------------

        query = db.query(Interaction)

        if filters["hcp_name"]:

            query = query.filter(
                Interaction.hcp_name.ilike(
                    f"%{filters['hcp_name']}%"
                )
            )

        if filters["interaction_type"]:

            query = query.filter(
                Interaction.interaction_type.ilike(
                    f"%{filters['interaction_type']}%"
                )
            )

        if filters["topic"]:

            query = query.filter(
                Interaction.topics_discussed.ilike(
                    f"%{filters['topic']}%"
                )
            )

        if filters["sentiment"]:

            query = query.filter(
                Interaction.sentiment.ilike(
                    f"%{filters['sentiment']}%"
                )
            )

        if filters["materials_shared"]:

            query = query.filter(
                Interaction.materials_shared.ilike(
                    f"%{filters['materials_shared']}%"
                )
            )

        if filters["follow_up"]:

            query = query.filter(
                Interaction.follow_up_actions.ilike(
                    f"%{filters['follow_up']}%"
                )
            )

        interactions = query.order_by(
            Interaction.interaction_date.desc()
        ).all()

        # -----------------------------
        # Step 3 : Format Results
        # -----------------------------

        records = []

        for row in interactions:

            records.append({

                "hcp_name": row.hcp_name,

                "interaction_type": row.interaction_type,

                "interaction_date": str(row.interaction_date),

                "topics_discussed": row.topics_discussed,

                "materials_shared": row.materials_shared,

                "sentiment": row.sentiment,

                "outcomes": row.outcomes,

                "follow_up_actions": row.follow_up_actions,

            })

        state["search_results"] = records

        # -----------------------------
        # Step 4 : AI summarizes results
        # -----------------------------

        summary_prompt = f"""
You are an AI CRM Copilot.

The user asked:

{message}

Database Results:

{json.dumps(records, indent=2)}

Generate a professional CRM response.

Guidelines:

- Answer the user's question.
- Mention the number of matching interactions.
- Highlight important trends if any.
- Never invent information.
- If no records exist, clearly say so.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": summary_prompt}],
            temperature=0.2,
        )

        state["summary"] = (
            response.choices[0].message.content.strip()
        )

        return state

    finally:

        db.close()