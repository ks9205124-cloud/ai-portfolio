from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class SuggestedQuestionsResponse(BaseModel):
    questions: List[str]