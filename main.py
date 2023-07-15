import this

from fastapi import FastAPI, HTTPException
from uuid import uuid4
from data.movies import movies
from models.movie import MovieCreate, MovieUpdate


app = FastAPI()
app.title = 'FastAPI movie API'


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
async def create_movie(movie: MovieCreate):
    new_movie = {
        'id': uuid4(),
        **movie.model_dump()
    }
    movies.append(new_movie)
    return new_movie


@app.put('/movies/{id_movie}', tags=['movies'])
async def update_movie(id_movie: str, movie: MovieUpdate):
    for index, item in enumerate(movies):
        if str(item['id']) == id_movie:
            movies[index].update(movie)
            return movies[index]

    raise HTTPException(404, 'Movie not found')


@app.delete('/movies/{id_movie}', tags=['movies'])
async def delete_movie(id_movie: str):
    movie_find = list(filter(lambda item: str(item['id']) == id_movie, movies))

    if len(movie_find) == 0:
        raise HTTPException(404, 'Movie not found')

    movies.remove(movie_find[0])
    return movie_find
