# LLM ki PROPER definition (Large Language Model)
1. Large Language Model (LLM) basically ek AI model hota hai jise "Machine Learning" aur "Deep Learning" ke zariye billions of words par train kiya jata hai.
2. Iska purpose ye hota hai ke wo text ko generate kare, translate kare, aur sawalon ke bilkul wese hi jawab de jaise koi insaan deta hai. 

---

# isa kin Purpose ka liya use karte hai:

* LLM sirf ek type ke nahi hote, inke kaam ke hisaab se categories hain:

1. **General Purpose Models:** Ye har tarah ke kaam kar sakte hain (e.g., GPT-4, Llama 3). Ye kahaniyan likhne se lekar coding tak sab kuch kar sakte hain.
2. **Small Language Models (SLM):** Jaise Phi-3 ya Gemma 2B. Ye size mein chote hote hain, kam computer power lete hain, aur laptop ya external disk par asani se chal jate hain.
3. **Coding Models:** yeah programming languages jaise Python, Java, etc. ke liye banaye jate hain,like (CodeLlama, DeepSeek-Coder).
4. **Instruction Tuned Models:** Ye models khas tor par insani "instructions" (hukm) manne ke liye train kiye jate hain.

---

# Types of LLM:

## Open Weight Models / Open Source Models:
1. yeah wo models hote hai jo open source publically free hote hai. inhe hum locally apne system mein download karke use kar sekhte hai. or inhe modify or fine-tune bhe kar sekhte hai. yeah free of course hote hai jaise ka phi3 , deepseek8b , llama etc.

## Proprietary Models: 
1. Yeh wo models hote hain jo kisi company ke control mein hote hain aur publicly open nahi hote.inhe tum locally download nahi kar sakte; sirf API ya web interface ke through use karte ha (jaise ChatGPT ya Gemini). hum inhe modify ya fine-tune directly nahi kar sakte (sirf limited customization milta hai) or Yeh mostly paid hote hain ya usage-based pricing pe chalte hain.

---

## Stage 01: `Inout Text`
1. subse phela hum LLM ko koi bhe Text provide karte ha like `Hello World`.
2. Ye wo text yeah input hai jo user kisi LLM ko bhejta hai.
3. abhe ka liya yeah sirf normal input yeah text hai. iski koi meaning nhe LLM ka liya.
4. LLM insaani zaban (Urdu/English/Spainsh) nahi samajhta, na characters na words kch nhe samajta hai.

---

## Stage 02: `Tokenizer`

1. **Tokenizer** wo software hai jo raw text ko chote chote pieces mein seperate karta hai, pre defined rules ka hisaab se. 
2. ois pieces ko hum **Tokens** bolte hai.
3. is process ka bad aik **list of tokens** ka output ata hai.

```text
"Hello world"
   ↓
["Hello", " world"] → 2 Tokens
```

## Stage 03: ID Mapping `Tokens → Numbers`

1. jo output mein **List of Tokens** ay the ab ois her token ko ek unique number diya jata hai. or har token ka ek **fixed number** hota hai jo model ke vocabulary mein save hai.
2. Mapping ka matlab hai token ko uske number se replace karna. means **Tokenizer** ne "Hello" ko **9906** se replace kiya, aur " world" ko **1917** se. 
3. Ab ye **numbers** hain, text nahi. LLM sirf in numbers ko samajhta hai.

```text
"Hello"  → 9906
"world" → 1917
```
### Output:
```text
[9906, 1917] 
```

---

## Stage 04: Embedding Layer `Numbers → Vectors`

1. Ab ye tokens jo numbers ban chuke hai. oisa Vector banaya jata hai means → numbers ka ek array
2. Har token ID ko ek meaningful numbers ke array mein convert kiya jata hai, taaki model uske "matlab" ko samajh sake.
3. Agar sirf ID 9906 use karte, to model ko pata nahi chalta ke "Hello" ka matlab kya hai.

```text
ID 9906 ("Hello")  →  [0.2, -0.5, 0.8, 0.1, ...]   (768 numbers)
ID 1917 (" world") →  [0.7, 0.3, -0.2, 0.9, ...]   (768 numbers)
```

---

## Stage 04: Positional Encoding: `Sequence Ka Pata Lagana`

1. **problem 01**: Model ko pata nahi chal raha ki "Hello" pehle hai ya "world" pehle. Kyunki vectors mein order nahi hota hai. 
2. Agar tum "Hello world" bhejo ya "world Hello" — embedding ke baad same dikhega.
3. **Positional Encoding** Har token ke vector mein uski position (pehla, doosra, teesra...) ki information mix karna.

```text
Token 1 ("Hello")  →  vector + "position 1" ka marker
Token 2 (" world") →  vector + "position 2" ka marker
```

---

## Step 05: `Transformer Layers` 

## Stage 06: `Attention Mechanism`
1. Jab model ek word pe kaam kar raha ho, usko doosre words dekhna padta hai jo usse related hain.
2. **The cat sat on the mat because it was tired**
3. "it" kisko refer kar raha hai — cat ya mat? Model ko "cat" dekhnа padega "it" samajhne ke liye
4. tu **Attention** yehi kaam karta hai.
5. Har token ke liye model 3 cheezein banata hai:

```text
Query (Q) — "Mujhe kya dhoondhna hai?"
Key (K) — "Main kya offer karta hoon?"
Value (V) — "Meri actual information kya hai?"
```