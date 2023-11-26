import asyncio
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json


class KafkaManager:
    def __init__(self, kafka_instance):
        self.loop = asyncio.get_event_loop()
        self.kafka_producer = AIOKafkaProducer(
            loop=self.loop, bootstrap_servers=kafka_instance)
        self.kafka_consumer = AIOKafkaConsumer(
            "task-manager", loop=self.loop, bootstrap_servers=kafka_instance)

    async def consume(self):
        await self.kafka_consumer.start()
        try:
            async for msg in self.kafka_consumer:
                print(f"Kafka consumer message - {msg}")
                # print("Consumed". msg.topic, msg.partition,
                #         msg.offset, msg.key, msg.value, msg.timestamp)
        finally:
            await self.kafka_consumer.stop()

    async def setup(self):
        await self.kafka_producer.start()
        self.loop.create_task(self.consume())

    async def close(self):
        await self.kafka_producer.stop()
        await self.kafka_consumer.stop()


KAFKA_INSTANCE = "localhost:9092"
kafka_manager = KafkaManager(KAFKA_INSTANCE)
