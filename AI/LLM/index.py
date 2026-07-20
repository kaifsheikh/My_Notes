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

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # thoda bada chunk, better context
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(documents)

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
            {
            "role": "system",
            "content": SYSTEM_PROMPT
            },
            
            {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
            }
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