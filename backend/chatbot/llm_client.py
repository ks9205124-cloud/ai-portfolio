import os
from dotenv import load_dotenv
from groq import Groq
from context import get_parsed_resume

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

prompt_system = get_parsed_resume()

message_system = {
        "role" : "system",
        "content" : prompt_system,
    }

def llm_ans(prompt_user):
    message_user = {
        "role":"user",
        "content":prompt_user
    }
    messages = [message_system,message_user]
    response = client.chat.completions.create(
        model = model,
        messages=messages,
    )
    ans = response.choices[0].message.content
    return ans

