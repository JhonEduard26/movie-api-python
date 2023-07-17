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
    with Session(engine) as session:
        statement = select(Movie)
        results = session.exec(statement)
        movies = [movie for movie in results]

    return movies


@app.get('/movies/{id_movie}', tags=['movies'], response_model=Movie)
async def get_movie_by_id(id_movie: UUID):
    with Session(engine) as session:
        movie = session.get(Movie, id_movie)
        if not movie:
            raise HTTPException(404, 'Movie not found')
    return movie


@app.get('/movies/', tags=['movies'], response_model=List[Movie])
async def get_movies_by_category(category: str):
    with Session(engine) as session:
        statement = select(Movie).where(Movie.category == category)
        movies = session.exec(statement).all()

    return movies


@app.post('/movies', tags=['movies'])
async def create_movie(movie: Movie):
    new_movie = Movie(**movie.dict())
    with Session(engine) as session:
        session.add(new_movie)
        session.commit()

    return new_movie


@app.put('/movies/{id_movie}', tags=['movies'])
async def update_movie(id_movie: UUID, movie: Movie):
    with Session(engine) as session:
        statement = select(Movie).where(Movie.id == id_movie)
        results = session.exec(statement)
        movie_found = results.one()

        movie_found.category = movie.category
        movie_found.title = movie.title
        movie_found.title = movie.title
        movie_found.year = movie.year
        movie_found.overview = movie.overview
        movie_found.rating = movie.rating

        session.add(movie_found)
        session.commit()
        session.refresh(movie_found)

    return movie_found


@app.delete('/movies/{id_movie}', tags=['movies'])
async def delete_movie(id_movie: UUID):
    with Session(engine) as session:
        movie = session.get(Movie, id_movie)
        if not movie:
            raise HTTPException(404, 'Movie not found')

        session.delete(movie)
        session.commit()

    return {
        'message': 'Movie deleted'
    }
