from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from typing import List
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup/")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = crud.authenticate_user(db, email=user.email, password=user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"id": authenticated_user.id, "name": authenticated_user.name, "email": authenticated_user.email}


@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/jobs/")
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)
# 


@app.get("/jobs/", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recommendations(db=db, user_id=user_id, skip=skip, limit=limit)

# , response_model=List[schemas.JobBase]
