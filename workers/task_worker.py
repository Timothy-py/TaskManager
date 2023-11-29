import datetime
from services.notifications import NotificationService
from schemas.notifications import TaskNotification


def create_notification(task: TaskNotification):
    """
    Creates a notification for a task update
    """
    task_id = task["task_id"]
    status = task["status"]
    data = {
        "task_id": task_id,
        "message": f"Task {task_id} is {status}",
        "timestamp": datetime.datetime.now()
    }
    NotificationService.create_notification(data)
    return
