from sqlalchemy.orm import Session
from . import models, schemas

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        location=user.location,
        email=user.email,
        preferences=user.preferences,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Update user preferences
def update_user_preferences(db: Session, user_id: int, preferences: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.preferences = preferences
        db.commit()
        db.refresh(user)
    return user

# Delete a user
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


# Create a new job
def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        title=job.title,
        description=job.description,
        industry=job.industry,
        location=job.location,
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# Get a job by ID
def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

# Get all jobs
def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Job).offset(skip).limit(limit).all()

# Delete a job
def delete_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
    return job



# Create a new skill
def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(name=skill.name)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

# Get all skills
def get_skills(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Skill).offset(skip).limit(limit).all()
