# What is `RAG`
1. RAG `(Retrieval-Augmented Generation)`

2. Jab aap GPT yeah kisi bhe AI se direct Chat karte hai, to wo apni general knowledge (jo usne internet se seekhi hai) waha se jawab deta hai.

3. Lekin RAG mein hum pehle apne private documents mein se sawaal se related chunks retrieve karte hain, phir un chunks ko sawaal ke saath LLM ko dete hain taaki wo context ke saath accurate jawab generate kare.

# Rag depends on 4 things:

| Features | Explain |
| -------- | -------- |
| **Documents** | humera personal data like pdf, doc or etc |
| **Document Loader / Parser** | Ek tool yeah library jo PDF, DOCX, CSV, HTML, etc. ko read karke unka raw text ko extract kar leta hai. |
| **Text Splitter** | Bade document ko chhote‑chhote tukdon (chunks) mein todne ka logic. |
| **Embedding Model** |  Aisa AI model jo text ko numbers **vectors** **floats** ki **list** mein badal deta hai. Ye vectors text ka "matlab" **represent** karte hain. |
| **Vector database** | Special database jo vectors (embeddings) ko store karta hai aur bahut tezi se similarity search (nearest neighbour) karta hai. |
| **Reranker** `Optional` | Ek chhota model jo retrieved chunks ko dubara score karta hai ki woh sawaal ke liye kitne relevant hain, aur final order set karta hai. |
| **LLM (Groq)** | context ke saath final jawab banayega. |
| **Prompt Template & Engineering** | Wo instruction set jo tum LLM ko dete ho ki "tumhari role kya hai, context kahan hai, kya karna hai, kya nahi karna. |

---

# Pakcages Installation:

```bash
pip install groq 
pip install chromadb
pip install sentence-transformers
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install pypdf
pip install python-dotenv
```

# Example 01:



```py
import os, shutil
from dotenv import load_dotenv
from groq import Groq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder

# ========== 1. LOAD & SPLIT (SAME) ==========
loader = TextLoader("data/story.txt", encoding="utf-8")
documents = loader.load()
print(f"Total pages loaded: {len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # thoda bada chunk, better context
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(documents)
print(f"Total chunks ban gaye: {len(chunks)}")

# ========== 2. BETTER EMBEDDING MODEL ==========
embedding_model_name = "BAAI/bge-small-en-v1.5"
embedding_function = HuggingFaceEmbeddings(
    model_name=embedding_model_name,
    model_kwargs={"device": "cpu"},    # "cuda" agar GPU ho
    encode_kwargs={"normalize_embeddings": True}
)

# ========== 3. VECTOR STORE (naye model ke saath) ==========
persist_directory = "./chroma_ai"
# Purana store hatao taaki naye embeddings create hon
if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_function,
    persist_directory=persist_directory
)
vectordb.persist()
print("Vector store save ho gaya.")

# ========== 4. RETRIEVER WITH MORE CHUNKS ==========
retriever = vectordb.as_retriever(search_kwargs={"k": 10})  # pehle 10 chunks laao

# ========== 5. CROSS-ENCODER RE-RANKER ==========
reranker_model = CrossEncoder("BAAI/bge-reranker-base")   # free, local
# ye model (query, chunk) pair ko score karega
def rerank_chunks(query, docs, top_n=3):
    if not docs:
        return []
    pairs = [(query, doc.page_content) for doc in docs]
    scores = reranker_model.predict(pairs)
    # score ke hisaab se sort karo
    sorted_pairs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in sorted_pairs[:top_n]]

# ========== 6. GROQ LLM ==========
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

SYSTEM_PROMPT = (
    "You are a precise assistant. Answer the user's question using ONLY the provided context. "
    "If the context does not contain the answer, say: 'Mujhe is sawaal ka jawab diye gaye documents mein nahi mila.' "
    "Do not make up anything. Keep it concise."
)

def ask_question(question: str) -> str:
    # 1. Retrieve 10 chunks
    raw_docs = retriever.invoke(question)
    if not raw_docs:
        return "Koi relevant document nahi mila."
    # 2. Re-rank to top 3
    top_docs = rerank_chunks(question, raw_docs, top_n=3)
    # 3. Context banao
    context = "\n\n".join(doc.page_content for doc in top_docs)
    # 4. Groq se jawab
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"}
        ],
        temperature=0.0,
        max_tokens=500,
    )
    return response.choices[0].message.content.strip()

# ========== 7. INTERACTIVE LOOP ==========
print("\n✅ Professional RAG System ready! (exit likhne par band hoga)\n")
while True:
    q = input("🧑 Aap: ")
    if q.lower() in ("exit", "quit"):
        break
    try:
        answer = ask_question(q)
        print(f"🤖 Bot: {answer}\n")
    except Exception as e:
        print(f"⚠️ Error: {e}")
```

