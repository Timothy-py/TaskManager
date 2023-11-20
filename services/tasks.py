from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from repositories.tasks import TaskRepository
from schemas.tasks import TaskCreate, TaskUpdate


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

        return tasks

    # UPDATE TASK STATUS
    def update_task_status(id: str, status: str):
        # Convert Pydantic model to dictionary
        update_data = jsonable_encoder(status)

        # Update the task in MongoDB
        result = TaskRepository.update_task(id, update_data)

        # Check if the task was updated successfully
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Task with ID {id} not found"
            )

        # Get the updated task from MongoDB
        updated_task = TaskRepository.get_task(id)

        # Return the updated task as a response
        return updated_task

    # DELETE TASK ITEM
    def delete_task(id: str):
        # Delete the task from MongoDB
        result = TaskRepository.delete_task(id)

        # Check if the task was deleted successfully
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Task with ID {id} not found"
            )

        return True