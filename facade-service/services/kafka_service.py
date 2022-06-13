"""
This module is responsible for coordinating Kafka objects and offering
enough methods to satisfy presentation layer needs.
"""
import asyncio

from application.kafka_producer import KafkaProducer
from application.custom_logger import LOGGER


class KafkaService:
    def __init__(self, topic, broker):
        kafka_loop = asyncio.get_event_loop()  # Create event loop
        self.__producer = KafkaProducer(LOGGER, kafka_loop, broker)
        self.topic = topic

    async def add_message_to_queue(self, msg):
        await self.__producer.send(self.topic, msg)
