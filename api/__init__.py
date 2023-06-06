from fastapi import APIRouter

from api.users import router as user_router
from api.tasks import router as item_router
from api.projects import router as project_router
from api.subtasks import router as subtask_router

router = APIRouter()

router.include_router(user_router)
router.include_router(item_router)
router.include_router(project_router)
router.include_router(subtask_router)