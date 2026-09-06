# Project Description:

1. is Project banane ka purpose hai apna khud ka personal models Create or apne Personal Data se Train karna

2. tu mera pass kch **Features** columns hai jiski madaad se mein new **Data predict** karonga:
    - Date
    - Description
    - Amount
    - Type
    - Categories

3. or mera Actual **Target** hoga jo muje **Predict** karna hai 
    - Category

---

# 1️⃣ Logistic Regression:

1. **Purpose:** Yeh ek simple model hai. iska kaam hai har **Category** ke liye ek **probability (0 se 1 ke beech)** number nikaal kar deta hai means.

2. **0 or 1**: Maths aur Code mein hum **0%** ko **0** likhte hain aur **100%** ko **1** likhte hain.
    - **0** ka matlab: **0%** chance.
    - **0.5** ka matlab: **50%** chance.
    - **1** ka matlab: **100%** chance.
    - Toh jab **Logistic Regression** transaction ko dekhta hai, toh woh har category ke liye 0 se 1 ke beech ek number (score) nikaalta hai.

3. **probability** ka maltab hota hai Machine Learning mein **yakeen** ya **percentage** jo kisi cheez per hota hai jaise ka **Mujhe 95% yakeen hai ke yeh Food hai.** 

4. Jis category ki **probability** sabse zyada hogi, wahi category **predict** kar dega.

# Example:


---

# TF - IDF

1. **Term Frequency** – **Inverse Document Frequency**
2. Yeh ek technique hai jisse hum **text** ko **Numbers** mein badalte hain, taake **Machine Learning Models** unhe asani se samajh saken.
3. Machine Learning models sirf **numbers** samajhte hain, text nahi. **TF-IDF** har document ko ek number **vector** bana deta hai.
4. yeah koi model nhe hai yeah aik technique or tool hai iska kam hai **text** to **number** mein convert karna jisa model easily samaj sake.

## TF (Term Frequency)

1. **Purpose** Yeh batata hai ka: koi **word** kisi document mein kitni baar aaya.

## IDF (Inverse Document Frequency)

1. **Purpose**Yeh batata hai ka: koi **word** poori collection mein kitna **common** ya **rare** hai.
2. Rare word ko zyada importance milegi kyunki woh kisi specific document ki pehchan ho sakta hai.

# Example:

---

# 2️⃣ Decision Tree:

1. **Decision Tree** ek Machine Learning **Model** hai koi technique nahi.
2. Yeh bilkul waise hi kaam karta hai jaise hum rozana decision lete hain — sawal puchh kar, haan/na mein jawab dekar.

# Example

---

# Random Forest

1. Random Forest ek aisa model hai jo bohat saare Decision Trees ka jhund (group) hai.
2. Agar 1 Decision Tree ek akela dost hai jo salah deta hai, to Random Forest 100 doston ki committee hai jo milkar faisla leti hai.

3. **Random Forest** sab trees ko mila kar Decision leta hai.

4. **purpose** iska purpose hai ke akelay **Decision Tree** ki kamzoriyaan door kare, jaise ke training data ko ratta maar lena **overfitting**, chhoti si tabdeeli se poora badal jaana **instability**, aur kisi ek ajeeb data point ki wajah se galat *prediction* dena.

5. **Random Forest** har tree ko thoda alag data sample aur thodi alag features dekh kar train karta hai, phir naye transaction par saare trees apni apni category predict karte hain aur majority vote se final category decide hoti hai — is tarah yeh ek stable, bharosemand aur zyada accurate model ban jaata hai,

---

## 4️⃣ Naive Bayes (Shabdon Ki Ginti Ka Jadugar)

### Purpose
Yeh poora **probability** par kaam karta hai. Bayes theorem ka use karta hai aur maan leta hai ki saare shabd ek-doosre se independent hain (isiliye “naive” = bhola).  
Yeh har category mein kisi shabd ke aane ki frequency dekhta hai aur naye text ki category ka guess lagata hai.

### Bacchon wali soch:
Socho tumhare paas do dibbe hain – ek mein “Shopping” ki chitthiyan, doosre mein “Salary” ki. Har chitthi par kuch shabd likhe hain.  
Ab ek nayi chitthi aayi: “Super Market”.  
Tum dekhte ho: “Super” shabd Shopping dibbe mein 20 baar hai, Salary mein 0 baar. “Market” Shopping mein 15 baar, Salary mein 0 baar.  
Toh probability bahut zyada hai ki yeh Shopping hai. Bas yahi karta hai Naive Bayes – shabdon ki ginti se anuman.

### Kab use karein?
- Jab **zyadatar information text mein** ho (amount kam matter kare).
- Yeh bahut **fast** hai aur chhote data par bhi accha perform karta hai.
- Agar tumhe sirf Description se category chahiye, aur amount ka pattern complicated ho, tab accha rahega.
- Dhyan rahe: assumption ke sab shabd independent hain, hamesha sahi nahi, lekin phir bhi kaam kar jaata hai.

