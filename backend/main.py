from fastapi import  FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import app.convert_audio_video as cav
import unicodedata
from app.ask_bot import ask_bot
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
# app.mount("/", StaticFiles(directory="dist", html=True), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["asked_question"],
)

@app.post("/talk")
async def ask_question(audio : UploadFile = File(...)):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",audio)
    with open("question_audio1.wav","wb") as f:
        f.write(await audio.read())

    question = cav.to_text()
    print("converted to text")
    resp = ask_bot(question)
    print("got ans") 
    output_audio = cav.to_audio(resp)
    print("converted to audio")
    question = unicodedata.normalize("NFKD", question  ).encode("ascii", "ignore").decode("ascii")
    headers = {"asked_question": question}
    return FileResponse(output_audio,media_type="audio/wav", headers=headers)