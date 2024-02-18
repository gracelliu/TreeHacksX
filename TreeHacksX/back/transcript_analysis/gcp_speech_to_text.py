import os
import wave
from google.cloud import storage, speech
from google.oauth2 import service_account
import io
import json
import base64
import secrets
import string

def generate_random_string(length=10):
    alphabet = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(alphabet) for _ in range(length))
    return random_string

def gcs_speech_to_text(wav_file, source_file_name):

    # used to extract header information from the audio file
        # Convert audio data to Base64
    audio_data_base64 = base64.b64encode(source_file_name).decode('utf-8')

    # Speech Client
    with open('../credentials.json', 'r') as json_file:
        credentials_json = json.load(json_file)

        credentials = service_account.Credentials.from_service_account_info(credentials_json)
    client = speech.SpeechClient(credentials=credentials)

    # Use Base64-encoded audio data
    audio = speech.RecognitionAudio(content=audio_data_base64)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        sample_rate_hertz=48000,
        language_code="en-US",
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    # def get_wav_properties(wav_file):
    #     with wave.open(wav_file, 'rb') as wav_file:
    #         print("getting sample rate")
    #         sample_rate = wav_file.getframerate()

    #         sample_width = wav_file.getsampwidth()
    #         num_channels = wav_file.getnchannels()
    #         return sample_rate, sample_width, num_channels

    # def upload_blob(bucket_name, source_file_name, destination_blob_name):
    #     """Uploads a file to the bucket."""
    #     storage_client = storage.Client(credentials=credentials)
    #     bucket = storage_client.bucket(bucket_name)
    #     blob = bucket.blob(destination_blob_name)
    #     print(blob)
    #     blob.upload_from_string(source_file_name)

    #     print(f"File {source_file_name} uploaded to {destination_blob_name}.")
        
    # # Create credentials from the dictionary
    # with open('../credentials.json', 'r') as json_file:
    #     credentials_json = json.load(json_file)

    #     credentials = service_account.Credentials.from_service_account_info(credentials_json)

    # # Set the GCS bucket name and construct the destination blob name
    # bucket_name = 'treehacksx'
    # file_name = generate_random_string()
    # destination_blob_name = f"audio-files/{file_name}"

    # # Upload the WAV file to GCS
    # print("am i here?")
    # upload_blob(bucket_name, source_file_name, destination_blob_name)

    # # Speech Client
    # client = speech.SpeechClient(credentials=credentials)

    # # Use the GCS URI of the uploaded file
    # gcs_uri = f"gs://{bucket_name}/{destination_blob_name}"

    # # Dynamically determine sample rate and encoding
    # sample_rate, sample_width, _ = get_wav_properties(wav_file)
    # if sample_width == 2:
    #     encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    # else:
    #     raise ValueError(f"Unsupported sample width: {sample_width}")

    # config = speech.RecognitionConfig(
    #     encoding=encoding,
    #     sample_rate_hertz=sample_rate,
    #     language_code="en-US"
    # )
    # audio = speech.RecognitionAudio(uri=gcs_uri)
    # operation = client.long_running_recognize(config=config, audio=audio)
    # print("Waiting for operation to complete...")
    # response = operation.result(timeout=90)

    # Compile the transcription into one string
    output = ""
    for result in response.results:
        output = output + result.alternatives[0].transcript + ". "
    
    # print(output + "\n--------------------------------------")
    return output


if __name__ == "__main__":
    audio_file_path = '/Users/graceliu/Downloads/female.wav'
    gcs_speech_to_text(audio_file_path)
