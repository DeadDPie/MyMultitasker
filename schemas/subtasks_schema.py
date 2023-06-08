from typing import List, Union
from pydantic import BaseModel


class SubtaskCreate(BaseModel):
    owner_id: int
    task_id: int
    title: str

class Subtask(BaseModel):
    subtask_id: int
    task_id: int
    owner_id: int
    title: str

