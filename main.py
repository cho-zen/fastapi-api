from fastapi import FastAPI, File, UploadFile
import uuid
from fastapi.responses import FileResponse
import cv2
import pyrebase


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

    img = cv2.imread(f'{IMGDIR}image.jpg')
    
    firebase_config = {
        "apiKey": "AIzaSyCUagURc1l3froPMMFLnUHgIs9eOODB9XI",
        "authDomain": "survey-application-c9806.firebaseapp.com",
        "databaseURL": "https://survey-application-c9806-default-rtdb.firebaseio.com",
        "projectId": "survey-application-c9806",
        "storageBucket": "survey-application-c9806.appspot.com",
        "messagingSenderId": "112280167703",
        "appId": "1:112280167703:web:aadeff65cb8141f52d0352"
        }

    firebase = pyrebase.initialize_app(firebase_config)

    # Get the auth object
    auth = firebase.auth()

    # Get the current user
    user = auth.current_user

    # Get the user's token
    token = user

    # Connect to Database
    db = firebase.database()

    db.child("/ImageData/").set(str(img[:,0,0]),token)

    # print(img[:,0,0])
    return FileResponse(f'{IMGDIR}image.jpg')



# uvicorn main:app --reload --port=8000
# uvicorn main:app --reload --port=8000 --host=0.0.0.0
