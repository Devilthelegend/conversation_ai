
from pydantic import BaseModel

# Define the request and response models
class MessageRequest(BaseModel):
    user_message: str

class MessageResponse(BaseModel):
    ai_response: str
    