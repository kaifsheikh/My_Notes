# What is LangGraph:
1. LangGraph Python ka ek modern framework hai, lekin yeh LangChain ka hi banaya hua extension/child ecosystem hai.
2. Jab aapke paas bohot saare tools ho jayein, toh AI bhatak sakta hai. tu LangGraph AI ko ek step-by-step rasta (Flow Chart) deta hai ke kis waqt kaun sa tool chala kar kahan jana hai.
3. Yeh AI ka Work Planner hai Agar AI se koi galti ho jaye, toh LangGraph usay batata hai: "Pehle step 1 par wapis jao, galti theek karo, aur phir step 2 par aao."

# Purpose:
1. **Cyclic Workflows:** Normal AI pipelines seedhi (Linear) hoti hain (Step A -> Step B -> End).
LangGraph aapko Loops banane ki ijazat deta hai (Step A -> Step B -> Check Result -> Agar Galat Hai To Wapas Step A).
2. **State Management**: Har AI agent ka ek **Brain State** hota hai. User ne kya poocha? Konsa tool run hua? Tool ka kya output aaya? Is saari maloomat ko **State** kehte hain. LangGraph is state ko har step par track aur update karta hai.
3. **Human-in-the-Loop:** Agar aapka agent koi sensitive kaam karne laga hai (jaise koi file delete karna ya email bhejna), toh LangGraph agent ko rok kar aap se approval maang sakta hai.
4. **Agentic AI:** smart AI agents ka flow, state (memory), aur decision-making process control karna hai.

---

LangGraph aur Agentic AI ko ache se samajhne aur master karne ke liye aapko step-by-step in **6 core concepts** ko seekhna hoga:

**1. State (Central Memory / Data Container)**
* [State Managment](state_management_02.md)

**2. Nodes (Execution Units / Workers)**

* **Kya Hai:** Nodes basically simple Python functions hote hain. Standard pattern mein ek Node LLM hota hai aur doosra Node Tools ka hota hai.
* **Kyun Seekhna Hai:** Aap apne agent ka har step (jaise file system check karna, code run karna, API call karna) alag node ke andar likhte hain.

**3. Edges & Conditional Edges (Traffic Control / Routing)**

* **Kya Hai:**
* **Normal Edges:** Ek node ke khatam hone par agle node ka rasta (e.g., Node A $\rightarrow$ Node B).
* **Conditional Edges:** Logic-based routing (`if/else`). Agar LLM ko lagta hai ke tool ki zaroorat hai toh Tools Node par bhejo, warna direct `END` kar do.


* **Kyun Seekhna Hai:** Yeh aapke agent ke decision-making power aur loops ko control karta hai.

**4. Checkpointers & Memory (Persistence)**

* **Kya Hai:**
* **In-Memory (`MemorySaver`):** Chat context ko RAM mein temporary save karna (jaisa abhi hum discuss kar rahe the).
* **Persistent DB Checkpointers (`SqliteSaver`, `PostgresSaver`):** Script band hone ke baad bhi conversation record database mein save rakhna.


* **Kyun Seekhna Hai:** Is se aapka agent multi-turn conversation yaad rakh sakta hai aur "Time-Travel" (purane state par wapas jana) kar sakta hai.

**5. Tools Integration (`@tool` Decorator)**

* **Kya Hai:** Python functions ko AI-readable format mein convert karna jisse LLM apne hisaab se call kar sake.
* **Kyun Seekhna Hai:** Files read/write karna, system commands execute karna, ya databases ke sath interact karne ke liye tools ka structure samajhna zaroori hai.

**6. Human-in-the-Loop (Approval System)**

* **Kya Hai:** Agent ke kisi critical node (jaise file delete karne ya terminal command execute karne) se pehle execution ko pauce kar ke human se "Yes/No" approval lena.
* **Kyun Seekhna Hai:** System safety aur unauthorized actions ko rokne ke liye yeh sabse important security feature hai.

---

### Suggested Learning Path

| Step | Topic | Objective |
| --- | --- | --- |
| **1** | **State & Nodes** | Simple custom Graph banana sikhna. |
| **2** | **Conditional Edges** | Logic-based routing aur Loops chalana. |
| **3** | **Checkpointer & Thread ID** | Chat memory aur multi-user sessions add karna. |
| **4** | **Human-in-the-Loop** | Dangerous tools ke liye approval check lagana. |
