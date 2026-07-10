# What is Ollama:
1. Ollama ek tool / platform hai jo hume LLMs ko locally run karne deta hai apne system mein bina internet ke.
2. isa hum apne computers par open source AI model run kar sekhte ha easily Ollama khud LLM nahe hai yeh LLMs ko run karne ka environment hai.
3. hum isme open-weight models download karke use kar sekhte ha.

## ***Important Commands for Ollama***

| Command | Category | Maqsad (Purpose) | Kab Istemal Karein? |
| --- | --- | --- | --- |
| **`ollama run [model_naam]`** | Main | Model download + Chat shuru karna. | Jab aap foran AI se baat karna chahen. |
| **`ollama pull [model_naam]`** | Download | Sirf model download karna (Chat nahi). | Slow internet par ya sirf download ke liye. |
| **`ollama list`** | Management | Downloaded models ki list dekhna. | Jab check karna ho ke F: drive mein kya kya hai. |
| **`ollama rm [model_naam]`** | Delete | Model ko disk se khatam/delete karna. | Jab space khatam ho rahi ho aur model na chahiye ho. |
| **`ollama ps`** | Monitor | Dekhna ke kaunsa model is waqt RAM mein chal raha hai. | Jab computer slow ho raha ho aur check karna ho. |
| **`ollama show [model_naam]`** | Info | Model ki mukammal detail dekhna. | Jab model ke parameters ya license check karna ho. |
| **`ollama serve`** | Service | Ollama ki background service start karna. | Agar Ollama ka icon taskbar mein nazar na aaye. |
| **`/bye`** | Chat | Chat se bahar nikalna (Exit). | Jab AI se baat khatam ho jaye aur CMD par wapis aana ho. |
| **`/set verbose`** | Chat | Jawab ki speed aur time (stats) dekhna. | Jab check karna ho ke AI kitna fast jawab de raha hai. |

---

# Full Installation Agentic AI:

1. first download **ollama** locally in your system
2. oiske bad **ollama pull qwen2.5:3b** yeah aik agentic model hai jo publically free hai.
3. phir **nodejs** downlaod karne hai openclaw ka liya kue ka wo nodejs per run hota hai
4. oiske bad cmd per yeah command run karne hai **npm install -g openclaw@latest**
5. oiske bad yeah cmd likhne hai **npm approve-scripts --allow-scripts-pendings**
6. check karna hai openclaw ko download hua yeah nhe **openclaw --version**
7. phir yeah cmd likhne hai **openclaw onboard --install-daemon**
    - **yes**
    - **QuickStart (recommended)**
    - **more**
    - **custom provider**
    - base url : **http://localhost:11434/v1**
    - **paste api key now**
    - enter : **ollama**
    - **OpenAI-compatible**
    - **qwen2.5:3b**
    - **custom-localhost-11434**
    - **local**
    - Enter: **Esc**

8. ab openclaw ko start karna hai hum:
    - **openclaw --help** isa openclaw ki ki commands miljayge sari
    - **openclaw gateway run** isa humera openclaw start hoga
    - **openclaw chat** isa humari actual chat start hoge 
    - **openclaw gateway stop** isa humera openclaw stop hoga

9. ab jab bhe start karna hoga hume apna openclaw ko tu yeah step follow karne ha:
    - **openclaw gateway stop** yeah gateway ko proper stop karayga bilkul
    - **openclaw gateway run** next cmd open karna hai oise bad yeah karna hai
    - **openclaw chat** ab apne actual cmd dena hai ager error ay tu neeche wali cmd run karne hai
    
    - **openclaw doctor --fix** 
    - **openclaw skills install --all**
    - **openclaw skills list**
    - **openclaw skills search windows**
    - **openclaw skills install windows-desktop-control**
    - **openclaw skills install windows-ui-automation**

    - **ollama** ollama ka server start kiya

# What is Hugging Face?
1. Hugging Face koi AI model nahi hai, balkay ye aik Platform/Community hai.
2. Yahan hazaron free aur open-source ready-made AI models paray hain jaise play store per apps.
3. Yahan hazaro Datasets bhe hote hai jis par AI ko train kiya jata hai
4. aur unko use karne ke tools & APIs
5. developers ko aik hi jagah par provide karta hai.