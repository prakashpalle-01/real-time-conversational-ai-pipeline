from fastapi.testclient import TestClient

from src.main import app


def test_health_check() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_session_and_conversation_flow() -> None:
    client = TestClient(app)
    session_response = client.post("/sessions", json={"session_id": "session-001", "user_id": "user-1"})
    assert session_response.status_code == 200
    assert session_response.json()["session_id"] == "session-001"

    turn_response = client.post("/conversation", json={"session_id": "session-001", "transcript": "hello there"})
    assert turn_response.status_code == 200
    payload = turn_response.json()
    assert payload["session_id"] == "session-001"
    assert payload["turns"][0]["speaker"] == "user"
