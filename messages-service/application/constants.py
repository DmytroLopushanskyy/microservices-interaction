"""
Contains configs and other constants
"""
from dotenv import load_dotenv

load_dotenv(dotenv_path='./messages-service.env')

# Consul
CONSUL_HOST = '127.0.0.1'
CONSUL_PORT = 8500

# Key names in Consul
KAFKA_BROKER = 'KAFKA_BROKER'
MESSAGES_TOPIC = 'MESSAGES_TOPIC'
KAFKA_CONSUMER_GROUP = 'KAFKA_CONSUMER_GROUP'
LOGGING_SERVICE_NAME = "logging-service"
MESSAGES_SERVICE_NAME = "messages-service"

# App
APP_NAME = 'messages-service'
