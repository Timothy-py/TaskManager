
import datetime
from pydantic import BaseModel


class NotificationCreate(BaseModel):
    task_id: str
    message: str
    timestamp: datetime