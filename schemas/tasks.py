from datetime import datetime
from typing import Annotated
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, Field

# Pydantic model for task creation
class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: datetime

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

# Pydantic model for task response
class TaskResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
    due_date: datetime
    status: str

    class Config:
        from_attributes = True