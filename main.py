from fastapi import FastAPI
from uuid import uuid4
from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str


app = FastAPI()
app.title = 'FastAPI movie API'


movies = [
    {
        'id': uuid4(),
        'title': 'Avatar',
        'overview': 'lorem lorem lorem',
        'year': '2009',
        'rating': 7.8,
        'category': 'Action'
    },
    {
        'id': uuid4(),
        'title': 'Scream',
        'overview': 'lorem lorem lorem',
        'year': '2004',
        'rating': 8,
        'category': 'Thriller'
    },
    {
        'id': uuid4(),
        'title': 'Scream 2',
        'overview': 'lorem lorem lorem',
        'year': '2007',
        'rating': 7,
        'category': 'Thriller'
    }
]


@app.get('/', tags=['home'])
async def root():
    return {'message': 'Hello World'}


@app.get('/movies', tags=['movies'])
async def get_movies():
    return movies


@app.get('/movies/{id_movie}', tags=['movies'])
async def get_movie_by_id(id_movie: str):
    movie = list(filter(lambda item: str(item['id']) == id_movie, movies))
    return {
        'ok': True,
        'movie': movie
    }


@app.get('/movies/', tags=['movies'])
async def get_movies_by_category(category: str):
    movies_filtered = list(filter(lambda item: item['category'] == category, movies))
    return {
        'ok': True,
        'movies': movies_filtered,
    }


@app.post('/movies', tags=['movies'])
async def create_movie(movie: Movie):
    new_movie = {
        'id': uuid4(),
        **movie.model_dump()
    }
    movies.append(new_movie)
    return new_movie
