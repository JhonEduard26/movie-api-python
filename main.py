from fastapi import FastAPI
from uuid import uuid4

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
    movie = [item for item in movies if str(item['id']) == id_movie]
    return {
        'ok': True,
        'movie': movie
    }
