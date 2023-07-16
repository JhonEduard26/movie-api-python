from os import getenv
from fastapi import FastAPI, HTTPException
from uuid import UUID
from dotenv import load_dotenv
from typing import List
from config.database import engine, SQLModel, Session, select

from models.movie import Movie
from models.user import User
from jwt_utils.jwt_manager import generate_token

SQLModel.metadata.create_all(engine)

app = FastAPI()
app.title = 'FastAPI movie API'
load_dotenv()


@app.get('/', tags=['home'])
async def root():
    return {'message': 'Hello World'}


@app.post('/auth/login', tags=['auth'])
async def login(user: User):
    if user.email == getenv('EMAIL') and user.password == getenv('PASS'):
        token = generate_token(user.model_dump())
        return {
            'token': token
        }
    else:
        raise HTTPException(401, 'Unauthorized')


@app.get('/movies', tags=['movies'], response_model=List[Movie])
async def get_movies():
    movies = []
    with Session(engine) as session:
        statement = select(Movie)
        results = session.exec(statement)
        for movie in results:
            movies.append(movie)

    return movies


@app.get('/movies/{id_movie}', tags=['movies'], response_model=Movie)
async def get_movie_by_id(id_movie: UUID):
    movie = list(filter(lambda item: item['id'] == id_movie, []))
    return {
        'ok': True,
        'movie': movie
    }


@app.get('/movies/', tags=['movies'], response_model=List[Movie])
async def get_movies_by_category(category: str):
    movies_filtered = list(filter(lambda item: item['category'] == category, []))
    return {
        'ok': True,
        'movies': movies_filtered,
    }


@app.post('/movies', tags=['movies'])
async def create_movie(movie: Movie):
    new_movie = Movie(**movie.dict())
    with Session(engine) as session:
        session.add(new_movie)
        session.commit()

    return new_movie


@app.put('/movies/{id_movie}', tags=['movies'])
async def update_movie(id_movie: UUID, movie: Movie):
    for index, item in enumerate([]):
        if item['id'] == id_movie:
            [][index].update(movie)
            return [][index]

    raise HTTPException(404, 'Movie not found')


@app.delete('/movies/{id_movie}', tags=['movies'])
async def delete_movie(id_movie: UUID):
    movie_find = list(filter(lambda item: item['id'] == id_movie, []))

    if len(movie_find) == 0:
        raise HTTPException(404, 'Movie not found')

    [].remove(movie_find[0])
    return movie_find
