
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm_integration import LLMIntegration


import logging

app = FastAPI()

# Initialize the LLM integration
llm_integration = LLMIntegration()

class MessageRequest(BaseModel):
    user_message: str

class MessageResponse(BaseModel):
    ai_response: str

@app.post("/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    try:
        ai_response = await llm_integration.get_response(request.user_message)
        return MessageResponse(ai_response=ai_response)
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    