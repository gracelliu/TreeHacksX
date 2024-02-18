from fastapi import FastAPI, HTTPException, Form, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO

from back.transcript_analysis.gcp_speech_to_text import gcs_speech_to_text
from fastapi.middleware.cors import CORSMiddleware

from back.vector import *

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/photo/")
async def get_photo_link(user_id: int):
    client, conn = create_connection()
    while conn.begin():
        return get_photo(conn, user_id)
                        
@app.get("/submit")
async def quiz_submit(image_id: int, description: str, user_id: int):
    client, conn = create_connection()
    while conn.begin():
        return check_similarity(client, conn, image_id, description, user_id)

@app.post("/transcribe/")
async def transcribe_audio(audio_data: UploadFile = Form(...)):
    try:
        # Read the audio file content
        audio_content = await audio_data.read()
        # audio_content = await audio_data.read()
        # print(audio_content)

        # # Use the BytesIO to create a file-like object
        # audio_file_like = BytesIO(audio_content)
        # print(audio_file_like)

        # Call your GCP speech-to-text function
        transcription_result = gcs_speech_to_text(audio_data, audio_content)

        # Return the transcription result
        return JSONResponse(content={"transcription": transcription_result})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
