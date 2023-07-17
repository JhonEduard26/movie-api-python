from fastapi import APIRouter, HTTPException
from config.database import Session, engine, select
from uuid import UUID

from models.movie import Movie
from services.movie import MovieService


router = APIRouter(
    prefix='/movies',
    tags=['movies']
)


@router.get('/')
async def get_movies():
    movies = await MovieService().get_movies()
    return movies


@router.get('/{id_movie}')
async def get_movie_by_id(id_movie: UUID):
    movie = await MovieService().get_movie_by_id(id_movie)
    return movie


@router.get('/')
async def get_movies_by_category(category: str):
    movies = await MovieService().get_movies_by_category(category)
    return movies


@router.post('/')
async def create_movie(movie: Movie):
    result = await MovieService().create_movie(movie)
    return result


@router.put('/{id_movie}')
async def update_movie(id_movie: UUID, movie: Movie):
    movie_found = await MovieService().update_movie(id_movie, movie)
    return movie_found


@router.delete('/{id_movie}')
async def delete_movie(id_movie: UUID):
    result = await MovieService().delete_movie(id_movie)
    return result
