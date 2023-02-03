from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.director import Director
from config.database import Session
from service.director import DirectorService

director_router = APIRouter()

@director_router.get('/directors',tags=['directors'], response_model = Director, status_code=200)
def get_director() -> Director:
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.post('/directors', tags=['directors'], status_code=201, response_model=dict)
def create_director(director:Director) ->dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'message':'director save in data base'})