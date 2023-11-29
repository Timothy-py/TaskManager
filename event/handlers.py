import json
from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event
from fastapi_events.typing import Event
from config.kafka import kafka_manager
from config.config import env_vars

KAFKA_TOPIC = env_vars.KAFKA_TOPIC

producer = kafka_manager.kafka_producer


@local_handler.register(event_name="task-update")
async def handle_task_update(event: Event):
    """Handles a task update event"""

    # Publish the updated task event to Kafka
    kafka_data_object = json.dumps(event[-1]).encode('utf-8')
    await producer.send(KAFKA_TOPIC, value=kafka_data_object)
    await producer.flush()
    return
