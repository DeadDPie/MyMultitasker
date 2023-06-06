from fastapi import APIRouter
from schemas.subtasks_schema import Subtask
from services.manage_subtasks import subtask_service
router = APIRouter()

@router.get(
    "/subtasks",
    status_code=200,
    response_model=list[Subtask]
)
def get_subtasks():
    return subtask_service.get_subtasks()


@router.post("/add")
def make_subtask(data: Subtask):
    return subtask_service.make_subtask(data)

@router.put(
    "/subtask/{id}",
)
def delete_subtask(
        id: int):
    return subtask_service.delete_subtask(id)
