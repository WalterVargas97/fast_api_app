from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from models.moviegenres import Movie_genres

from config.database import Session
from schemas.movie_genres import Movie_genres
from service.movie_genres import MovieGenresService

movie_genres_router = APIRouter()


