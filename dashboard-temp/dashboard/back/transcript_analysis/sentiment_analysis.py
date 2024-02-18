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
        Label the sentence as either "0: neutral", "1: positive", or "2: negative":

        Sentence: {message}

        Here is EXACTLY ONE integer in arabic format corresponding to the most accurate label:
        """,
            "top_p": 1,
            "top_k": 100,
            "temperature": 0.6,
            "max_tokens": 1,
            "repetition_penalty": 1,
        },
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
        },
    )
    return res.json()["output"]["choices"][0]["text"]
