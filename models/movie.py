from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class Movie(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(unique=True)
    overview: Optional[str] = None
    year: int
    rating: Optional[float] = Field(default=0.0)
    category: str
