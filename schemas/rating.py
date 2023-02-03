from typing import Optional
from pydantic import BaseModel, Field

class Rating(BaseModel):
    movie_id: int
    reviewer_id: int
    reviewer_stars: int
    num_o_ratings: int
    
    
    class Config:
        schema_extra = {
            "example":{
                "movie_id":1,
                "reviewer_id": 1,
                "reviewer_stars":1,
                "num_o_ratings":1,
            }
        }