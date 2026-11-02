import json

import jwt
from cryptography.fernet import Fernet


def sign_token(client_id, secret):
    return jwt.encode({"sub": client_id}, secret, algorithm="HS256")


def client_for(token, secret):
    return jwt.decode(token, secret, algorithms=["HS256"])["sub"]


def seal_cursor(cursor, key):
    return Fernet(key).encrypt(json.dumps(cursor).encode()).decode()


def open_cursor(sealed, key):
    return json.loads(Fernet(key).decrypt(sealed.encode()))
