from application.consul import Consul


class ConsulService:
    def __init__(self):
        self.__consul = Consul()

    def get_value(self, key):
        return self.__consul.get_value(key)

    def deregister(self):
        self.__consul.deregister()
