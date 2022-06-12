"""
This module is responsible for getting the data for the facade service.
"""
import uuid


class DataAccess:
    def __init__(self):
        self.__data_dict = dict()

    def save_data(self, msg):
        assigned_uuid = self.__create_id()
        self.__data_dict[assigned_uuid] = msg

    def __create_id(self):
        """
        Create unique UUID
        :return: str
        """
        return str(uuid.uuid4())

    def get_data(self):
        print(list(self.__data_dict.values()))
        return list(self.__data_dict.values())
