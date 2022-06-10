from fastapi import FastAPI, Body
import uuid
import httpx
import json
import random

app = FastAPI()
logging_service_url = [
    "http://127.0.0.1:5020",
    "http://127.0.0.1:5021",
    "http://127.0.0.1:5022"
]
messages_service_url = "http://127.0.0.1:5030"


@app.post('/')
async def index(msg: str = Body(..., title="msg", embed=True)):
    uuid_assigned = uuid.uuid4()

    data_to_send = {
        "msg": msg,
        "uuid": str(uuid_assigned)
    }

    async with httpx.AsyncClient() as client:
        random_logging_url = random.choice(logging_service_url)
        try:
            await client.post(random_logging_url, json=data_to_send)
        except:
            return {'status': 'error, logging unavailable'}

    return {'status': 'ok'}


@app.get('/')
async def index():
    async with httpx.AsyncClient() as client:
        random_logging_url = random.choice(logging_service_url)
        try:
            logging_resp = await client.get(random_logging_url)
            logging_resp = json.loads(logging_resp.text).get('data')
        except:
            return {'status': 'error, logging unavailable'}

        messages_resp = await client.get(messages_service_url)
        messages_resp = json.loads(messages_resp.text).get('data')

    return {'status': 'ok', 'data': f"{logging_resp}. {messages_resp}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)
