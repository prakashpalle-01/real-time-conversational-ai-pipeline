# Real-Time Conversational AI Pipeline

A FastAPI service for real-time conversational sessions. The project simulates a streaming voice pipeline with session state, transcript handling, response generation, and room for speech-to-text, LLM, and text-to-speech adapters.

## What it does

- Accepts streaming audio or text messages over WebSocket
- Maintains per-session conversation state
- Produces assistant responses and transcript summaries
- Exposes a health endpoint and session lookup endpoint
- Ships with smoke tests and container-ready packaging

## API

- `GET /health` - service readiness
- `POST /sessions` - create a conversation session
- `GET /sessions/{session_id}` - inspect session state
- `WS /ws/conversation` - stream conversation turns

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[test]
uvicorn src.main:app --reload
```
