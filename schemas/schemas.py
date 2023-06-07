from typing import List, Union
from enum import Enum
from pydantic import BaseModel, validator

class Response(BaseModel):
    info: str

class TaskImportance(str, Enum):
    very_urgent = "very urgent"
    urgent = "urgent"
    wait = "can wait"
    non_emergent = "not urgent"


class TaskCreate(BaseModel):
    owner_id: int
    title: str
    importance: TaskImportance
    executor: str
    description: Union[str, None] = None


class Task(BaseModel):
    id: int
    owner_id: int
    title: str
    importance: TaskImportance
    executor: str
    description: Union[str, None] = None


class Credentials(BaseModel):
    email: str
    password: str

    @validator('password')
    def name_length(cls, v):
        if len(v) < 8 or len(v) > 16:
            raise ValueError('length must be between 8 and 16')
        return v


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    password2: str

    @validator('password')
    def name_length(cls, v):
        if len(v) < 8 or len(v) > 16:
            raise ValueError('length must be between 8 and 16')
        return v


class User(BaseModel):
    id: int  # uuid.UUID
    email: str # TODO: EmailStr (install pydantic[email], then "from pydantic import EmailStr")
    username: str
    # tasks: List[Task] = []


class UserRestore(BaseModel):
    email: str
    password: str
    password2: str

    @validator('password')
    def name_length(cls, v):
        if len(v) < 8 or len(v) > 16:
            raise ValueError('length must be between 8 and 16')
        return v


class UserUpdate(BaseModel):
    auth: Credentials
    email: str
