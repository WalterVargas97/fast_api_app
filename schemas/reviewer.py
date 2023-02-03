from typing import Optional
from pydantic import BaseModel, Field

class Reviewer(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=30,min_length=3)
    
    class Config:
        schema_extra = {
            "example":{
                "name":"vin"
            }
        }