from fastapi import FastAPI
from pydantic import BaseModel

from services.email_generator import generate_email

app = FastAPI(
    title="AI Email Assistant API"
)


class EmailRequest(BaseModel):
    prompt: str
    tone: str


@app.get("/")
def home():
    return {
        "message": "AI Email Assistant API Running"
    }


@app.post("/generate")
def generate(data: EmailRequest):

    try:

        email = generate_email(
            data.prompt,
            data.tone
        )

        return {
            "status": "success",
            "tone": data.tone,
            "generated_email": email
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }