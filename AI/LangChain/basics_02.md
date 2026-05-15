# Model inside Encoder or Decoder:
## Part 1: Pehle Ye Samjho — Model Kya Hai:

AI Model ek **dimaag** hai jo:
- **Input** leta hai (Questions, text)
- **Sochta** hai (process karta hai)
- **Output** deta hai (Answer, Response)

Ab ye "sochna" do hisson mein divide hota hai: **Encoder** aur **Decoder**

---

## Part 2: Encoder Kya Hai:
> **Encoder wo hissa hai jo input ko "samajhta" hai aur uska ek "summary/meaning" bana leta hai.**

### Example:

Socho ek **teacher** hai jo kitaab padhta hai.

| Step | Kya Ho Raha Hai |
|:---|:---|
| Teacher kitaab padhta hai | Input lena |
| Teacher dimaag mein summary banata hai | **Encoding** |
| Ab teacher ne sab kuch "samajh" liya | Encoder ka kaam khatam |

**Encoder ka kaam:**  
Text ko numbers mein badalna. Ye numbers "meaning" store karte hain.

---

## Part 3: Decoder Kya Hai:

> **Decoder wo hissa hai jo "summary/meaning" se naya text generate karta hai.**

### Example:

Ab wahi **teacher** students ko padhata hai.

| Step | Kya Ho Raha Hai |
|:---|:---|
| Teacher ke dimaag mein summary hai | Encoded information |
| Teacher students ko samjhata hai | **Decoding** |
| Student ko jawab mil gaya | Decoder ka kaam khatam |

**Decoder ka kaam:**  
Numbers se wapas text banana — jawab, translation, ya kuch bhi.

---

## Part 4: Dono Ka Combination

Input: `"How are you?"`  
Output chahiye: `"Aap kaise hain?"`

---

### Step-by-Step:

```
"How are you?"
      ↓
   [ENCODER]  ← Ye sentence ko "samjha"
      ↓
  "Ye sawaal hai, mood puchh raha hai, informal hai..."
  (Ye sab numbers mein convert ho gaya)
      ↓
   [DECODER]  ← Numbers se Urdu banayega
      ↓
"Aap kaise hain?"
```
---

# Model Architecture:
1. Model Architecture = Model ka "design" ya "Structure". Ye batata hai ki model andar se kaise bana hai — kitne layers hain, kaunse parts hain, aur input se output kaise banta hai.

## Example:
1. Ek car ka architecture: Engine, wheels, steering, brakes

2. Ek house ka architecture: Rooms, kitchen, bathroom, doors

3. waise hi: Ek model ka architecture: Encoder, Decoder, Attention layers, Feed-forward layers

# Model Architecture Ke Main Types:
1. aik model mein 2 combination ho sekhte hai jaise ka yeah tu sirf Encoder hai yeah Decoder hai
2. yeh phir wo dono he hai Encoder bhe or Decoder bhe

| Type | Parts | Example |
|:---|:---|:---|
| **Encoder + Decoder** | Dono hain | T5, BART, FLAN-T5 |
| **Sirf Decoder** | Sirf Decoder | GPT, Llama, Mistral |
| **Sirf Encoder** | Sirf Encoder | BERT, RoBERTa |

---