from fastapi import FastAPI, File, UploadFile
import uuid

app = FastAPI()


@app.get('/')
async def index():
    return "Hello Shivam!!"


@app.post('/upload')
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    return {"filename": file.filename}


# uvicorn main:app --reload --port=8000
# uvicorn main:app --reload --port=8000 --host=0.0.0.0
