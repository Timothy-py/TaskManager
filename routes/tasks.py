from fastapi import APIRouter

task_api_router = APIRouter()

# GET ALL TAKSS
@task_api_router.get("/", tags=["Task"])
async def read_tasks():
    return {"status": "ok", "data": []}