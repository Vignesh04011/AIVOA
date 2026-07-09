from sqlalchemy import Column, Integer, String, Text, Date, Time, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255), nullable=False)

    interaction_type = Column(String(100), nullable=False)

    interaction_date = Column(Date)

    interaction_time = Column(Time)

    attendees = Column(Text)

    topics_discussed = Column(Text)

    materials_shared = Column(Text)

    sentiment = Column(String(50))

    outcomes = Column(Text)

    follow_up_actions = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )