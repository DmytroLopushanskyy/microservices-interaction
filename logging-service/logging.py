from fastapi import FastAPI, Body

app = FastAPI()
data_store = dict()


@app.get('/')
async def get_all_stored_data():
    return {'status': 'ok', 'data': '. '.join(data_store.values())}


@app.post('/')
async def write_message(msg: str = Body(..., title="msg", embed=True),
                uuid: str = Body(..., title="msg", embed=True)):
    print(f"Got a new message. UUID={uuid}. Message='{msg}'")
    data_store[uuid] = msg
    return {'status': 'ok'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5020)
