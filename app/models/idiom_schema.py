from pydantic import BaseModel

# Data model for the incoming request from Swift
class IdiomRequest(BaseModel):
    idiom: str

# Data model for the outgoing response to Swift
class IdiomResponse(BaseModel):
    explanation: str