from typing import List, Union
from pydantic import BaseModel

from schemas import Task


class ProjectCreate(BaseModel):
    owner_id: int
    title: str

class Project(BaseModel):
    proj_id: int
    owner_id: int
    title: str
    tasks: Union[List[int], None]#id of tasks

