from sqlalchemy.orm import Session

from app.database.models import Interaction
from app.schemas.interaction import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(
        hcp_name=interaction.hcp_name,
        interaction_type=interaction.interaction_type,
        interaction_date=interaction.interaction_date,
        interaction_time=interaction.interaction_time,
        attendees=interaction.attendees,
        topics_discussed=interaction.topics_discussed,
        materials_shared=interaction.materials_shared,
        sentiment=interaction.sentiment,
        outcomes=interaction.outcomes,
        follow_up_actions=interaction.follow_up_actions,
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction