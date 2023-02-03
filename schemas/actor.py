from typing import Optional
from pydantic import BaseModel, Field


class Actor(BaseModel):
        id: Optional[int] = None
        fname: str = Field(max_length=15,min_length=3)
        lname: str = Field(max_length=15,min_length=3)
        gender: str = Field(max_length=15,min_length=1)

        class Config:
            schema_extra = {
                "example":{
                    "fname": "Vin",
                    "lname":"Diesel",
                    "gender":"M"
                }
            }
