import random
import json

from application.constants import LOGGING_SERVICE_URLS
from data_access import DataAccess


class Logging:
    def __init__(self):
        self.__data_access = DataAccess()
        self.logging_url = self.__get_logging_url()

    async def get_data(self):
        """
        Get the data saved in the Logging Microservice
        :return: status: bool, data: str
        """
        try:
            logging_resp = await self.__data_access.get(self.logging_url)
            logging_resp = json.loads(logging_resp.text).get('data')
            return True, logging_resp
        except Exception as e:
            return False, f'error, logging unavailable. {e}'

    async def send_data(self, data):
        """
        Send the data saved to Logging Microservice
        :return: status: bool, data: str
        """
        try:
            await self.__data_access.post(self.logging_url, data)
        except Exception as e:
            return False, f'error, logging unavailable. {e}'
        return True, 'ok'

    def __get_logging_url(self):
        """
        Get a random logging service URL.
        :return: str
        """
        return random.choice(LOGGING_SERVICE_URLS)
