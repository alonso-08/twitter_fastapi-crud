#Python
from datetime import date, datetime
from typing import Optional
from uuid import UUID
import uuid

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
        min_length=8,
        max_length=64
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
    tweet_id: uuid = Field(...)
    content: str = Field(
        ...,
        min_length=1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

@app.get("/")
def home():
    return {"mensaje":"Funcionando"}