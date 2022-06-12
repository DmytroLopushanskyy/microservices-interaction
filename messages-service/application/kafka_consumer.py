import json
from aiokafka import AIOKafkaConsumer

from application.constants import KAFKA_BROKER, KAFKA_CONSUMER_GROUP, MESSAGES_TOPIC


class KafkaConsumer:
    def __init__(self, logger, event_loop, data_access):
        self.__logger = logger
        self.__consumer = AIOKafkaConsumer(
            MESSAGES_TOPIC,
            loop=event_loop,
            bootstrap_servers=[KAFKA_BROKER],
            group_id=KAFKA_CONSUMER_GROUP
        )
        self.__data_access = data_access

    async def consume(self):
        await self.__consumer.start()
        try:
            async for rec in self.__consumer:
                msg = json.loads(rec.value)
                msg = str(msg)
                self.__logger.info(f'Consumed msg: {msg}')

                self.__data_access.save_data(msg)

                await self.__consumer.commit()
        except Exception as err:
            self.__logger.error(f'Consumer error: {err}')
        finally:
            await self.__consumer.stop()

    def get_data(self):
        return self.__data_access.get_data()
