"""
This module is responsible for the presentation layer of the messages service.
Async REST API based on FastAPI has been developed.
uvicorn api:app --workers 1 --reload
"""
import asyncio
from fastapi import FastAPI

from application.constants import APP_PORT, KAFKA_BROKER, KAFKA_CONSUMER_GROUP, MESSAGES_TOPIC
from services.kafka_service import KafkaService
from data_access import DataAccess

app = FastAPI()
data_access = DataAccess()
kafka_loop = asyncio.get_event_loop()
kafka_service = KafkaService(data_access, kafka_loop)

asyncio.create_task(kafka_service.consume())


@app.get('/')
async def index():
    data = kafka_service.get_data()
    return {'status': 'ok', 'data': ", ".join(data)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=APP_PORT)
