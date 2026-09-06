# What is LangChain?
1. LangChain ek open-source framework hai jo LLMs jaise AI models ko tools, data, aur external systems se connect karne ki permission deta hai taake wo real-world jaise kam ko bhe easily kar sekhe.
2. AI Models sirf Data ki base per Train hote lakin Current situation nhe bta sekhte hai tu is problem ko dour karta hai lainchain.
3. LangChain ek **bridge** hai jo **AI aur aapke computer programs, websites, databases, Excel files, APIs** ke beech kaam karwata hai 

LangChain ko samajhne ke liye iske saare core modules aur concepts ko **6 main pillars** mein divide kiya jata hai. Un sab ki tafseel aasan Roman Urdu mein neeche maujood hai:

---

## **1. Model Input & Output**

* AI Model ko Input dena means (Prompts) aur usse Sahi Format mein Output lena (Parsers).
* is ke andar 3 main cheezein hoti hain jo mil kar kaam karti hain:
    - Prompt Engineering
    - Model 
    - Output Parsers 

* **Chat Models & LLMs:** Groq, OpenAI, ya Anthropic ke models ko Python ke sath connect karna (e.g., `ChatGroq`, `ChatOpenAI`).
* **Prompt Templates:** Static prompts ke bajaye dynamic user inputs add karne ke liye formats banana (e.g., `ChatPromptTemplate`, `SystemMessage`, `HumanMessage`).
* **Output Parsers:** AI ke raw text answer ko structured data (JSON, Python List, ya Dictionary) mein convert karna.

---

### **2. Tools & Tool Calling**

AI Model ko sirf baatein karne se rok kar real-world tasks perform karne ki taqat dena.

* **`@tool` Decorator:** Simple Python functions ko AI Tools mein wrap karna taake model unhein zarurat ke waqt execute kar sake.
* **Tool Schemas & Type Hints:** Model ko yeh batana ke function kya kaam karta hai aur usme konse parameters (`str`, `int`) chahiye.
* **Structured Tools:** Complex inputs (multiparams) wale tools banana (using `Pydantic`).

---

### **3. Chains (Execution Flows)**

Mukhtalif components (Prompts + Models + Parsers) ko ek sequence mein jorna.

* **LCEL (LangChain Expression Language):** Pipe operator (`|`) ka istemal karke clean code likhna (e.g., `chain = prompt | model | parser`).
* **Sequential Chains:** Ek step ka output doosre step ke input mein pass karna.
* **Runnable Protocol:** Chains ko asynchronous (`ainvoke`), streaming (`astream`), ya batch processing ke liye execution options dena.

---

### **4. Memory & Context Management**

Conversations ke context aur history ko manage karna taake AI purani baatein na bhoole.

* **Chat History Managers:** Messages ko list format mein manage karna (`ChatMessageHistory`).
* **Message Trimming (`trim_messages`):** Token limit se bachne ke liye purani history ko trim/crop karna.
* **Memory Summarizers:** Lambi chats ko chota kar ke unka summary context mein rakhna.

---

### **5. Retrieval & RAG (Data Connections)**

Apne private documents (PDFs, Databases, Text files) ko AI ke sath connect karna.

* **Document Loaders:** Mukhtalif file formats (PDF, CSV, HTML, TXT) se data read karna.
* **Text Splitters:** Bade documents ko chote pieces (chunks) mein todna.
* **Embedding Models:** Text chunks ke maani (semantics) ko mathematical numbers (vectors) mein convert karna.
* **Vector Stores (Databases):** Embeddings ko Chroma, Pinecone, ya FAISS mein save karna aur relevant data search karna (Retrieval).

---

### **6. Agents & Tool Execution**

Autonomous decision-making system banana jahan AI khud decide karta hai ke kaun sa tool kab chalana hai.

* **Agent Engines:** React / Tool calling logic jo LLM ko plan banane aur loop mein execute karne mein madad karta hai.
* **Agent Executors:** Agent ki execution ko control karna aur errors ko gracefully handle karna.

---

### **Summary Table**

| Component | Main Purpose | Core Example |
| --- | --- | --- |
| **Model I/O** | Model Connection & Prompts | `ChatPromptTemplate`, `ChatGroq` |
| **Tools** | External Functions Access | `@tool`, `Pydantic` |
| **Chains (LCEL)** | Steps linking | `prompt | model | parser` |
| **Memory** | History Management | `trim_messages`, `ChatMessageHistory` |
| **Retrieval (RAG)** | Private Documents QA | `TextSplitters`, `VectorStores` |
| **Agents** | Autonomous Execution | `create_tool_calling_agent` |

# What is LangGraph:
1. LangGraph ek alag framework (library) hai, lekin yeh LangChain ka hi banaya hua extension/child ecosystem hai.
1. Jab aapke paas bohot saare tools ho jayein, toh AI bhatak sakta hai. LangGraph AI ko ek step-by-step rasta (Flow Chart) deta hai ke kis waqt kaun sa tool chala kar kahan jana hai.
2. Yeh AI ka Work Plan / Mind Map hai. Agar AI se koi galti ho jaye, toh LangGraph usay batata hai: "Pehle step 1 par wapis jao, galti theek karo, aur phir step 2 par aao."