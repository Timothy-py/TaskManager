def task_serializer(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": str(task["title"]),
        "description": str(task["description"]),
        "due_date": str(task["due_date"]),
        "status": task["status"]
    }