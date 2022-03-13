from fastapi import FastAPI

app = FastAPI()
data_store = dict()


@app.get('/')
async def index():
    return {'status': 'ok', 'data': 'not implemented yet'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5030)
