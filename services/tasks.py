from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from repositories.tasks import TaskRepository
from schemas.tasks import TaskCreate


class TaskService():
    # GET A TASK DETAILS
    def get_task(id: str):
        task = TaskRepository.get_task(id)

        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

        return task

    # CREATE A TASK
    def create_task(task_data: TaskCreate):
        # Convert Pydantic model to dictionary
        task_dict = jsonable_encoder(task_data)

        # Add additional fields
        task_dict["status"] = "Todo"  # Set default status

        # Insert task into DB
        task = TaskRepository.create_task(task_dict)

        # Get the inserted task from DB
        result = TaskRepository.get_task(task.inserted_id)

        return result

    # GET ALL TASKS
    def get_all_tasks():
        tasks = TaskRepository.get_all_tasks()
        print(tasks)

        return tasks
