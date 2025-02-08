from pydantic import BaseModel

class URLRequest(BaseModel):
    url: str

# User Authentication Schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# URL Request Schema
class URLRequest(BaseModel):
    url: str