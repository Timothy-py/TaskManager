from fastapi import FastAPI
from middlewares.exceptions import ExceptionHandlerMiddleware
from routes.tasks import task_api_router

app = FastAPI()


app.include_router(task_api_router)
app.add_middleware(ExceptionHandlerMiddleware)