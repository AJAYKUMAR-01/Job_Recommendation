from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

#signup a new user
def signup_user(user: schemas.AuthBase, db: Session):
    db_user = models.Auth(
        name = user.name,
        email = user.email,
        password = user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(user: schemas.LoginBase, db: Session):
    return db.query(models.Auth).filter(models.Auth.email == user.email and models.Auth.password == user.password).first()

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

def get_recommendations(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    # Get the user
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return []

    # Get the user's skills
    user_skills = {skill.name for skill in user.skills}

    # Fetch jobs that match the user's skills
    jobs = db.query(models.Job).all()
    recommended_jobs = []
    for job in jobs:
        job_skills = {skill.name for skill in job.skills}
        # Calculate match score based on overlapping skills
        match_score = len(user_skills.intersection(job_skills))
        if match_score > 0:  # Only recommend jobs with skill matches
            recommended_jobs.append((job, match_score))

    # Sort jobs by match score in descending order
    recommended_jobs.sort(key=lambda x: x[1], reverse=True)

    # Limit the number of recommendations
    return [job[0] for job in recommended_jobs[skip:skip + limit]]

def search_jobs(db: Session, location: Optional[str] = None, industry: Optional[str] = None, skill: Optional[str] = None):
    query = db.query(models.Job)
    
    # Filter by location
    if location:
        query = query.filter(models.Job.location.ilike(f"%{location}%"))
    
    # Filter by industry
    if industry:
        query = query.filter(models.Job.industry.ilike(f"%{industry}%"))
    
    # Filter by skill
    if skill:
        query = query.join(models.Job.skills).filter(models.Skill.name.ilike(f"%{skill}%"))
    
    return query.all()
