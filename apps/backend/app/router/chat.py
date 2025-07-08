import json
import logging
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, Body
from openai import OpenAI
from openai.types.responses import ResponseInputParam, ResponseOutputItem

from ..core.config import Settings
from ..models.chat import Chat
from ..tools.tide_times import get_tide_times, tide_times_tool

logger = logging.getLogger("uvicorn.error")

router = APIRouter()
settings = Settings()

client = OpenAI(api_key=settings.openai_api_key)


@router.post("/chat/send")
async def send_chat_message(message: str = Body(..., embed=True)) -> Chat:
    logger.info(f"send_chat_message::message::{message}")
    input_messages: ResponseInputParam = [{"role": "user", "content": message}]

    response = client.responses.create(
        model="gpt-4.1-mini-2025-04-14",
        instructions="You are a lifeguard that wants to keep people safe on the beach.",
        input=input_messages,
        tools=[tide_times_tool],
    )
    print(response.output)

    tool_call: ResponseOutputItem = response.output[0]
    if tool_call.type == "function_call":
        args = json.loads(tool_call.arguments)
        logger.info(f"Tool call: {tool_call.name} with arguments: {args}")

        result = get_tide_times(args["location_name"])

        input_messages.append(tool_call)  # type: ignore
        input_messages.append(
            {
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": str(result),
            }
        )

        response = client.responses.create(
            model="gpt-4.1",
            input=input_messages,
            tools=[tide_times_tool],
        )
        logger.info(f"response_2.output_text::{response.output_text}")

    chat = Chat(
        id=uuid4(),
        message=message,
        response=response.output_text,
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )

    return chat
