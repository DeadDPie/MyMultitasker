from fastapi import APIRouter
from schemas.projects_schema import Project
from schemas.schemas import  Response
from services.manage_projects import project_service
router = APIRouter()

@router.get(
    "/projects",
    status_code=200,
    response_model=list[Project]
)
def get_projects():
    return project_service.get_projects()


@router.post("/add_project", response_model=Response)
def make_project(data: Project):
    return project_service.make_project(data)

@router.put(
    "/project/{id}",response_model=Response
)
def delete_project(
        id: int):
    return project_service.delete_project(id)