# Packages:

## 📦 `import os, shutil`
- **os** → Files aur folders ko check karne or oisa overall manage karta hai.

---

## 📦 `from dotenv import load_dotenv`
- `.env` file se **Groq API key** load karta hai, taaki wo code mein openly na likhni pade. Security aur neatness ke liye.

---

### 📦 `from groq import Groq`
- **Groq API client** – yahi wo LLM hai jo sawaal ka final jawab generate karta hai (jaise llama3, mixtral), context ke saath. Tumhara brain of the RAG.

---

### 📦 `from langchain_community.document_loaders import TextLoader`
- **TextLoader** → Tumhari `.txt` file ko padhkar usmein se raw text nikalta hai. Yhi tumhara **Document Loader** hai.

---

## 📦 `from langchain_text_splitters import RecursiveCharacterTextSplitter`
- **Text Splitter** – bade document ko chhote‑chhote tukdon (chunks) mein todta hai, taaki embedding aur search asaan ho. Tumhara chunking logic.

---

## 📦 `from langchain_community.vectorstores import Chroma`
- **Chroma** → Vector database. Ye chunks ke embeddings ko store karta hai aur sawaal ke embedding ke saath similarity search karta hai.

---

## 📦 `from langchain_community.embeddings import HuggingFaceEmbeddings`
- **Embedding Model** – ye kisi bhi text (chunk ya sawaal) ko numbers ki list (vector) mein badalta hai. Yhi `sentence-transformers` model ko load karta hai.

---

## 📦 `from sentence_transformers import CrossEncoder`
- **Re‑ranker** – ye ek chhota advanced model hai jo (sawaal + chunk) dono ko saath padhkar **relevance score** deta hai. Retrieval ke baad top-10 mein se sirf 3 best chunks chun leta hai 

---

# Explanation:

1. Hum `RecursiveCharacterTextSplitter` class ka ek **object** banaya hai.
2. jiska naam rekha hai **text_splitter**.
3. Iske andar **3** important **settings** de rahe hain:

4. `chunk_size=800`:
    - Har chunk ki maximum length 800 characters hogi.
    - Characters matlab **letters**, **spaces**, **newlines** sab count hote hain (jaise A, B, space, . etc.).
    - Kyon 800? — Ek typical LLM context mein 500‑1000 character ka chunk fit hota hai, embedding model bhi itne mein accha perform karta hai. Na chhota ki context toote, na bada ki search slow ho.

## Example:
```py
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("data/ai.pdf")
documents = loader.load()

print(f"Total pages loaded: {len(documents)}")

# ========== TEXT SPLITTER CONFIGURATION ==========

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=36,  
    chunk_overlap=3,     
    separators=["\n\n", "\n", " ", ""]   
)

# Documents (pages) ko chunks mein baat do
chunks = text_splitter.split_documents(documents)

print(f"Total chunks ban gaye: {len(chunks)}")

``` 
| Chunk | How | Result |
| -------- | -------- | -------- |
| Chunk‑1 | Pehle 15 characters (indices 0–14) liye gaye | `ABCDEFGHIJKLMNO` |
| Chunk‑2 | Overlap = `Chunk‑1` ke aakhri `3 characters` = MNO Ab MNO ke aage next 12 characters (P se lekar 0 tak) jode → total 15 | `MNOPQRSTUVWXYZ01` |
| Chunk‑3 | Overlap = Chunk‑2 ke aakhri `3 characters` = Z01 Ab Z01 ke aage baaki bache 7 characters (23456789) jode → total 10 (kyunki text khatam ho gaya, 15 se kam bhi chalega) | `Z0123456789` |

- total **Characters** **``36``**
- or total **Chunks** **`3`** hai