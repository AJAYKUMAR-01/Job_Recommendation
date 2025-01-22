from passlib.context import CryptContext  # For hashing passwords
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Password hashing context

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
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String)
    location = Column(String)
    skills = relationship("Skill", secondary=user_skills, back_populates="users")

    # Hash password
    def set_password(self, password: str):
        self.password = pwd_context.hash(password)

    # Verify password
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    jobs = relationship("Job", secondary=job_skills, back_populates="skills")
    users = relationship("User", secondary=user_skills, back_populates="skills")


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    industry = Column(String)
    location = Column(String)
    skills = relationship("Skill", secondary=job_skills, back_populates="jobs")
