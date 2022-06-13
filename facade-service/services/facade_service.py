import random

from application.facade import Facade
from application.messages import Messages
from application.logging import Logging
from application.consul import Consul
from application.constants import LOGGING_SERVICE_NAME, MESSAGES_SERVICE_NAME


class FacadeService:
    def __init__(self):
        self.__facade = Facade()
        self.__consul = Consul()

        self.__logging = Logging(self.__get_logging_url())
        self.__mess = Messages(self.__get_mess_url())

    def create_message(self, msg: str):
        return self.__facade.create_message(msg)

    async def get_data_from_logging(self):
        return await self.__logging.get_data()

    async def send_data_to_logging(self, data: dict):
        return await self.__logging.send_data(data)

    async def get_data_from_mess(self):
        return await self.__mess.get_data()

    def __get_logging_url(self):
        urls = self.__consul.get_service_urls(LOGGING_SERVICE_NAME)
        print(f'Discovered {LOGGING_SERVICE_NAME} URLs', urls)
        if not urls:
            return 'not-available'
        return random.choice(urls)

    def __get_mess_url(self):
        urls = self.__consul.get_service_urls(MESSAGES_SERVICE_NAME)
        print(f'Discovered {MESSAGES_SERVICE_NAME} URLs', urls)
        if not urls:
            return 'not-available'
        return random.choice(urls)
