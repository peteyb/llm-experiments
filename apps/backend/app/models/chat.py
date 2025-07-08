from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Chat(BaseModel):
    id: UUID
    message: str
    response: str
    created_at: datetime
    updated_at: datetime
