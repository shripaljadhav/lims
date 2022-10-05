import email
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    bio:str
    email:str
    password:str
    companyname:str
    website:str
    address:str
    country:str
    state:str
    city:str
    zipcode:str

class ShowUser(BaseModel):
    id:int
    firstname: str
    lastname: str
    bio:str
    email:str
    password:str
    companyname:str
    website:str
    address:str
    country:str
    state:str
    city:str
    zipcode:str
    class Config():
        orm_mode = True



class Login(BaseModel):
    email: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
