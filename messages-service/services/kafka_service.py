"""
This module is responsible for coordinating Kafka objects and offering
enough methods to satisfy presentation layer needs.
"""
import asyncio

from application.kafka_consumer import KafkaConsumer
from application.custom_logger import LOGGER
from application.constants import MESSAGES_TOPIC


class KafkaService:
    def __init__(self, data_access, kafka_loop):
        self.__producer = KafkaConsumer(LOGGER, kafka_loop, data_access)

    async def consume(self):
        await self.__producer.consume()

    def get_data(self):
        return self.__producer.get_data()
