# What is `RAG`
1. RAG `(Retrieval-Augmented Generation)`

2. Jab aap GPT yeah kisi bhe AI se direct Chat karte hai, to wo apni general knowledge (jo usne internet se seekhi hai) waha se jawab deta hai.

3. Lekin RAG mein hum pehle apne private documents mein se sawaal se related chunks retrieve karte hain, phir un chunks ko sawaal ke saath LLM ko dete hain taaki wo context ke saath accurate jawab generate kare.

# Rag depends on 4 things:

1. **Documents** → humera personal data like pdf, doc or etc
2. **Document Loader / Parser** → Ek tool yeah library jo PDF, DOCX, CSV, HTML, etc. ko read karke unka raw text ko extract kar leta hai.
3. **Text Splitter** Bade document ko chhote‑chhote tukdon (chunks) mein todne ka logic. 
4. **Embedding Model** Aisa AI model jo text ko numbers **vectors** **floats** ki **list** mein badal deta hai. Ye vectors text ka "matlab" **represent** karte hain.
5. **Vector database** → Special database jo vectors (embeddings) ko store karta hai aur bahut tezi se similarity search (nearest neighbour) karta hai.
6. **Reranker Optional** Ek chhota model jo retrieved chunks ko dubara score karta hai ki woh sawaal ke liye kitne relevant hain, aur final order set karta hai.
7. **LLM (Groq)** → context ke saath final jawab banayega.
8. **Prompt Template & Engineering** Wo instruction set jo tum LLM ko dete ho ki "tumhari role kya hai, context kahan hai, kya karna hai, kya nahi karna".

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
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("data/ai.pdf")
documents = loader.load()

print(f"Total pages loaded: {len(documents)}")

# ========== TEXT SPLITTER CONFIGURATION ==========

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,  
    chunk_overlap=150,     
    separators=["\n\n", "\n", " ", ""]   
)

# Documents (pages) ko chunks mein baat do
chunks = text_splitter.split_documents(documents)

print(f"Total chunks ban gaye: {len(chunks)}")
```

# Explanation:

1. Hum `RecursiveCharacterTextSplitter` class ka ek **object** banaya hai.
2. jiska naam rekha hai **text_splitter**.
3. Iske andar **3** important **settings** de rahe hain:

    - `chunk_size=800` Har chunk ki maximum length 800 characters hogi.
    - Characters matlab **letters**, **spaces**, **newlines** sab count hote hain (jaise A, B, space, . etc.).
    - Kyon 800? — Ek typical LLM context mein 500‑1000 character ka chunk fit hota hai, embedding model bhi itne mein accha perform karta hai. Na chhota ki context toote, na bada ki search slow ho.

## Example:

1. hello word, this is the sample text. -> total chars **``36``** hai
    - h(0), e(1), l(2), l(3), o(4), space(5), w(6), o(7), r(8), d(9) → **chunk1** = **hello wor** (10 chars).
    
2. chunk_overlap = 3 -> means ka last ka **3** chars **overlap** hoga like 

```py
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,  
    chunk_overlap=150,     
    separators=["\n\n", "\n", " ", ""]   
)
```