ext():
    model = whisper.load_model("base")
    resp = model.transcribe("./question_audio.wav")
    print(resp["text"])
    return resp["text"]