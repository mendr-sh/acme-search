from cryptography.fernet import Fernet

from search.tokens import client_for, open_cursor, seal_cursor, sign_token


def test_token_round_trip():
    assert client_for(sign_token("reports", "s3cret"), "s3cret") == "reports"


def test_cursor_round_trip():
    key = Fernet.generate_key()
    assert open_cursor(seal_cursor({"after": 20}, key), key) == {"after": 20}
