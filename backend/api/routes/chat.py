from fastapi import APIRouter
from chatbot.chat_engine import chat, question
from api.schemas import ChatRequest, ChatResponse, SuggestedQuestionsResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
async def get_chat(payload: ChatRequest):
    answer = chat(payload.message)
    return ChatResponse(response=answer)


@router.get("/", response_model=SuggestedQuestionsResponse)
async def get_suggested_questions():
    res = question()

    if isinstance(res, dict):
        questions_list = res.get("output_list", [])
    elif hasattr(res, "output_list"):
        questions_list = res.output_list
    else:
        questions_list = res

    return SuggestedQuestionsResponse(questions=questions_list)