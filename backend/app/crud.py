from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from typing import Optional

def create_user(db: Session, user: schemas.UserCreate):
    # Check if email already exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create user
    db_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role,
        location=user.location,
    )
    db_user.set_password(user.password)  # Hash the password
    db.add(db_user)
    db.commit()

    # Link skills to user
    for skill_name in user.skills:
        skill = db.query(models.Skill).filter(models.Skill.name == skill_name).first()
        if not skill:
            skill = models.Skill(name=skill_name)
            db.add(skill)
            db.commit()
            db.refresh(skill)
        db_user.skills.append(skill)  # Associate skill with user
    
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not user.verify_password(password):
        return None
    return user


# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create a new job
def create_job(db: Session, job: schemas.JobCreate):
    # Create the job
    db_job = models.Job(
        title=job.title,
        description=job.description,
        industry=job.industry,
        location=job.location,
    )
    db.add(db_job)
    db.commit()

    # Link skills to the job
    for skill_name in job.skills:
        skill = db.query(models.Skill).filter(models.Skill.name == skill_name).first()
        if not skill:
            skill = models.Skill(name=skill_name)
            db.add(skill)
            db.commit()
            db.refresh(skill)
        db_job.skills.append(skill)  # Associate skill with the job

    db.commit()
    db.refresh(db_job)
    return db_job


# Get all jobs
def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Job).offset(skip).limit(limit).all()

# Get recommendations based on skills
def get_recommendations(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_skills = {skill.name for skill in user.skills}
    jobs = db.query(models.Job).all()
    recommended_jobs = []

    for job in jobs:
        job_skills = {skill.name for skill in job.skills}
        if user_skills & job_skills:  # Check for common skills
            recommended_jobs.append(job)
    print(recommended_jobs)
    return recommended_jobs[skip: skip + limit]
