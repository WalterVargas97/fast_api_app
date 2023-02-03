from typing import Optional
from pydantic import BaseModel, Field

class MovieDirection(BaseModel):
    director_id: int 
    movie_id : int
    
    
    class Config:
        schema_extra = {
            "example":{
                "director_id": 1,
                "movie_id": 1,
            }
        }