import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API key not found")

response = openai.Completion.create(
    model="gpt-4o-mini",
    prompt="Q: Write a poem about Cognizant\n A: ",
    temperature = 0.2,
    max_tokens = 50,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0,
    stop = ["\n"]
)

print(response['choices'][0]['text'])