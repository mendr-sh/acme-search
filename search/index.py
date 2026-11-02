# The documents the API searches. A real deployment loads them from the
# catalog service at start-up.
DOCUMENTS = [
    {"id": 1, "title": "Billing API runbook"},
    {"id": 2, "title": "Status page incident checklist"},
    {"id": 3, "title": "Search API on-call guide"},
]


def find(query):
    words = query.lower().split()
    return [doc for doc in DOCUMENTS if all(w in doc["title"].lower() for w in words)]
