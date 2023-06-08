from fastapi import APIRouter

from schemas.schemas import Response
from schemas.subtasks_schema import Subtask, SubtaskCreate
from services.manage_subtasks import subtask_service
router = APIRouter()

@router.get(
    "/subtasks",
    status_code=200,
    response_model=list[Subtask]
)
def get_subtasks():
    return subtask_service.get_subtasks()


@router.post("/add_subtasks/{id}", response_model=Response,)
def make_subtask(data: SubtaskCreate):
    return subtask_service.make_subtask(data)

@router.put(
    "/subtask/{id}", response_model=Response,
)
def delete_subtask(
        subtask_id: int):
    return subtask_service.delete_subtask(subtask_id)
