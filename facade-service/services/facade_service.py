from application.facade import Facade
from application.messages import Messages
from application.logging import Logging


class FacadeService:
    def __init__(self):
        self.__facade = Facade()
        self.__logging = Logging()
        self.__mess = Messages()

    def create_message(self, msg: str):
        return self.__facade.create_message(msg)

    async def get_data_from_logging(self):
        return await self.__logging.get_data()

    async def send_data_to_logging(self, data: dict):
        return await self.__logging.send_data(data)

    async def get_data_from_mess(self):
        return await self.__mess.get_data()
