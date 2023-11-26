import json
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event
from fastapi_events.typing import Event
from config.kafka import kafka_manager


producer = kafka_manager.kafka_producer


@local_handler.register(event_name="task-update")
async def handle_task_update(event: Event):
    """Handles a task update event"""

    # Publish the updated task event to Kafka
    kafka_data_object = json.dumps(event[-1]).encode('utf-8')
    await producer.send("task-manager", value=kafka_data_object)
    await producer.flush()
    return
