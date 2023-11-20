from fastapi import APIRouter, Body
from services.tasks import TaskService
from schemas.tasks import TaskCreate, TaskResponse

task_api_router = APIRouter()

# GET ALL TAKSS
@task_api_router.get("/", tags=["Task"], response_model=TaskResponse)
async def get_task(id:str):
    return TaskService.get_task(id)

# CREATE TASK
@task_api_router.post("/", tags=["Task"], response_model=TaskResponse)
async def create_task(task_data: TaskCreate=Body(...)):
    return TaskService.create_task(task_data)