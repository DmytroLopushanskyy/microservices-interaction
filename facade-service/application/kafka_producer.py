import json
from aiokafka import AIOKafkaProducer


class KafkaProducer:
    def __init__(self, logger, event_loop, broker):
        self.__logger = logger
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=[broker],
            value_serializer=lambda data: json.dumps(data).encode("utf-8"),
            loop=event_loop
        )

    async def send(self, topic, message):
        await self.__producer.start()
        try:
            await self.__producer.send_and_wait(topic=topic, value=message)
            self.__logger.info(f"Successfully sent message to {topic} topic")
            await self.__producer.stop()
        except:
            self.__logger.error(f"Error while sending a message to {topic} topic.")
            await self.__producer.stop()
