
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .password_generator import generate_password

app = FastAPI()

class PasswordRequest(BaseModel):
    length: int

@app.post("/generate-password")
async def generate_password_endpoint(password_request: PasswordRequest):
    if password_request.length <= 0:
        raise HTTPException(status_code=400, detail="Length should be a positive integer")
    
    password = generate_password(password_request.length)
    return {"password": password, "length": len(password)}
