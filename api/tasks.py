from fastapi import APIRouter
from schemas.schemas import Task, TaskCreate
from services.manage_tasks import task_service

router = APIRouter()

# привет
@router.get(
    "/tasks",
    status_code=200,
    response_model=list[Task]
)
def get_tasks():
    return task_service.get_tasks()


@router.post("/add")
def make_task(data: TaskCreate):
    return task_service.make_task(data)

@router.put(
    "/task/{id}",
)
def delete_task(
        id: int):
    return task_service.delete_task(id)
