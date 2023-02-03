from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):
    id: Optional[int] = None
    fname: str = Field(max_length=15,min_length=3)
    lname: str = Field(max_length=15,min_length=3)
    
    
    class Config:
        schema_extra = {
            "example":{
                "fname": "omar",
                "lname": "Don"
            }
        }