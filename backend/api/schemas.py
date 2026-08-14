from pydantic import BaseModel

class UserQuestion(BaseModel):
    message: str

class ChatBotResponseQuestion(BaseModel):
    question: list