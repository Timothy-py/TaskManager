
import datetime
from pydantic import BaseModel


class NotificationCreate(BaseModel):
    task_id: str
    message: str
    timestamp: str


class TaskNotification(BaseModel):
    task_id: str
    status: str
