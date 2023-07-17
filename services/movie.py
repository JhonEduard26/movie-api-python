from fastapi import HTTPException
from uuid import UUID

from config.database import Session, engine, select
from models.movie import Movie


class MovieService:
    async def get_movies(self):
        with Session(engine) as session:
            statement = select(Movie)
            results = session.exec(statement)
            movies = [movie for movie in results]
        return movies

    async def get_movie_by_id(self, id_movie: UUID):
        with Session(engine) as session:
            movie = session.get(Movie, id_movie)
            if not movie:
                raise HTTPException(404, 'Movie not found')

        return movie

    async def get_movies_by_category(self, category: str):
        with Session(engine) as session:
            statement = select(Movie).where(Movie.category == category)
            movies = session.exec(statement).all()
        return movies

    async def create_movie(self, movie: Movie):
        new_movie = Movie(**movie.dict())
        with Session(engine) as session:
            session.add(new_movie)
            session.commit()
        return {
            'message': 'created'
        }

    async def update_movie(self, id_movie: UUID, movie: Movie):
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

    async def delete_movie(self, id_movie: UUID):
        with Session(engine) as session:
            movie = session.get(Movie, id_movie)
            if not movie:
                raise HTTPException(404, 'Movie not found')

            session.delete(movie)
            session.commit()
        return {
            'message': 'deleted'
        }
