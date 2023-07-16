from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_length=4, max_length=32)
    password: str = Field(min_length=6, max_length=32)
