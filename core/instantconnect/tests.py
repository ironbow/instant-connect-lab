import pytest


def test_home_page(client, db):
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    assert b"Instant Connect Lab" in response.content
