# LLM ki PROPER definition (Large Language Model)
1. Large Language Model (LLM) basically ek AI model hota hai jise "Machine Learning" aur "Deep Learning" ke zariye billions (arbon) alfaaz par train kiya jata hai.
2. Iska purpose ye hota hai ke wo text ko generate kare, translate kare, aur sawalon ke bilkul wese hi jawab de jaise koi insaan deta hai. 

# isa kin Purpose ka liya use karte hai:

1. **General Purpose Models:** Ye har tarah ke kaam kar sakte hain (e.g., GPT-4, Llama 3). Ye kahaniyan likhne se lekar coding tak sab kuch kar sakte hain.
2. **Small Language Models (SLM):** Jaise Phi-3 ya Gemma 2B. Ye size mein chote hote hain, kam computer power lete hain, aur laptop ya external disk par asani se chal jate hain.
3. **Coding Models:** Ye khas tor par programming languages (Python, Java, etc.) ke liye banaye jate hain, jaise CodeLlama.
4. **Instruction Tuned Models:** Ye models khas tor par insani "instructions" (hukm) manne ke liye train kiye jate hain (Ollama par aksar yahi models milte hain).

# Types of LLM?
1. Open Weight Models
2. Proprietary Models

## Open Weight Models / Open Source Models:
1. yeah wo models hote hai jo open source publically free hote hai/
2. hum isko locally apne system mein download karke use kar sekhte hai. or isko modify or fine-tune bhe kar sekhte hai.
3. yeah free of course hote hai jaise ka phi3 , deepseek8b , llama etc.

## Proprietary Models: 
1. Yeh wo models hote hain jo kisi company ke control mein hote hain aur publicly open nahi hote.
2. Inko tum locally download nahi kar sakte; sirf API ya web interface ke through use karte ho. (jaise ChatGPT ya GPT-4)
3. nko modify ya fine-tune directly tum nahi kar sakte (sirf limited customization milta hai) or Yeh mostly paid hote hain ya usage-based pricing pe chalte hain.

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