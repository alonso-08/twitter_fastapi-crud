#Python
from datetime import date, datetime
from encodings import utf_8
from turtle import title
from typing import Optional, List
from unittest import result
from uuid import UUID
import uuid
import json

#Pydantic
from pydantic import EmailStr
from pydantic import BaseModel
from pydantic import Field

#FastApi
from fastapi import Body, FastAPI
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
    birth_date: Optional[date] = Field(default=None)

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
    updated_at: Optional[datetime] = Field(default=None)
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
def signup(user: UserRegister = Body(...)):
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
    - birth_date: datetime

    """
    with open("users.json","r+",encoding="utf_8") as file:
        contenido_archivo=json.loads(file.read()) 
        user_dict=user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        contenido_archivo.append(user_dict)
        file.seek(0)
        file.write(json.dumps(contenido_archivo))
        print( user_dict["birth_date"])
        return user

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
    """
    This path operations shows all users in the app
    Parameters:
    -

    Returns a json list with all users in the app, with the following keys:

    - user_id: UUID
    - email: EmailStr
    - first_name. str
    - last_name: str
    - birth_date: datetime
    """
    with open("users.json","r",encoding="utf-8") as file:
        results=json.loads(file.read())
        return results
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
    """
    This path operations shows all tweets in the app
    Parameters:
    -

    Returns a json list with all tweets in the app, with the following keys:

    - tweet_id: UUID
    - created_at: datetime 
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r",encoding="utf-8") as file:
        results=json.loads(file.read())
        return results

### Post a Tweet
@app.post(
    path="/post/"
    , response_model=Tweet
    , status_code=status.HTTP_201_CREATED
    , summary="Post a Tweet"
    , tags=["Tweets"]

)
def post(tweet : Tweet = Body(...)):
    """
    Crear tweet
    
    This path operations register a Tweet in the app
    
    Parameters:
    - Request body parametes
        - User: Tweet
    Returns a json with  the basic user information:
    - tweet_id: UUID
    - created_at: datetime 
    - updated_at: Optional[datetime]
    - by: User

    """
    with open("tweets.json","r+",encoding="utf_8") as file:
        contenido_archivo=json.loads(file.read()) 
        tweet_dict=tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        contenido_archivo.append(tweet_dict)
        file.seek(0)
        file.write(json.dumps(contenido_archivo))       
        return tweet


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