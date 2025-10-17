from typing import Any

from app.server.http_server import app


test_client = app.test_client()


test_sentences = [
    "Autonomous cars shift insurance liability toward manufacturers",
    "Apple is looking at buying U.K. startup for $1 billion",
    "Credit and mortgage account holders must submit their requests",
    "San Francisco considers banning sidewalk delivery robots",
]


def test_handle_batch_analyze() -> None:
    payload: dict[str, Any] = {
        "sentences": test_sentences,
    }

    response = test_client.post(
        "/v1/nlp/english/batch",
        headers={"Content-Type": "application/json"},
        json=payload,
    )

    print(response.json)
    assert response.status_code == 200