### Example tumhare data se:
Training mein model ne seekha:
- “Credit” shabd Salary category mein 90% baar aaya, Shopping mein 0%.
- “Market” shabd Shopping mein 80% baar aaya, Others mein 20%.
Naya: “JazzCash Transfer 1979.51”
- “JazzCash” sirf Others mein dikha tha → Others ki probability bahut high.
Toh predict: Others.

---

## 5️⃣ XGBoost (Expert Chela Jo Galtiyon Se Seekhta Hai)

### Purpose
Yeh bhi Random Forest ki tarah ensemble hai, lekin trees ko **ek ke baad ek** banata hai. Har naya tree pichhle trees ki **galtiyon par focus** karta hai. Ise boosting kehte hain.  
Yeh bahut powerful aur fast hai.

### Bacchon wali soch:
Maano tumhe teerandazi seekhni hai. Pehla teer chalaya aur nishane se thoda left gira.  
Doosra teer chalate waqt tumne pichhli galti sudhari – thoda right adjust kiya. Ab aur paas.  
Teesra aur bhi paas… aakhir mein bilkul bullseye.  
XGBoost theek aise hi kaam karta hai – har naya tree pichhle ki kamiyan poori karta hai.

### Kab use karein?
- Jab accuracy aur improve karni ho (Random Forest ke 80-85% ke baad 90% tak le jaana).
- Jab categories mein confusion ho (jaise “Shopping” aur “Others” bahut milte-julte hon).
- Thoda advanced hai, hyperparameter tuning maang sakta hai.

### Example tumhare data se:
Pehle tree ne kuch “Others” ko “Shopping” bol diya. Doosre tree ne un mistakes par dhyan diya aur seekha ki “Transfer” shabd ho toh Shopping mat bolo.  
Teesre tree ne aur refine kiya. Aakhri model bahut sharp hai.  
“Shophive 4555.45” – shayad Random Forest kabhi-kabhi ise Others bol de, lekin XGBoost ise Shopping pakdega kyunki usne “Shophive” aur amount range ka gehra mel dekh liya.

---

## ⭐ Tumhein Shuru Kahan Se Karni Chahiye?

**Meri recommendation: Random Forest Classifier (`RandomForestClassifier` in scikit-learn).**

Kyun?
- ✅ Text (TF-IDF ke baad) aur numbers (Amount) dono ko bahut acchhe se handle karta hai.
- ✅ Overfitting ka dar kam hota hai.
- ✅ Feature importance se tumhe pata chalega ki kaunse words (jaise “Market”) ya amount range sabse zyada predict kar rahi hai.
- ✅ Code karna aasan hai, 1000 rows par shaandaar kaam karega.

Agar baad mein lage ki accuracy thodi aur chahiye, to XGBoost ki taraf badh sakte ho.  
Agar shuru mein sirf shabdon se khelna chaho, to Naive Bayes ek quick experiment hai.

---

## 🧪 Ek Chhoti Si Poori Kahani (Dimagh Mein Bithane Ke Liye)

Maano tumhare paas training data:

| Description               | Amount  | Category |
|---------------------------|---------|----------|
| SALARY CREDIT             | 30000.0 | Salary   |
| Imtiaz Super Market       | 969.59  | Shopping |
| JazzCash Transfer         | 1979.51 | Others   |

**Step 1:** Description ko TF-IDF se numbers mein badlo.  
**Step 2:** Amount ko usi table mein jod do (Random Forest ko scaling ki zaroorat nahi).  
**Step 3:** Random Forest ko seekhao (fit).  
**Step 4:** Nayi entry “Daraz 1500” ka prediction lo – Model bolega “Shopping”.

Ab tum soch rahe hoge: “Daraz” shabd to training mein tha hi nahi! Phir bhi model ne kaise pehchana?  
Kyunki amount 1500 Shopping jaisa hai, aur shayad “Daraz” ke aas-paas ke shabd Shopping se milte-julte hain. Random Forest in combinations ko pakad leta hai.

---

## 🧩 Tumhari Saari Features Ka Role
- **Date** – Isse tum “day of week”, “month” nikaal sakte ho (weekend par shopping zyada?). Shuru mein chhod bhi sakte ho ya baad mein add karna.
- **Description** – Sabse important, ise TF-IDF se numbers banana hai.
- **Amount** – Direct feature, bahut helpful.
- **Type** (Credit/Debit) – Salary hamesha Credit hoti hai, yeh bhi ek powerful hint hai. Ise 0/1 banakar feature mein daal sakte ho.

Random Forest in sabko jodkar seekh lega, tumhein bas ek table (DataFrame) taiyar karna hai aur model.fit() karna hai.

---

## 🎁 Aakhri Salaah (Bilkul Aasan)
- **Pehla kadam:** Random Forest + TF-IDF par haath aazmao.
- **Doosra kadam:** Agar accuracy kam lage, to XGBoost aazmao.
- **Teesra kadam:** Categories ki insight lekar apne kharchay samjho.

Koi bhi model chuno, shuru mein jaadu nahi hoga – lekin thodi practice ke baad tumhara apna personal finance assistant taiyar ho jayega jo apne aap category pehchanega.

Kya ab main tumhein **Random Forest ke saath poora practical flow** (step by step, sochne ka tareeqa) Roman Urdu mein samjha doon? Bolo, haan toh agla step batata hoon! 😊
