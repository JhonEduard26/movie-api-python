from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(min_length=1, max_length=40)
    overview: str = Field(min_length=1, max_length=120)
    year: int = Field(gt=1900)
    rating: float = Field(gt=0.0, le=10.0)
    category: str = Field(min_length=1, max_length=40)
