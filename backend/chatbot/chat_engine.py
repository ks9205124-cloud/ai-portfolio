from llm_client import llm_ans
from question_generator import llm_ques
from time import sleep
def chat(user_message: str) -> str:
    return llm_ans(user_message)

def question() :
    return llm_ques()
