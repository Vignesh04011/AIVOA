from datetime import date, time
from typing import Optional
from typing import Any

from pydantic import BaseModel


class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str

    interaction_date: Optional[date] = None
    interaction_time: Optional[time] = None

    attendees: Optional[str] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None

    sentiment: Optional[str] = None

    outcomes: Optional[str] = None

    follow_up_actions: Optional[str] = None


class InteractionResponse(InteractionCreate):
    id: int
    ai_response: dict[str, Any] | None = None

    class Config:
        from_attributes = True