import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import ValidationError

from chatbot.prompts.prompts import get_system_prompt
from chatbot.schemas.schemas import UserOutputSchema
from chatbot.history import add_user_message, add_assistant_message, get_history, trim_history

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

prompt_system = get_system_prompt()

message_system = {
        "role" : "system",
        "content" : prompt_system,
    }

def llm_ans(prompt_user):
    add_user_message(prompt_user)

    messages = [message_system] + get_history()

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"}
    )
    ans = response.choices[0].message.content
    try:
        validated_ans = UserOutputSchema.model_validate_json(ans)
        add_assistant_message(validated_ans.output_text)
        trim_history()
        return validated_ans.output_text
    except ValidationError:
        return "Sorry, I had trouble generating a response. Please try again."

