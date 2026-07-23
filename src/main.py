from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect

from src.models import ConversationInput, ConversationResponse, SessionCreate
from src.store import ConversationStore

app = FastAPI(title="Real-Time Conversational AI Pipeline")
store = ConversationStore()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/sessions")
def create_session(payload: SessionCreate):
    return store.create_session(payload)


@app.get("/sessions/{session_id}", responses={404: {"description": "Session not found"}})
def get_session(session_id: str):
    session = store.get_session(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@app.post("/conversation")
def post_conversation(payload: ConversationInput) -> ConversationResponse:
    return store.handle_turn(payload.session_id, payload.transcript)


@app.websocket("/ws/conversation")
async def conversation_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        while True:
            payload = await websocket.receive_text()
            response = store.handle_turn("live-session", payload)
            await websocket.send_json(response.model_dump())
    except WebSocketDisconnect:
        return
