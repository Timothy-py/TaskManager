import asyncio
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
from workers.task_worker import create_notification
from config.config import env_vars

BOOTSTRAP_SERVERS = env_vars.BOOTSTRAP_SERVERS
KAFKA_TOPIC = env_vars.KAFKA_TOPIC


class KafkaManager:
    def __init__(self, kafka_instance):
        self.loop = asyncio.get_event_loop()
        self.kafka_producer = AIOKafkaProducer(
            loop=self.loop, bootstrap_servers=kafka_instance)
        self.kafka_consumer = AIOKafkaConsumer(
            KAFKA_TOPIC, loop=self.loop, bootstrap_servers=kafka_instance)

    async def consume(self):
        await self.kafka_consumer.start()
        try:
            async for msg in self.kafka_consumer:
                create_notification(json.loads(msg.value))
        finally:
            await self.kafka_consumer.stop()

    async def setup(self):
        await self.kafka_producer.start()
        self.loop.create_task(self.consume())

    async def close(self):
        await self.kafka_producer.stop()
        await self.kafka_consumer.stop()


KAFKA_INSTANCE = BOOTSTRAP_SERVERS
kafka_manager = KafkaManager(KAFKA_INSTANCE)
