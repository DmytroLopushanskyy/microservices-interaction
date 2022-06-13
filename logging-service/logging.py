import os
import hazelcast
from fastapi import FastAPI, Body

from application.constants import HZ_MAP_NAME, HZ_CLUSTER
from services.consul_service import ConsulService


app = FastAPI()
consul_service = ConsulService()
hz = hazelcast.HazelcastClient(cluster_name=consul_service.get_value(HZ_CLUSTER))
data_store = hz.get_map(consul_service.get_value(HZ_MAP_NAME)).blocking()


@app.get('/')
async def get_all_stored_data():
    return {'status': 'ok', 'data': '. '.join(data_store.values())}


@app.post('/')
async def write_message(msg: str = Body(..., title="msg", embed=True),
                uuid: str = Body(..., title="msg", embed=True)):
    print(f"Got a new message. UUID={uuid}. Message='{msg}'")
    data_store.put(uuid, msg)
    return {'status': 'ok'}


@app.on_event("shutdown")
def shutdown():
    print('Deregistering from Consul')
    consul_service.deregister()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=int(os.getenv('PORT')))
