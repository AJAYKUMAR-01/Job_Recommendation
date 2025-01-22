from pydantic import BaseModel
from typing import Optional, List

# Base User schema
class UserBase(BaseModel):
    name: str
    email: str
    role: str
    location: str

class UserCreate(UserBase):
    password: str
    skills: List[str]  # List of skill names for the user

# Schema for login
class UserLogin(BaseModel):
    email: str
    password: str

# Response schema
class User(UserBase):
    id: int
    skills: List[str]  # This will be a list of skill names in the response

    class Config:
        orm_mode = True

# Job schemas
class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    skills: List[str] = []  # List of skill names for the job


class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True


# Skill schemas
class SkillBase(BaseModel):
    name: str
    class Config:
        orm_mode = True

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int

    class Config:
        orm_mode = True
