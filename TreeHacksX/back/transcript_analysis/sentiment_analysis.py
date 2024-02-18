import os
import requests

endpoint = "https://api.together.xyz/inference"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def sentiment_analysis(message):
    res = requests.post(
        endpoint,
        json={
            "model": "togethercomputer/RedPajama-INCITE-7B-Base",
            "prompt": f"""\
        Label the sentence as either "1: positive", "2: negative", "3: mixed", or "4: neutral":

        Sentence: {message}

        Respond with ONE integer corresponding to the most accurate label (NO NEWLINE CHARACTERS, OUTPUT 0 IF NOT SURE DONT JUST OUTPUT NOTHING):
        Label:""",
            "top_p": 1,
            "top_k": 40,
            "temperature": 0.8,
            "max_tokens": 1,
            "repetition_penalty": 1,
        },
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "User-Agent": "<YOUR_APP_NAME>",
        },
    )
    return res.json()["output"]["choices"][0]["text"]
