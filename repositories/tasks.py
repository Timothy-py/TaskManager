from bson import ObjectId
from config.database import db_tasks

class TaskRepository():
    def get_task(id:str):
        return db_tasks.find_one({"_id": ObjectId(id)})
    
    def get_tasks():
        return db_tasks.find()
    
    def create_task(task:dict):
        return db_tasks.insert_one(task)

    def update_task(id:str, task:dict):
        return db_tasks.update_one({"_id": ObjectId(id)}, {"$set": task})

    def delete_task(id:str):
        return db_tasks.delete_one({"_id": ObjectId(id)})