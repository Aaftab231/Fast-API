from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title: Optional[str]
    body: Optional[str]

class Blog(BlogBase):
    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    class Config:
        orm_mode = True
    
    username: str
    email: str
    blogs: List[Blog] = []

class ShowBlog(BaseModel):
    class Config:
        orm_mode = True
    
    title: Optional[str]
    body: Optional[str]
    creator: ShowUser

class Login(BaseModel):
    username: str
    password: str