from django.test import Client


def test_health():
    assert Client().get("/health").json() == {"ok": True}


def test_search():
    body = Client().get("/search", {"q": "runbook"}).json()
    assert body["query"] == "runbook"
    assert [doc["id"] for doc in body["results"]] == [1]
