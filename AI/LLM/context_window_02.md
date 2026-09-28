# Context Window:

Socho tum ek dost se baat kar rahe ho. Lekin us dost ki **yaad-dasht sirf 5 minute** ki hai.

```
Tum:  "Mera naam Ali hai"
Dost: "Achha, Ali!"
[2 minute baad]
Tum:  "Mera naam kya hai?"
Dost: "Kya? Tumne bataya tha kya?"
```

**Kyun bhool gaya?** Kyunki uski yaad-dasht chhoti hai. Wo sirf **last 5 minute** yaad rakh sakta hai.

**LLM bilkul same hai.** Uski "yaad-dasht" = **Context Window**.

---

## Definition:

> **Context Window** = Ek LLM ek waqt mein **kitna text yaad rakh sakta hai** (dekh sakta hai), jab tum usse baat karte ho.

Isko **"memory limit"** samjho.

- Chhoti context window = Chhoti memory
- Badi context window = Badi memory

**Important:** Ye limit **tokens** mein measure hoti hai (words mein nahi).

---

## Example

1. Maan lo ek LLM ki context window **10,000 tokens** hai.
2. Ab tum usse baat karte ho. Har cheez jo bhejte ho — **sab us 10,000 mein count hoti hai**:

```
┌─────────────────────────────────────────┐
│         CONTEXT WINDOW (10,000)         │
├─────────────────────────────────────────┤
│ System prompt      →   500 tokens       │
│ Tool definitions   → 1,500 tokens       │
│ User message 1     →   100 tokens       │
│ LLM reply 1        →   300 tokens       │
│ User message 2     →   150 tokens       │
│ LLM reply 2        →   250 tokens       │
│ User message 3     →   200 tokens       │
│ ...                                     │
├─────────────────────────────────────────┤
│ TOTAL              → ~3,000 tokens      │
│ Remaining          → ~7,000 tokens      │
└─────────────────────────────────────────┘
```

Har nayi baat **jagah leti hai**. Jab 10,000 full ho jaye, **nayi cheez add nahi kar sakte** (ya purani hatani padegi).

---

## Sabse Important Point — LLM Ke Paas Memory Nahi Hoti

Ye samajhna **must** hai:

### ❌ Ghalat Fehmi:
"LLM ko pehle ki baatein yaad rehti hain"

### ✅ Sach:
"LLM **kuch bhi yaad nahi rakhta**. Tumhe **har baar poori baat** dobara bhejni padti hai."

**Iska matlab kya hai?**

Jab tum agent se 3rd baar baat karte ho, tum **poori history dobara bhejte ho**:

```
Call 1: [System] + [User1]                    → LLM reply deta hai
Call 2: [System] + [User1] + [Reply1] + [User2] → LLM reply deta hai
Call 3: [System] + [User1] + [Reply1] + [User2] + [Reply2] + [User3] → LLM reply
```

**Dekha?** Har call mein **poora safar** wapas jaata hai. Kyunki LLM ko kuch yaad nahi.

**Isliye context window bharti jaati hai. Isliye limit hit hoti hai.**

---

## Analogy — Whiteboard

Socho ek **whiteboard** hai. Tum aur tumhara dost us pe likh ke baat karte ho.

**Rules:**
1. Whiteboard ki **size fixed** hai (context window)
2. Tum kuch likhte ho (user message)
3. Dost padhta hai aur jawab likhta hai (LLM reply)
4. Sab kuch **whiteboard pe hi rehta hai**
5. Jab whiteboard **full** ho jaata hai, naya likhne ki jagah nahi bachti

**Aur sabse important:**
6. Dost **har baar poora whiteboard padhta hai** — sirf last line nahi
7. Jab dost jawab deta hai, wo **poora whiteboard dekh ke** jawab deta hai

**Yehi hai context window.** Ek limited jagah jahan poori baat-cheet rehti hai, aur LLM har baar poori cheez dekhta hai.

---

## Context Window Mein Kya Kya Count Hota Hai?

Ye **bahut important** hai samajhna. Sirf tumhara message nahi — **sab kuch** count hota hai:

### 1. System Prompt
Wo instructions jo LLM ko di jaati hain shuru mein.
```
"Tum ek coding assistant ho. File tools use karo..."
```
**~500 - 2,000 tokens**

### 2. Tool Definitions
Har tool ka naam, description, schema — LLM ko batana padta hai.
```
read_file(path, offset, limit) — File padhne ke liye...
write_file(path, content) — File likhne ke liye...
bash(cmd) — Command chalane ke liye...
```
**~1,000 - 5,000 tokens**

### 3. Conversation History
Poori purani baat-cheet — user ke messages aur LLM ke replies.
**Bahut zyada tokens — jitni lambi baat, utne zyada**

### 4. Tool Results
Jab LLM file padhta hai, bash chalata hai — uske **results bhi** count hote hain.
```
LLM: read_file("main.py")
Result: [5000 lines ka code]  ← ye 15,000 tokens!
```
**Bahut zyada tokens**

### 5. Current User Message
Tumhara abhi ka message.
**~100 - 500 tokens**

### 6. Output Reserve
Jawab ke liye jagah chahiye — isliye input aur output **same window share** karte hain.

---

## Chalo Ek Real Example Calculate Karein

Maan lo tumhara agent chal raha hai:

```
┌─────────────────────────────────────────┐
│         CONTEXT WINDOW (200,000)        │
├─────────────────────────────────────────┤
│ System prompt      →    800 tokens      │
│ Tool definitions   →  3,200 tokens      │
│ AGENTS.md          →  1,500 tokens      │
│ Chat history       →  8,000 tokens      │
│ File read result   → 12,000 tokens      │
│ Bash output        →  2,500 tokens      │
│ Current message    →    200 tokens      │
├─────────────────────────────────────────┤
│ TOTAL INPUT        → 28,200 tokens      │
│ Reserve for output → 50,000 tokens      │
│ Remaining          → 121,800 tokens     │
└─────────────────────────────────────────┘
```

Ye **200K window** ke saath. ~171K free hai abhi.

Lekin **20 more turns** ke baad? Window bhar jaayegi.

---

## LLM Memory:

1. LLM kuch yaad nahi rakhta iske pass koi memory nhe hoti hai.
2. Tumhe har baar poori history dobara bhejni padti hai
