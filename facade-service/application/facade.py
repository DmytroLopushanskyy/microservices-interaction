import uuid


class Facade:
    def create_message(self, msg: str):
        assigned_uuid = self.__create_id()
        return {
            "msg": msg,
            "uuid": assigned_uuid
        }

    def __create_id(self):
        """
        Create unique UUID
        :return: str
        """
        return str(uuid.uuid4())
