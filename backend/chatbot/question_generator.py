import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import ValidationError

from chatbot.prompts.question_prompts import get_system_prompt
from chatbot.schemas.question_schemas import llmOutputSchema

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

prompt_system = get_system_prompt()

message_system = {
        "role" : "system",
        "content" : prompt_system,
    }

def llm_ques():

    messages = [message_system]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"}
    )
    ans = response.choices[0].message.content
    try:
        validated_ans = llmOutputSchema.model_validate_json(ans)
        return validated_ans.output_list  # Changed from output_text to output_list
    except ValidationError:
        return "Sorry, I had trouble generating a response. Please try again."