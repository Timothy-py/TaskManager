from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config.config import env_vars
 
# Create a new client and connect to the server
client = MongoClient(env_vars.DB_URI, server_api=ServerApi('1'))

mongo_client = client.TaskManager

tasks_collection = mongo_client["tasks"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)