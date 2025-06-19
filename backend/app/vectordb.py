import faiss
import pickle
import os
import openai
from PyPDF2 import PdfReader
import numpy as np
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

faiss_index = faiss.IndexFlatL2(1536)

docs =[]
embeddings =  []

for file in os.listdir("backend/data"):
    file_path = os.path.join("backend/data",file)
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
        resp = openai.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(resp.data[0].embedding)
faiss_index.add(np.array(embeddings).astype("float32"))
faiss.write_index(faiss_index,"backend/vector_database/faiss.index")

with open("backend/vector_database/docs.pkl", "wb") as f:
    pickle.dump(docs, f)
