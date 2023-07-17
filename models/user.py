from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    password: str = Field(min_length=6, max_length=32)
