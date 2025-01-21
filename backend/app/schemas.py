from pydantic import BaseModel
from typing import List, Optional

# User schemas
class UserBase(BaseModel):
    name: str
    location: Optional[str] = None
    email: str
    preferences: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Job schemas
class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        from_attributes = True

# Skill schemas
class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int

    class Config:
        from_attributes = True
