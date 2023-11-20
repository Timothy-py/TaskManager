from bson import ObjectId
from config.database import tasks_collection

class TaskRepository():
    def get_task(id:str):
        return tasks_collection.find_one({"_id": ObjectId(id)})
    
    def get_all_tasks():
        return tasks_collection.find()
    
    def create_task(task:dict):
        return tasks_collection.insert_one(task)

    def update_task(id:str, task:dict):
        return tasks_collection.update_one({"_id": ObjectId(id)}, {"$set": task})

    def delete_task(id:str):
        return tasks_collection.delete_one({"_id": ObjectId(id)})