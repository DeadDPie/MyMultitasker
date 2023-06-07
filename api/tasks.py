from fastapi import APIRouter
from schemas.schemas import Task, TaskCreate, Response
from services.manage_tasks import task_service

router = APIRouter()

@router.get(
    "/tasks",
    status_code=200,
    response_model=list[Task]
)
def get_tasks():
    return task_service.get_tasks()


@router.post("/add", response_model=Response,)
def make_task(data: TaskCreate):
    return task_service.make_task(data)

@router.put(
    "/task/{id}",
    response_model=Response,
)
def delete_task(
        id: int, mail: str, password: str):
    return task_service.delete_task(id, mail, password)
