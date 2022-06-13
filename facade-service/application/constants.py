"""
Contains configs and other constants
"""
from dotenv import load_dotenv

load_dotenv(dotenv_path='./facade-service.env')

# Consul Configs
CONSUL_HOST = '127.0.0.1'
CONSUL_PORT = 8500

# Key names in Consul
KAFKA_BROKER = 'KAFKA_BROKER'
MESSAGES_TOPIC = 'MESSAGES_TOPIC'
LOGGING_SERVICE_NAME = "logging-service"
MESSAGES_SERVICE_NAME = "messages-service"

# App
APP_NAME = 'facade-service'

