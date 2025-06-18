# import whisper
import openai
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def to_text():
    with open("question_audio.wav","rb") as audio:
        text = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        print(text.text)
        return text.text
    

def to_audio(text):
    tts = gTTS(text)
    question_audio = "answer_audio.wav"
    tts.save(question_audio)
    return question_audio