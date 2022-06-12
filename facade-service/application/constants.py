"""
Contains configs and other constants
"""
# Services
LOGGING_SERVICE_URLS = [
    "http://127.0.0.1:5020",
    "http://127.0.0.1:5021",
    "http://127.0.0.1:5022"
]
MESSAGES_SERVICE_URLS = [
    "http://127.0.0.1:5030",
    "http://127.0.0.1:5031"
]

# Kafka
KAFKA_BROKER = '127.0.0.1:9092'
MESSAGES_TOPIC = 'messages'

# App
APP_PORT = 5000
