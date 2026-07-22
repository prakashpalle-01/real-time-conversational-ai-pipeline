from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Real-Time Conversational AI Pipeline")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.websocket("/ws/conversation")
async def conversation_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        while True:
            payload = await websocket.receive_text()
            response = {
                "event": "response",
                "transcript": payload,
                "message": "Pipeline scaffold received input",
            }
            await websocket.send_json(response)
    except WebSocketDisconnect:
        return
