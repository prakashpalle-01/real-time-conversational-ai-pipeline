from src.models import ConversationResponse, ConversationTurn, SessionCreate, SessionRecord


class ConversationStore:
    def __init__(self) -> None:
        self._sessions: dict[str, dict[str, str | int | None]] = {}

    def create_session(self, payload: SessionCreate) -> SessionRecord:
        self._sessions[payload.session_id] = {"user_id": payload.user_id, "turn_count": 0, "last_transcript": None}
        return SessionRecord(**payload.model_dump(), turn_count=0, last_transcript=None)

    def get_session(self, session_id: str) -> SessionRecord | None:
        session = self._sessions.get(session_id)
        if session is None:
            return None
        return SessionRecord(
            session_id=session_id,
            user_id=session.get("user_id") if isinstance(session.get("user_id"), str) else None,
            turn_count=int(session.get("turn_count", 0)),
            last_transcript=session.get("last_transcript") if isinstance(session.get("last_transcript"), str) else None,
        )

    def handle_turn(self, session_id: str, transcript: str) -> ConversationResponse:
        session = self._sessions.setdefault(session_id, {"user_id": None, "turn_count": 0, "last_transcript": None})
        turn_count = int(session.get("turn_count", 0)) + 1
        session["turn_count"] = turn_count
        session["last_transcript"] = transcript
        assistant_message = f"Received turn {turn_count}: {transcript}"
        turns = [
            ConversationTurn(speaker="user", content=transcript),
            ConversationTurn(speaker="assistant", content=assistant_message),
        ]
        return ConversationResponse(session_id=session_id, assistant_message=assistant_message, transcript=transcript, turns=turns)