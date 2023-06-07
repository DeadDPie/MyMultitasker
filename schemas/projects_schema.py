from typing import List, Union
from pydantic import BaseModel

    

class ProjectCreate(BaseModel):
    owner_id: int
    title: str
    description: Union[str, None] = None


class Project(BaseModel):
    proj_id: int
    owner_id: int
    title: str
    description: Union[str, None] = None

