"""
This module is responsible for the presentation layer of the messages service.
Async REST API based on FastAPI has been developed.
"""
import asyncio
from fastapi import FastAPI

from services.kafka_service import KafkaService
from data_access import DataAccess
from services.consul_service import ConsulService
from application.constants import MESSAGES_TOPIC, KAFKA_BROKER, KAFKA_CONSUMER_GROUP


app = FastAPI()
consul_service = ConsulService()
data_access = DataAccess()
kafka_loop = asyncio.get_event_loop()
kafka_service = KafkaService(kafka_loop=kafka_loop,
                             data_access=data_access,
                             topic=consul_service.get_value(MESSAGES_TOPIC),
                             grp=consul_service.get_value(KAFKA_CONSUMER_GROUP),
                             broker=consul_service.get_value(KAFKA_BROKER))

asyncio.create_task(kafka_service.consume())


@app.get('/')
async def index():
    data = kafka_service.get_data()
    return {'status': 'ok', 'data': ", ".join(data)}


@app.on_event("shutdown")
def shutdown():
    print('Deregistering from Consul')
    consul_service.deregister()
