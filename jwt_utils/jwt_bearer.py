from os import getenv
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from jwt_utils.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)

        if data['email'] != getenv('EMAIL'):
            raise HTTPException(403, 'Invalid credentials')
