from fastapi import APIRouter, Body, status
from services.tasks import TaskService
from schemas.tasks import TaskCreate, TaskResponse, TaskUpdate

task_api_router = APIRouter()


# GET A TASK DETAILS
@task_api_router.get("/", tags=["Task"], response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def get_task(id: str):
    return TaskService.get_task(id)


# CREATE TASK
@task_api_router.post("/", tags=["Task"], response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate = Body(...)):
    return TaskService.create_task(task_data)


# GET ALL TASKS
@task_api_router.get("/all", tags=["Task"], response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def get_all_tasks():
    return TaskService.get_all_tasks()


# UPDATE TASK STATUS
@task_api_router.patch("{id}/status", tags=["Task"], response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update_task_status(id: str, status: TaskUpdate = Body(...)):
    return TaskService.update_task_status(id, status)