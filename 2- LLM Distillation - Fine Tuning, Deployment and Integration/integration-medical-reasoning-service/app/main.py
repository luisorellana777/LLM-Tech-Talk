from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.service import get_diagnosis

app = FastAPI()

class PromptRequest(BaseModel):
    question: str

@app.post("/medical-diagnosis")
def generate_medical_diagnosis(request: PromptRequest):

    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Prompt must not be empty")
    diagnosis = get_diagnosis(question)
    return {"diagnosis": diagnosis}