from fastapi import APIRouter
from chatbot.chat_engine import chat , question
from api.schemas import UserQuestion

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
async def get_chat(payload: UserQuestion):
    # Fixed: Return a proper dictionary for FastAPI JSON serialization
    return {"response": chat(payload.message)}

@router.get("/question")
async def post_chat():
    return {"status": question()}