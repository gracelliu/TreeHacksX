import requests
import together
import os

endpoint = "https://api.together.xyz/inference"
together.api_key = os.getenv("TOGETHER_API_KEY")

def topic_classification(transcript = "As seniors approach their later years, many begin to contemplate the transition into a life phase where work takes a backseat to leisure, hobbies, and family time. They discuss strategies for ensuring financial stability, often delving into savings, investments, and estate planning to secure a comfortable future. Conversations frequently revolve around the dream of relocating to serene locations, spending more time with grandchildren, and embracing passions that career obligations previously limited. This period of life offers a chance to explore new horizons, engage in lifelong learning, and contribute to communities in meaningful ways, all while maintaining a sense of purpose and fulfillment."):
    res = requests.post(
        endpoint,
        json={
            "model": "meta-llama/Llama-2-70b-chat-hf",
            "prompt": f"""
            You are given a speech transcript, return its topic in the format "Topic Label: 'topic'".
            
            The possible labels are: 1. Health, 2. Family, 3. Retirement, 4. Hobbies, 5. Technology, 6. Housing
            
            Here is the speech transcript: {transcript}

            Return one integer corresponding to the label and nothing else (output 0 if not sure but dont just output nothing):
            """,
            "top_p": 1,
            "top_k": 40,
            "temperature": 0.3,
            "max_tokens": 1,
            "repetition_penalty": 1,
            "stop": [],
        },
        headers={
            "Authorization": "Bearer " + together.api_key,
        },
    )

    return res.json()["output"]["choices"][0]["text"]
# print(res.json()['output']['choices'][0])
# print(res.json())
