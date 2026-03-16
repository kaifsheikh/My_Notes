# LLM ki PROPER definition (Large Language Model)
1. Large Language Model (LLM) ek AI model hota hai jise "Machine Learning" aur "Deep Learning" ke zariye billions (arbon) alfaaz par train kiya jata hai.
2. Iska purpose ye hota hai ke wo text ko generate kare, translate kare, aur sawalon ke bilkul wese hi jawab de jaise koi insaan deta hai.
3. jaise ka Chatgpt isme LLM model use hua hai

# isa kin Purpose ka liya use karte hai:

1. **General Purpose Models:** Ye har tarah ke kaam kar sakte hain (e.g., GPT-4, Llama 3). Ye kahaniyan likhne se lekar coding tak sab kuch kar sakte hain.
2. **Small Language Models (SLM):** Jaise Phi-3 ya Gemma 2B. Ye size mein chote hote hain, kam computer power lete hain, aur laptop ya external disk par asani se chal jate hain.
3. **Coding Models:** Ye khas tor par programming languages (Python, Java, etc.) ke liye banaye jate hain, jaise CodeLlama.
4. **Instruction Tuned Models:** Ye models khas tor par insani "instructions" (hukm) manne ke liye train kiye jate hain (Ollama par aksar yahi models milte hain).

# How LLM Words in Detail:

## Step 01: `Data Collection` `(Dunya bhar ki maloomat jama karna)`
1. Sab se pehle, model ko "parhane" ke liye bohot saara data chahiye hota hai.
2. Internet se billions of pages, Wikipedia, kitabein, articles, aur computer code uthaya jata hai.
3. Samjhein ke humne AI ko dunya ki har library ki har kitab parhwa di.

--- 

## Step 02: `Tokenization` `(Alfaaz ko numbers mein badalna)`
1. Computer insaani zaban (Urdu/English/Spainsh) nahi samajhta, wo sirf `Numbers` samajhta hai.
2. Kya hota hai? Har lafz ya lafz ke hissay ko ek khaas number (Token) de diya jata hai.
3. Agar jumla hai "Apple is red", to computer ise aise dekhega: Apple = `12`, is = `4`, red = `89`.

## Step 03: `Embeddings` `asal game yahan se start hoti hai`
1. Har token ko high-dimensional vector mein convert karna <br>
King   → [0.9, 1.1, 0.2] <br>
Queen  → [0.88, 1.09, 0.25] <br>
Apple  → [-0.7, 0.1, 1.9] <br>

## Step 04: `Transformer` `` 

## Step 05: `Self-Attention` ``

## Step 06: `Query, Key, Value (QKV) – real math` ``
Embedding → Query (Q) <br>
Embedding → Key   (K) <br>
Embedding → Value (V) <br>

## Step 07: `Multi-Head Attention`

## Step 08: `Feed Forward Network`

## Step 09: `Layers repeat hoti hain (depth)`

## LLM Major Commands:
Bilkul, aapki sahulat ke liye main ne tamam zaroori commands ko ek saaf-suthri table mein convert kar diya hai. Aap iska screenshot le sakte hain ya ise kahin save kar sakte hain:

### **Ollama Ki Zaroori Commands Table**

| Command | Category | Maqsad (Purpose) | Kab Istemal Karein? |
| --- | --- | --- | --- |
| **`ollama run [naam]`** | Main | Model download + Chat shuru karna. | Jab aap foran AI se baat karna chahen. |
| **`ollama pull [naam]`** | Download | Sirf model download karna (Chat nahi). | Slow internet par ya sirf download ke liye. |
| **`ollama list`** | Management | Downloaded models ki list dekhna. | Jab check karna ho ke F: drive mein kya kya hai. |
| **`ollama rm [naam]`** | Delete | Model ko disk se khatam/delete karna. | Jab space khatam ho rahi ho aur model na chahiye ho. |
| **`ollama ps`** | Monitor | Dekhna ke kaunsa model is waqt RAM mein chal raha hai. | Jab computer slow ho raha ho aur check karna ho. |
| **`ollama show [naam]`** | Info | Model ki mukammal detail dekhna. | Jab model ke parameters ya license check karna ho. |
| **`ollama serve`** | Service | Ollama ki background service start karna. | Agar Ollama ka icon taskbar mein nazar na aaye. |
| **`/bye`** | Chat | Chat se bahar nikalna (Exit). | Jab AI se baat khatam ho jaye aur CMD par wapis aana ho. |
| **`/set verbose`** | Chat | Jawab ki speed aur time (stats) dekhna. | Jab check karna ho ke AI kitna fast jawab de raha hai. |

---

# What is Model?
1. Model aik trained mathematical function hota hai
2. jo input (text, image, audio) ko process karke
3. output (answer, prediction, text) generate karta hai.

## Model Parameters?
1. Parameter wo numerical values hotay hain
2. jo model ke andar store hotay hain
3. aur ye decide karte hain ke model input ko kaise process karega aur output kya dega.
4. or parameters floating-point numbers hotay hain String , Integer yeah Words nahe hote hai
5. Agar hum kahein ke GPT-3 ke 175 Billion parameters hain, to iska matlab hai uske paas 175 billion chotay chotay "knobs" ya "settings" hain jo usay batate hain ke kis lafz ka kya matlab nikalna hai Jitne zyada parameters, AI utna hi smart hota hai.

## Model ka andar Paramter kaha per hote hai?
Model ke andar hotay hain:
1. Weights
2. Biases

## Weight:
1. Weight aik number hota hai
2. jo ye decide karta hai ke kisi input ki importance kitni hai.

## Bias:
1. Bias aik extra number hota hai
2. jo output ko thora sa adjust karta hai.

# What is Inference?
1. Inference wo process hai jisme trained model ko new input diya jata hai aur output liya jata hai
without training.

# What is Hugging Face?
1. Hugging Face koi AI model nahi hai, balkay ye aik Platform/Community hai.
2. Yahan hazaron free aur open-source ready-made AI models paray hain jaise play store per apps.
3. Yahan hazaro Datasets bhe hote hai jis par AI ko train kiya jata hai
4. aur unko use karne ke tools & APIs
5. developers ko aik hi jagah par provide karta hai.