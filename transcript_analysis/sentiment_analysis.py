import os
import requests

endpoint = "https://api.together.xyz/inference"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

message = "my dog is dead."

res = requests.post(
    endpoint,
    json={
        "model": "togethercomputer/RedPajama-INCITE-7B-Base",
        "prompt": f"""\
      Label the sentence as either "positive", "negative", "mixed", or "neutral":

      Sentence: {message}
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
print(res.json()["output"]["choices"][0]["text"])
