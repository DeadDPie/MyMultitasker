from pydantic import BaseModel

class Create_subtask_info(BaseModel):
    info: str
    subtask_id: str
    title: str

class Subtask(BaseModel):
    subtask_id: str
    title: str
    description: str
    executor_id: str



class Subtask_list(BaseModel):
    info: str
    subtasks: list[Subtask]