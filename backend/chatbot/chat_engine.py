from llm_client import llm_ans
from question_generator import llm_ques
from time import sleep
def chat(user_message: str) -> str:
    return llm_ans(user_message)

def question() :
    return llm_ques()

print(chat("tell me about the candidate"))

sleep(2)
ques1 = question()[0]

print(ques1)
print((chat(ques1)))

sleep(2)
ques2 = question()[1]

print(ques2)
print((chat(ques2)))

sleep(2)
ques3 = question()[0]

print(ques3)
print((chat(ques1)))

sleep(2)

print("that is all i wanted to ask about user")
print((chat("that is all i wanted to ask about user")))