# 🎙️ Sriram Voice Assistant 🤖 – RAG-Based Voice Bot with PDF/Info Retrieval

This is a voice-based assistant powered by **OpenAI**, **FAISS vector database**, and a beautiful **React + Tailwind** frontend. It allows users to speak naturally, sends the audio to a backend, transcribes it, searches over personal documents, and responds back with generated answers – as voice!

---

## 🛠 Tech Stack 👨‍💻

**Frontend:** React.js, Tailwind CSS, Framer Motion, Axios  
**Backend:** FastAPI, OpenAI, FAISS, Python  
**Audio:** Whisper/OpenAI Speech-to-Text, gTTS / OpenAI Text-to-Speech  
**RAG (Retrieval-Augmented Generation):** FAISS + OpenAI Embeddings

---

## Wanna Clone It 🖨️

**1. Clone the Project via Link**
[Follow this](https://github.com/ksriramreddy/MyVoiceAssitance.git)

**2. Follow the Folder Structure Below 👇👇**
[Follow this](https://github.com/ksriramreddy/MyVoiceAssitance.git)
---

## 📂 Folder Structure

```bash

#This are the file you need to update in order to make your OWN AI ASSISTANT

MyVoiceAssistant/
│
├── frontend/                # React client
│   └── src/pages/Home.jsx   # Main voice assistant UI
│   └──.env                  # You backend deployed server link or localhost:8000/
│
├── backend/
│   ├── app/
│   │   ├── ask_bot.py       # RAG + LLM logic
│   │   ├── audio_utils.py   # Audio handling (TTS/STT)
│   │   └── vectordb.py      # Embedding + FAISS index builder
│   ├── vector_database/
│   │   ├── faiss.index      # FAISS index file
│   │   └── docs.pkl         # Chunked documents for search
│   ├── data/                # Place your PDF or text files here
│   ├── main.py              # FastAPI main server
│   └── .env                 # Add your OpenAI API key here
```

**3. Code Updates ✍️📝**

*3.1* Change the information in the `backend/data` you can add more text file.

*3.2* Run the `backend/app/vectordb.py` to ubdate the `fAISS` indices

*3.3* Make sure to add you `OPEN AI` API key in the `.env` file as `OPENAI_API_KEY`

*3.4* Add `VITE_BACKEND_API  = http://localhost:800` in `frontend/.env`

**4. Test Run 🧑‍🔬🧪**

``` bash


#for backend 
#open new terminal
cd backend
python -m venv new_env #create an new virtual env
pip install -r reqirements.txt #install all required packages
uvicorn main:app --reload # Run the backend Server

#for Frontend
#open new terminal

cd frontend
npm install # install all dependencies
npm run dev #start the server

```

**5. Deploy🚀**

*5.1* User any service provider like `vercel` or `render` to deploy you voice assistance

*5.2* If your deploying individually make sure to ass your backend api to your frontend

**6. Facing Trouble ❌**

Mail me here `k.sriramreddy9@gmail.com`
[LinkedIn](https://www.linkedin.com/in/sriram-reddy-34905a212/)
[Instagram](https://www.instagram.com/kothireddysriram/)