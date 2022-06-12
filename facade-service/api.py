"""
This module is responsible for the presentation layer of the facade service.
Async REST API based on FastAPI has been developed.
"""
from fastapi import FastAPI, Body

from application.constants import APP_PORT
from services.facade_service import FacadeService
from services.kafka_service import KafkaService


app = FastAPI()


@app.post('/')
async def index(msg: str = Body(..., title="msg", embed=True)):
    facade_service = FacadeService()
    kafka_service = KafkaService()

    data = facade_service.create_message(msg)
    logging_status, logging_resp = await facade_service.send_data_to_logging(data)

    await kafka_service.add_message_to_queue(msg)

    if logging_status:
        return {'status': 'ok'}

    return {
        'status': 'error',
        'data': f'Logging service response: {logging_resp}'
    }


@app.get('/')
async def index():
    facade_service = FacadeService()
    logging_status, logging_resp = await facade_service.get_data_from_logging()
    mess_status, mess_resp = await facade_service.get_data_from_mess()

    combined_resp = f'Logging service response: {logging_resp}. ' \
                      f'Messaging service response: {mess_resp}.'

    if mess_status and logging_status:
        return {'status': 'ok', 'data': combined_resp}
    return {'status': 'error', 'data': combined_resp}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=APP_PORT)
