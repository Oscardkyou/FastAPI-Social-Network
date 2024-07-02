from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    profile_image: Optional[str] = None

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    timestamp: datetime
    owner_id: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    timestamp: datetime
    user_id: int
    post_id: int

    class Config:
        orm_mode = True

class Like(BaseModel):
    user_id: int
    post_id: int

    class Config:
        orm_mode = True

class Notification(BaseModel):
    content: str
    timestamp: datetime
    user_id: int
    post_id: Optional[int] = None

    class Config:
        orm_mode = True
