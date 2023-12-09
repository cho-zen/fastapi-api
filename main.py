from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse
import uuid
from fastapi.responses import FileResponse
import cv2
import pyrebase
import face_recognition

IMGDIR = "static/"
app = FastAPI()

@app.get('/')
async def index():
    return "Hello Shivam!!"

@app.post('/upload/{user_number}/{survey}',response_class=PlainTextResponse)
async def upload_image(user_number,survey,file: UploadFile = File(...)):
    file.filename = f"image.jpg"
    contents = await file.read()

    # Save the file
    with open(f"{IMGDIR}{file.filename}","wb") as f:
        f.write(contents)
    
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

    # Loading Face Encodings from an Image
    img = cv2.imread(f'{IMGDIR}image.jpg')
    find_face = face_recognition.face_locations(img)

    if len(find_face) == 0:
        return PlainTextResponse("0")   

    else:
        face_enc = face_recognition.face_encodings(img)

        # print(face_enc)

        db.child(f"Data201/{user_number}/{survey}/ImageData").push(str(face_enc[0]),token)


    return FileResponse(f'{IMGDIR}image.jpg')



# uvicorn main:app --reload --port=8000
# uvicorn main:app --reload --port=8000 --host=0.0.0.0
