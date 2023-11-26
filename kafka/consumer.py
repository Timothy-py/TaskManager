from services.notifications import NotificationService
from config.kafka import kafka_consumer

async def consume():
    await kafka_consumer.start()
    try:
        async for msg in kafka_consumer:
            print("Consumed". msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
    finally:
        await kafka_consumer.stop()