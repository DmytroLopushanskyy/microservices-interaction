from fastapi import FastAPI, Body
import hazelcast

app = FastAPI()
hz = hazelcast.HazelcastClient(cluster_name="hz-cluster-3")
data_store = hz.get_map("distributed-map").blocking()


@app.get('/')
async def get_all_stored_data():
    return {'status': 'ok', 'data': '. '.join(data_store.values())}


@app.post('/')
async def write_message(msg: str = Body(..., title="msg", embed=True),
                uuid: str = Body(..., title="msg", embed=True)):
    print(f"Got a new message. UUID={uuid}. Message='{msg}'")
    data_store.put(uuid, msg)
    return {'status': 'ok'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5020)
