"""
Contains configs and other constants
"""
from dotenv import load_dotenv

load_dotenv(dotenv_path='./logging-service.env')

# Hazelcast
HZ_CLUSTER = 'HZ_CLUSTER'
HZ_MAP_NAME = 'HZ_MAP_NAME'

# Consul
CONSUL_HOST = '127.0.0.1'
CONSUL_PORT = 8500

# App
APP_NAME = 'logging-service'

