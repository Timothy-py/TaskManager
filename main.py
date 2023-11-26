from fastapi import FastAPI
from fastapi_events.middleware import EventHandlerASGIMiddleware
from fastapi_events.handlers.local import local_handler
from contextlib import asynccontextmanager
# from middlewares.exceptions import ExceptionHandlerMiddleware
from routes.tasks import task_api_router
from event.handlers import handle_task_update
from config.kafka import kafka_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_manager.setup()
    yield
    await kafka_manager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(task_api_router, prefix="/api/v1/tasks")
app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])
app.add_middleware(ExceptionHandlerMiddleware)


handle_task_update
