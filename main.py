from fastapi import FastAPI
from os import environ as env

app = FastAPI()


@app.get('/')
async def index():
    return {"details":"Hello Shivam!!"}



# uvicorn main:app --reload --port=8000
# uvicorn main:app --reload --port=8000 --host=0.0.0.0
