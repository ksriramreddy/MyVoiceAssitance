import faiss
import pickle
import os
import openai
import google.generativeai as genai
from PyPDF2 import PdfReader
import numpy as np
from dotenv import load_dotenv
import cohere

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.embed_content
# faiss_index = faiss.IndexFlatL2(1536)#for open ai embeddings dimensions
# faiss_index = faiss.IndexFlatL2(768) #for GEMINI embeddings dimensios
faiss_index = faiss.IndexFlatL2(1024) # for cohere embeddings  dimensions

co = cohere.Client(os.getenv("COHERE_API_KEY"))



docs =[]
embeddings =  []

for file in os.listdir("./data"):
    file_path = os.path.join("./data",file)
    text = ""
    if file.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    chunks = []
    for i in range(0 , len(text) , 450):
        chunks.append(text[i:i+500])
    docs.extend(chunks)
    
    for chunk in chunks:
        #------------------OPEN AI Embeddings----------------------------
        # resp = openai.embeddings.create( # this is for OPEN AI Embedding which need credits
        #     model="text-embedding-3-small",
        #     input=chunk
        # )
        # -----------------GEMINI Embeddings------------------------------
        # resp = model(
        #     model = "models/embedding-001",
        #     content = chunk, 
        #     task_type="retrieval_document"
        # )
        #-------------------COHERE Embeddings-----------------------------
        resp = co.embed(
            texts = [chunk],
            model = "embed-english-v3.0",
            input_type="search_document"
        )
        print(resp)
        # embeddings.append(resp['embedding']) # for GEMINI response
        embeddings.append(resp.embeddings[0]) # for COHERE resp
faiss_index.add(np.array(embeddings).astype("float32"))
faiss.write_index(faiss_index,"./vector_database/faiss.index")

with open("./vector_database/docs.pkl", "wb") as f:
    pickle.dump(docs, f)
