from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from .database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    username = Column(String, unique=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    profile_image = Column(String, nullable=True)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    owner = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")

class Like(Base):
    __tablename__ = "likes"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    owner = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, nullable=True)
    user = relationship("User", back_populates="notifications")
