from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.llm import llm

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bondi Bot está vivo 🚍"}

class Message(BaseModel):
    query: str

@app.post("/ask")
def ask(message: Message):
    response = llm.invoke(message.query)
    return {"response": response.content}

@app.post("/ask-stream")
async def ask_stream(message: Message, request: Request):
    async def token_generator():
        for chunk in llm.stream(message.query):
            if await request.is_disconnected():
                break
            yield chunk.content or ""
    
    return StreamingResponse(token_generator(), media_type="text/plain")
