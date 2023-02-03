from fastapi import APIRouter, Path
from fastapi.responses import  JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

from schemas.director import Director
from config.database import Session
from service.director import DirectorService
from models.director import Director as DirectorModel

director_router = APIRouter()

@director_router.get('/director',tags=['director'], response_model = List[Director], status_code=200)
def get_directors() -> Director: 
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.get('/director/{id}', tags=['director'], response_model= Director , status_code=200)
def get_directors_by_id(id:int = Path(ge=1,le=2000)):   
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(status_code=400,content={"message":"No found director with that ID"})
    return  JSONResponse(content=jsonable_encoder(result), status_code=200)
    
    
#def get_directors_by_fname(fname:str = Query(min_lenght=5, max_length=50 ))

@director_router.post('/director', tags=['director'], status_code=201, response_model=dict)
def create_director(director:Director) ->dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'message':'director save in data base'})