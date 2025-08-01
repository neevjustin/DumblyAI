from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load .env file for GEMINI_API_KEY
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up model correctly
model = genai.GenerativeModel("models/gemini-2.5-flash")

# FastAPI app setup
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/respond")
async def respond(request: Request):
    body = await request.json()
    user_prompt = body.get("prompt", "")

    if not user_prompt.strip():
        return {"answer": "Even I know nothing means nothing."}

    base_prompt = (
        "You are a chatbot that gives confidently incorrect answers. "
        "Always respond like you know everything  — but provide answers that are clearly false, ridiculous, or absurd."
        "Dont provide long answers. Try to be short as possible"
        "You are lazy dumb absurd but confidently wrong"
        "Dont be satire. give completely wrong answer"
        
    )

    full_prompt = f"{base_prompt}\n\nUser asked: {user_prompt}"

    try:
        chat = model.start_chat(history=[])
        result = chat.send_message(full_prompt)
        answer = result.text
    except Exception as e:
        answer = f"Oops, I got confused: {str(e)}"

    return {"answer": answer}

@app.get("/ping")
def ping():
    return {"status": "alive"}

