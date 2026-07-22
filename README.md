# Real-Time Conversational AI Pipeline

A production-oriented scaffold for a streaming conversational AI system that can ingest live audio, run speech-to-text, orchestrate LLM responses, and emit text or speech back to the client.

## What is included

- FastAPI app entrypoint
- WebSocket endpoint for streaming sessions
- Health check endpoint
- Test scaffold
- Dockerfile for containerized deployment
- Packaging metadata for a Python service

## Intended architecture

- Client streams audio over WebSocket
- Speech is transcribed with Whisper or a compatible STT backend
- A conversation orchestrator manages context, safety checks, and response generation
- Responses are returned as text and optionally synthesized to speech
- Kafka or another streaming bus can be added later for event fanout and buffering

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn src.main:app --reload
```

## Next steps

- Add a real Whisper adapter
- Add an LLM provider adapter
- Add TTS output support
- Add streaming persistence and observability
