#Python
from datetime import date
from typing import Optional
from uuid import UUID

#Pydantic
from pydantic import EmailStr
from pydantic import BaseModel
from pydantic import Field

#FastApi
from fastapi import FastAPI

app=FastAPI()


#Models
class UserBase(BaseModel):
    user_id:UUID
    email: EmailStr = Field(...)

class UserLogin(BaseModel):
    password: str = Field(
        ...,
        min_length=8
    )

class User(UserBase):   
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    birt_date: Optional[date] = Field(default=None)


class Tweet():
    pass

@app.get("/")
def home():
    return {"mensaje":"Funcionando"}