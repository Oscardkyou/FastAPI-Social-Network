from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from . import models, schemas, crud, security
from .database import SessionLocal, engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = security.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(security.get_current_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)

@app.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(security.get_current_user)):
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id, post_id=post_id)

@app.get("/posts/{post_id}/comments/", response_model=List[schemas.Comment])
def read_comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_post(db, post_id=post_id)

@app.post("/posts/{post_id}/like/")
def like_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(security.get_current_user)):
    return crud.like_post(db=db, post_id=post_id, user_id=current_user.id)

@app.post("/posts/{post_id}/unlike/")
def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(security.get_current_user)):
    return crud.unlike_post(db=db, post_id=post_id, user_id=current_user.id)
