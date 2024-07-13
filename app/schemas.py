from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    username: str
    profile_image: Optional[str]

class UserCreate(schemas.BaseUserCreate):
    username: str
    profile_image: Optional[str]

class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    profile_image: Optional[str]

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
