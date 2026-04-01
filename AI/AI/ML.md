# What is Machine Learning?
1. Machine Learning (ML) AI ki aik branch hai jisme hum machines ko data se seekhne ke qabil banate hain na ka Rules set karke.
2. simple words mein Pehle AI rule-based thi jaise ka ager muje spam or not spam filter karne hai tu muje rules set karne hote the jaise ka `if else` `switch` `case` yeah rules set karne hote the.
3. lakin ab ML mein hum Machine ko data dete hai or wo khud seekhti hai or khud rules banati hai na ke hum code likh kar rules set karein.

# Machine Learning 3 steps mein work karti hai:
1. Data
2. Algorithm
3. Computing Power

---

# 📘 **Step 01: `Data`**

1. Data ka matlab information hai ab wo information kch bhe ho sekhti hai jaise ka Text, Audio, Video, Images, Numbers, Tables, Code yeah kuch bhe ho sekhta hai.
2. Jaise insaan dekhta, sunta, padhta hai aur seekhta hai — waise machine data se seekhti hai.

---

## 🔹 Types of Data

### **1. Structured Data**

* Yeh woh data hota hai jo rows & columns tablular form mein hota hai
* jaise ka: excel sheets, mysql, banking data and etc.

---

### **2. Unstructured Data**

* Yeh woh data hota hai jo kisi khaas format mein nahi hota hai
* jaise ka: text, images, audio and videos and etc.

---

### **3. Semi-structured Data**

* Yeh woh data hota hai jo structured aur unstructured data ka combination hota hai
* jaise ka: json files, xml files and etc.

---

## 🔹 Data Key Points

1. jitna zyada data hoga, utne better learning hogi.
2. Data jitna clean hoga, utni better learning hogi.
3. agar data galat hai, to AI galat seekhega jisa input or output galat hoga.

---

Theek — main tumhare **same words** ko use karte hue isko clean aur organized kar deta hoon, aur end mein **Algorithm** ko bhi easy aur detail mein add kar deta hoon (simple aur same style mein).

---

# 📘 **Step 02: `Type of Machine Learning`**

## 🔹 Types

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

---

```text
MACHINE LEARNING
│
├── 1. SUPERVISED LEARNING
│   ├── Classification (Categories)
│   └── Regression (Numbers)
│
├── 2. UNSUPERVISED LEARNING
│   ├── Clustering (Groups)
│   └── Association (Patterns)
│
└── 3. REINFORCEMENT LEARNING
    ├── Agent (Learner)
    ├── Environment (World)
    ├── Actions (Choices)
    └── Rewards (Feedback)
```

---

## 🔹 Supervised Learning:

1. Supervised Learning ek aisa method hai jahan machine ko input + correct output Data diya jata hai, taake wo future mein naye data ke liye sahi prediction kar sake.

2. means mena machine ko koi question diya (`Input` isa `Features` bhe bolte hai) oisi question ka mena sahe answer bhe bata diya machine ko oiska botle hai (`Output` isa `Label` bhe bolte hai) ab machine khud se in dono ko samajti hai oiska bad jo new Output ata hai oiska hum Prediction bolte hai

3. **Purpose**

* Future ka result Predict karna
* Input aur output ka relation find karna
* Human decision ko automate karna

---

## 🔹 ML Example:

| Hours | Marks |
| ----- | ----- |
| 2     | 40    |
| 5     | 70    |

1. `my Input` : 6
2. `Machine Output` : 80 isa Prediction bolte hai

## 🔹 Classification (SubCategory of Supervise Learning)
1. Classification mein machine data ko categories / groups mein divide karti hai.
2. means machine predict karti hai ke input kis category yeah group se belong karta hai. 

## Example:
1. Categories / Classes (Jaise: Yes/No, Red/Blue/Green, Spam/Not Spam)

| Email Text                  | Label    |
| --------------------------- | -------- |
| “You won a prize”           | Spam     |
| “Meeting at 10 am tomorrow” | Not Spam |

## 🔹 Regression (SubCategory of Supervise Learning)
1. Regression mein machine data continuous numerical output predict karti hai.
2. Matlab, output number / value hoti hai, category nahi. 

## Example:
1. Numbers (Jaise: Price, Marks, Temperature, Salary)

| Hours Studied | Marks |
| ------------- | ----- |
| 2             | 40    |
| 5             | 70    |

# 🔹 Algorithm (Easy + Detail)

1. Algorithm ek step-by-step process hota hai jo machine ko batata hai ke data se kaise seekhna hai.

2. Jab hum machine ko Input aur Output dete hain to machine khud se direct nahi seekhti, balkay wo ek specific tareeqa follow karti hai jisa Algorithm kehte hain.

3. means machine jab in dono (Input + Output) ko samajti hai to wo actually Algorithm ka use kar rahi hoti hai taake wo relation find kar sake.

4. Algorithm ka kaam hota hai:

* Input aur Output ke darmiyan relation find karna
* pattern samajhna
* future ke liye prediction banana

---

# 📘 **Step 03: `Computing Power`**

1. Computing Power ka matlab hai machine ki calculation karne ki Power.
2. Jitni zyada computing power hogi, utna fast AI kaam karegi.

| Processor | Simple Explanation |
|-----------|--------------------|
| CPU (Central Processing Unit) | Normal processor — sab kaam kar sakta hai lekin AI ke liye slow |
| GPU (Graphics Processing Unit) | Pehle gaming ke liye, ab AI ke liye — ek saath hazaaron calculations kar sakta hai |
| TPU (Tensor Processing Unit) | Google ne specially AI ke liye banaya — aur bhi faster |
