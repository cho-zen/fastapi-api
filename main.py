from fastapi import FastAPI, File, UploadFile
import uuid
from fastapi.responses import FileResponse

IMGDIR = "static/"
app = FastAPI()


@app.get('/')
async def index():
    return "Hello Shivam!!"


@app.post('/upload')
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"image.jpg"
    contents = await file.read()

    # Save the file
    with open(f"{IMGDIR}{file.filename}","wb") as f:
        f.write(contents)

    return FileResponse(f'{IMGDIR}image.jpg')



# uvicorn main:app --reload --port=8000
# uvicorn main:app --reload --port=8000 --host=0.0.0.0
