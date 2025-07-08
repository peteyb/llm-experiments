from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, Body
from openai import OpenAI

from ..core.config import Settings
from ..models.chat import Chat

router = APIRouter()
settings = Settings()

client = OpenAI(api_key=settings.openai_api_key)


@router.post("/chat/send")
async def send_chat_message(message: str = Body(..., embed=True)) -> Chat:
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a lifeguard that wants to keep people safe on the beach.",
        input=message,
    )

    chat = Chat(
        id=uuid4(),
        message=message,
        response=response.output_text,
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    return chat
