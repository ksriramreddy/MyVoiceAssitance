import pickle
import os 
import faiss
import openai
import numpy as np
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

faiss_index = faiss.read_index("vector_database/faiss.index")

with open("vector_database/docs.pkl","rb") as f:
    docs = pickle.load(f)

def ask_bot(question):
    question_propt = f"""
            Given the following Question, generate 5 different versions of questions that convey the same meaning but use different wording, sentence structures, and vocabulary. Each version should retain the original intent and clarity while sounding natural and professional.

            Question : {question}
        """
    new_questions = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":question_propt}],
        temperature=0.2
    )
    question = new_questions.choices[0].message.content
    print(question)
    resp = openai.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )
    embeddings = resp.data[0].embedding
    question_embd = np.array([embeddings]).astype("float32")
    # print(question_embd)
    _, idx  = faiss_index.search(question_embd , k = 4)

    answer = "\n\n".join([docs[i] for i in idx[0]])

    prompt = f"""
    You are a voice assitance who knows averythig about Sriram,
    Use this following Context and answer the given question.
    the replay should more like human.
    if the Context inopproprite to question just reply with:
    "I Dont have awareness to that question right now"
    Rules : 

    1. always use I am, me , mine in the place Sriram Reddy , like your talking in behalf of me 
    2. never use based on the context provided
    3. responce politly and respectfully like adding greetings and thank you
    4. The generated answer should fell like human emotions
    5. Give me only one best answer by combinig all
    Context : {answer}
    question : {question}
    """
    resp = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )
    # print(resp)
    # print(resp.choices[0]["message"]["content"])
    return resp.choices[0].message.content
