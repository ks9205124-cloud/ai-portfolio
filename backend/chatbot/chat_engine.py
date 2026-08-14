from chatbot.llm_client import llm_ans
from chatbot.question_generator import llm_ques

def chat(user_message: str) -> str:
    return llm_ans(user_message)

def question() :
    return llm_ques()
