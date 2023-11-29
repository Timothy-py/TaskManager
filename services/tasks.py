import json
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi_events.dispatcher import dispatch
from repositories.tasks import TaskRepository
from schemas.tasks import TaskCreate
from config.redis import redis_cache
from serializers.task import task_serializer


class TaskService():
    # GET A TASK DETAILS
    def get_task(id: str):
        # Check if the task is in cache
        cache = redis_cache.get(f"task_{id}")
        if cache is not None:
            load = json.loads(cache)
            data = {
                "_id": id,
                "title": load["title"],
                "description": load["description"],
                "due_date": load["due_date"],
                "status": load["status"],
            }
            return data

        # Get the task from DB
        task = TaskRepository.get_task(id)

        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

        # Serialize the task
        data = task_serializer(task)

        # Add the task to cache
        redis_cache.set(f"task_{id}", json.dumps(data), 60)

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

        # Emit the task update event
        dispatch(event_name="task-update",
                 payload={"task_id": id, **update_data})

        # Get the updated task from MongoDB
        updated_task = TaskRepository.get_task(id)

        # Serialize the task
        data = task_serializer(updated_task)

        # Add the task to cache
        redis_cache.set(f"task_{id}", json.dumps(data), 60)

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

        # Delete the task from cache
        redis_cache.delete(f"task_{id}")

        return True
