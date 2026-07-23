from pydantic import BaseModel, Field


class SessionCreate(BaseModel):
    session_id: str = Field(min_length=1)
    user_id: str | None = None


class SessionRecord(SessionCreate):
    turn_count: int
    last_transcript: str | None = None


class ConversationInput(BaseModel):
    session_id: str = Field(min_length=1)
    transcript: str = Field(min_length=1)


class ConversationTurn(BaseModel):
    speaker: str
    content: str


class ConversationResponse(BaseModel):
    session_id: str
    assistant_message: str
    transcript: str
    turns: list[ConversationTurn]