import whisper
# import imageio_ffmpeg
import openai
from gtts import gTTS
from dotenv import load_dotenv
import speech_recognition as sr
import os


# os.environ["PATH"] += os.pathsep + os.path.dirname(imageio_ffmpeg.get_ffmpeg_exe())
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# # def to_text():
# #     with open("question_audio.wav","rb") as audio:
# #         text = openai.audio.transcriptions.create(
# #             model="whisper-1",
# #             file=audio
# #         )
# #         print(text.text)
# #         return text.text

recognizer = sr.Recognizer()

def to_text():
    with sr.AudioFile("./answer_audio.wav") as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    print("Text:", text)

to_text()
    
# to_text()
# def to_text():
#     model = whisper.load_model("base")
#     resp = model.transcribe("./question_audio.wav")
#     print(resp["text"])
#     return resp["text"]
    
# to_text()

# def to_audio(text):
#     tts = gTTS(text)
#     question_audio = "answer_audio.wav"
#     tts.save(question_audio)
#     return question_audio