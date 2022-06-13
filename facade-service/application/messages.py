import json

from data_access import DataAccess


class Messages:
    def __init__(self, messages_url):
        self.__data_access = DataAccess()
        self.messages_url = messages_url

    async def get_data(self):
        """
        Get the data saved in the Messages Microservice
        :return: status: bool, data: str
        """
        try:
            messages_resp = await self.__data_access.get(self.messages_url)
            messages_resp = json.loads(messages_resp.text).get('data')
            return True, messages_resp
        except Exception as e:
            return False, f'error, messages unavailable. {e}'
