from typing import List, Union
from enum import Enum
from pydantic import BaseModel, validator

    
class ProjectImportance(str, Enum):
    very_urgent = "very urgent"
    urgent = "urgent"
    wait = "can wait"
    non_emergent = "not urgent"


class ProjectCreate(BaseModel):
    owner_id: int
    title: str
    importance: ProjectImportance
    executor: str
    description: Union[str, None] = None


class Project(BaseModel):
    id: int
    owner_id: int
    title: str
    importance: ProjectImportance
    executor: str
    description: Union[str, None] = None

