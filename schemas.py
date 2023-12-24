from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


# User
class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    idea_id: Optional[int] = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


# Direction
class DirectionBase(BaseModel):
    name: str


class DirectionCreate(DirectionBase):
    pass


class DirectionUpdate(DirectionBase):
    name: Optional[str] = None


class Direction(DirectionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


# Idea
class IdeaBase(BaseModel):
    name: str
    direction_id: int


class IdeaCreate(IdeaBase):
    pass


class IdeaUpdate(IdeaBase):
    name: Optional[str] = None
    direction_id: Optional[int] = None


class Idea(IdeaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
