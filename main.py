#Python
from datetime import date, datetime
from turtle import title
from typing import Optional, List
from uuid import UUID
import uuid

#Pydantic
from pydantic import EmailStr
from pydantic import BaseModel
from pydantic import Field

#FastApi
from fastapi import FastAPI
from fastapi import status
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

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


# Path Operations



## Users
### Register a User
@app.post(
    path="/signup/"
    , response_model=User
    , status_code=status.HTTP_201_CREATED
    , summary="Register a User"
    , tags=["Users"]

)
def signup():
    """
    Signup
    
    This path operations register a user in the app
    
    Parameters:
    - Request body parametes
        - User: UserRegister
    Returns a json with  the basic user information:
    - user_id: UUID
    - email: EmailStr
    - first_name. str
    - last_name: str
    - birth_date: str

    """
### Login a User
@app.post(
    path="/login/"
    , response_model=User
    , status_code=status.HTTP_200_OK
    , summary="Login a User"
    , tags=["Users"]

)
def login():
    pass
### Show all Users
@app.get(
    path="/users/"
    , response_model=List[User]
    , status_code=status.HTTP_201_CREATED
    , summary="Show all Users"
    , tags=["Users"]

)
def show_all_users():
    pass
### Show a User
@app.get(
    path="/users/{user_id}"
    , response_model=User
    , status_code=status.HTTP_200_OK
    , summary="Show a User"
    , tags=["Users"]

)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete"
    , response_model=User
    , status_code=status.HTTP_200_OK
    , summary="Delete a User"
    , tags=["Users"]

)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update"
    , response_model=User
    , status_code=status.HTTP_200_OK
    , summary="Update a User"
    , tags=["Users"]

)
def update_a_user():
    pass

## Tweets
### Show all Tweets
@app.get(
     path="/"
    , response_model=List[Tweet]
    , status_code=status.HTTP_200_OK
    , summary="Show all Tweets"
    , tags=["Tweets"]
)
def home():
    return {"Twitter API":"Funcionando"}

### Post a User
@app.post(
    path="/post/"
    , response_model=Tweet
    , status_code=status.HTTP_201_CREATED
    , summary="Post a Tweet"
    , tags=["Tweets"]

)
def post():
    pass

### Show a Tweet
@app.get(
    path="/tweets/{tweet_id}"
    , response_model=Tweet
    , status_code=status.HTTP_200_OK
    , summary="Show a Tweet"
    , tags=["Tweets"]

)
def show_a_tweet():
    pass

### Delete a Tweet
@app.delete(
     path="/tweets/{tweet_id}/delete"
    , response_model=Tweet
    , status_code=status.HTTP_200_OK
    , summary="Delete a Tweet"
    , tags=["Tweets"]

)
def delete_a_tweet():
    pass

### Update a Tweet
@app.put(
     path="/tweets/{tweet_id}/update"
    , response_model=Tweet
    , status_code=status.HTTP_200_OK
    , summary="Update a Tweet"
    , tags=["Tweets"]

)
def update_a_tweet():
    pass