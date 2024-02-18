import requests
import together
import os

endpoint = "https://api.together.xyz/inference"
together.api_key = os.getenv("TOGETHER_API_KEY")

def topic_classification(transcript = "As seniors approach their later years, many begin to contemplate the transition into a life phase where work takes a backseat to leisure, hobbies, and family time. They discuss strategies for ensuring financial stability, often delving into savings, investments, and estate planning to secure a comfortable future. Conversations frequently revolve around the dream of relocating to serene locations, spending more time with grandchildren, and embracing passions that career obligations previously limited. This period of life offers a chance to explore new horizons, engage in lifelong learning, and contribute to communities in meaningful ways, all while maintaining a sense of purpose and fulfillment."):
    res = requests.post(
        endpoint,
        json={
            "model": "togethercomputer/RedPajama-INCITE-7B-Base",
            "prompt": f"""
            Label the transcript with its corresponding topic as either "1: Health and Wellness", "2: Family and Relationships", "3: Retirement Planning", "4: Leisure and Hobbies", "5: Technology", "6: Healthcare and Social Services":
            
            Here is the speech transcript: {transcript}

            Here is EXACTLY ONE integer corresponding to the most accurate label:
            """,
            "top_p": 1,
            "top_k": 100,
            "temperature": 0.6,
            "max_tokens": 1,
            "repetition_penalty": 1,
        },
        headers={
            "Authorization": "Bearer " + together.api_key,
        },
    )

    return res.json()["output"]["choices"][0]["text"]
# print(res.json()['output']['choices'][0])
# print(res.json())
