import os
import consul

from application.constants import APP_NAME, CONSUL_HOST, CONSUL_PORT


class Consul:
    def __init__(self):
        self.__consul_client = consul.Consul(
            host=CONSUL_HOST,
            port=CONSUL_PORT
        )

        self.service_id = f'{APP_NAME}:{os.getenv("PORT")}'

        self.__consul_client.agent.service.register(
            name=APP_NAME,
            service_id=self.service_id,
            address=os.getenv("HOST"),
            port=int(os.getenv("PORT"))
        )

    def get_value(self, key: str):
        _, data = self.__consul_client.kv.get(key, index=None)
        return data["Value"].decode("utf-8") if data else None

    def deregister(self):
        self.__consul_client.agent.service.deregister(self.service_id)
