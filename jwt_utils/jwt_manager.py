from os import getenv
from jwt import encode, decode


def generate_token(data: dict):
    token = encode(payload=data, key=getenv('JWT_SECRET'), algorithm='HS256')
    return token


def validate_token(token: str):
    data = decode(token, getenv('JWT_SECRET'))
    return data
