from os import getenv
from fastapi import APIRouter, HTTPException

from models.user import User
from jwt_utils.jwt_manager import generate_token


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/login')
async def login(user: User):
    if user.email == getenv('EMAIL') and user.password == getenv('PASS'):
        token = generate_token(user.dict())
        return token
    else:
        raise HTTPException(401, 'Unauthorized')