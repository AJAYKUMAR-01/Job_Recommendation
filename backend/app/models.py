from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association tables
user_skills = Table(
    "user_skills", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("skill_id", Integer, ForeignKey("skills.id"))
)

job_skills = Table(
    "job_skills", Base.metadata,
    Column("job_id", Integer, ForeignKey("jobs.id")),
    Column("skill_id", Integer, ForeignKey("skills.id"))
)

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    email = Column(String, unique=True, nullable=False)
    preferences = Column(String)
    skills = relationship("Skill", secondary=user_skills, back_populates="users")


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    users = relationship("User", secondary=user_skills, back_populates="skills")
    jobs = relationship("Job", secondary=job_skills, back_populates="skills")


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    industry = Column(String)
    location = Column(String)
    skills = relationship("Skill", secondary=job_skills, back_populates="jobs")
