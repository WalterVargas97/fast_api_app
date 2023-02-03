from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):
    id: Optional[int] = None
    fname: str = Field(max_length=30,min_length=2)
    lname: str = Field(max_length=30,min_length=2)
    
    
    class Config:
        schema_extra = {
            "example":{
                "fname": "omar",
                "lname": "Don"
            }
        }