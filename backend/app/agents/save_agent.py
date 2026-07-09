from datetime import datetime

from app.database.database import SessionLocal
from app.database.models import Interaction


def save_agent(state):

    interaction = state.get("interaction", {})

    db = SessionLocal()

    try:

        interaction_date = (
            datetime.strptime(
                interaction["interaction_date"],
                "%Y-%m-%d",
            ).date()
            if interaction.get("interaction_date")
            else None
        )

        interaction_time = (
            datetime.strptime(
                interaction["interaction_time"],
                "%H:%M:%S",
            ).time()
            if interaction.get("interaction_time")
            else None
        )

        record = Interaction(

            hcp_name=interaction.get("hcp_name", ""),

            interaction_type=interaction.get("interaction_type", ""),

            interaction_date=interaction_date,

            interaction_time=interaction_time,

            attendees=interaction.get("attendees", ""),

            topics_discussed=interaction.get("topics_discussed", ""),

            materials_shared=interaction.get("materials_shared", ""),

            sentiment=interaction.get("sentiment", ""),

            outcomes=interaction.get("outcomes", ""),

            follow_up_actions=interaction.get("follow_up_actions", ""),

        )

        db.add(record)

        db.commit()

        db.refresh(record)

        state["saved_id"] = record.id

        state["tool_result"] = (
            f"Interaction saved successfully. ID: {record.id}"
        )

    except Exception as e:

        db.rollback()

        state["tool_result"] = (
            f"Save failed: {str(e)}"
        )

    finally:

        db.close()

    return state