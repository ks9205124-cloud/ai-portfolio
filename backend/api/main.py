from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import chat
app = FastAPI()

app.include_router(chat.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)