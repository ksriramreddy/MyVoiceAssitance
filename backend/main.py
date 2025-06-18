from fastapi import  FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import app.convert_audio_video as cav
from app.ask_bot import ask_bot

app = FastAPI()
app.mount("/", StaticFiles(directory="dist", html=True), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myvoiceassitance-3.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/talk")
async def ask_question(audio : UploadFile = File(...)):
    with open("question_audio.wav","wb") as f:
        f.write(await audio.read())

    question = cav.to_text()
    resp = ask_bot(question)
    print("got ans")
    output_audio = cav.to_audio(resp)
    print("converted to audio")
    return FileResponse(output_audio,media_type="audio/wav")