from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.interaction_service import process_interaction

from app.database.database import get_db
from app.database.crud import create_interaction
from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
)

router = APIRouter()


@router.post(
    "/interactions",
    response_model=InteractionResponse,
)
def create_hcp_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):

    saved = create_interaction(db, interaction)

    ai_response = process_interaction(
        interaction.model_dump()
    )

    return {
        **saved.__dict__,
        "ai_response": ai_response,
    }