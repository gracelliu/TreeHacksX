import os
import together

together.api_key = os.getenv("TOGETHER_API_KEY")

temp = """
Given this caption and the following paragraphs, check if the caption and paragraph describe the same event. Output your answer as true or false in the format:
"Output: [True/False]"

Caption:
    "Aluminium cans, a marvel of modern engineering, have transformed the way we package and consume beverages. Their lightweight yet durable construction ensures that your favorite drinks stay fresh and portable, while their recyclable nature contributes to a more sustainable future. From chilled sodas to craft brews, aluminium cans have become synonymous with convenience and environmental responsibility, making them a staple in our everyday lives.",

Paragraphs:
    "Aluminium cans are a juicy,li. From chilled sodas to craft brews, aluminium cans have become synonymous with convenience and environm beverages cherished worldwide as a delicious and nutritious treat."

"""

prompt = f"<human>: {temp}\n<bot>:"

output = together.Complete.create(
    prompt=prompt,
    model="meta-llama/Llama-2-70b-chat-hf",
    max_tokens=1000,
    temperature=0.3,
    top_k=60,
    top_p=0.6,
    repetition_penalty=1.1,
    stop=["Explanation"],
)

# print generated text
print(output["output"]["choices"][0]["text"])
