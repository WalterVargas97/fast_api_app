from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from schemas.movie_direction import MovieDirection
from config.database import Session
from service.movie_direction import MovieDirectionService
from models.movie_direction import Movie_direction as MovieDirectionModel

movie_direction_router = APIRouter()

@movie_direction_router.get('/movie/{id_movie}/direction/', tags=['cast'], response_model=list[MovieDirection], status_code=200)
def get_movie_direction(id_movie:int = Path(ge=1,le=2000)):
    db=Session()
    result = MovieDirectionService(db).get_movie_direction(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro", "status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_direction_router.post('/direction', tags=['cast'], response_model=dict, status_code=201)
def create_direction(direction:MovieDirection)-> dict:
    db = Session()
    MovieDirectionService(db).create_movie_direction(direction)
    return JSONResponse(content={"message":"se ha registrado el actor","status_code":201})