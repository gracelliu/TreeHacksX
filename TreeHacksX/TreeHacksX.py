"""Welcome to Reflex!."""

from TreeHacksX import styles

# Import all the pages.
from TreeHacksX.pages import *

from TreeHacksX.back.vector import *

from TreeHacksX.transcript_analysis.gcp_speech_to_text import *

import reflex as rx

from fastapi import  HTTPException, Form, UploadFile
import base64
from io import BytesIO




class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)

async def get_photo_link(user_id: int):
    client, conn = create_connection()
    return get_photo(conn, user_id)

async def transcribe_audio(audio_file: UploadFile = Form(...)):
    try:
        # Read the audio file content
        audio_content = await audio_file.read()

        # Use the BytesIO to create a file-like object
        audio_file_like = BytesIO(audio_content)

        # Call your GCP speech-to-text function
        transcription_result = gcs_speech_to_text(audio_file_like)

        # Return the transcription result
        return {"transcription": transcription_result }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
                        
async def quiz_submit(client, conn, image_id: int, description: str, user_id: int):
    client, conn = create_connection()
    return check_similarity(client, conn, image_id, description, user_id)

app.api.add_api_route("/photo", get_photo_link)
app.api.add_api_route("/submit", quiz_submit)
app.api.add_api_route("/transcribe", transcribe_audio)





