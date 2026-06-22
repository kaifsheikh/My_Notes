# What is Pipeline:

Pipeline ka simple matlab hai: **Aik taraf se hum Raw Data provide karte hai, beech mein automatic steps honte hai, aur doosri taraf se hume result milta ha**

Aap pipeline ko aik **"Water Filter Plant"** se samajte hai.

* Pehle ganda pani andar aata hai.
* Beech mein filter 1 mitti saaf karta hai.
* Filter 2 germs ko maarta hai.
* Aakhir mein aapko saaf pani mil jata hai.

hume filter ko alag se khol kar saaf nahi karna parta, pani khud ba khud aik filter se doosre filter mein jata hai. Isi tarah Data Science aur AI mein data khud ba khud aik step se doosre step tak jata hai.

---

# Data Science vs AI Pipeline:

In dono ka maqsad aik hi hai: **Kaam ko automatic banana**. Lekin inke andar ke steps thode alag hote hain kyunke dono ka kaam thoda mukhtalif hai.

## 1. Data Science Pipeline:

Data Science ka zyada kaam hota hai purane data ko dekh kar company ke liye reports banana, graphs banana, aur faide ki baat dhoondna (Insights).

Iske steps aese hote hain:

1. **Data Jama Karna:** Excel ya database se purani sales ka data uthana.
2. **Data Safai (Cleaning):** Jo ghaltiyan hain ya missing numbers hain unhe theek karna.
3. **Analysis:** Graph banana ke kis mahine mein sab se zyada sale hui.
4. **Report:** Boss ko report de dena ke *"Sir, is mahine sale zyada hui thi."*

> **Data Science Pipeline ka end result:** Ek Report, Dashboard, ya Graph hota hai jo insan dekh kar samajhte hain.

## 2. AI / Machine Learning Pipeline:

AI ka kaam sirf report banana nahi hota, balkay aik aesa computer program (Model) banana hota hai jo khud se faisle kar sake (jaise automatic gaari chalana ya fraud pakarna).

Iske steps thode lambe aur advanced hote hain:

1. **Data Jama Karna:** Wahi purana data uthana.
2. **Data Safai (Cleaning):** Data ko saaf karna aur numbers ko scale karna.
3. **Model Training:** Scikit-Learn ke algorithm (jaise Logistic Regression) ko data de kar sikhana.
4. **Testing & Tuning:** Model ka imtihan lena ke woh kitne sahi jawab de raha hai aur uski settings theek karna.
5. **Deployment (Live Karna):** Model ko internet par live kar dena taake woh naye customers ka jawab khud de sake.

> **AI Pipeline ka end result:** Ek chalta phirta, faisla lene wala AI software hota hai.

---

## Ek Real-World:

Farz karein aap **YouTube** ke liye kaam kar rahe hain:

* **Data Science Pipeline:** Yeh check karegi ke Pakistan mein log kis tarah ki videos zyada dekh rahe hain. Yeh data saaf karegi, graph banayegi, aur YouTube ke manager ko dikhayegi ke *"Pakistan mein log cricket videos zyada dekhte hain."* (Kaam khatam).
* **AI Pipeline:** Yeh YouTube ka woh **Recommendation System** banayegi jo aapke samne khud ba khud videos lata hai. Yeh aapki har click ko monitor karegi, data filter karegi, AI model ko batayegi, aur furan aapke screen par aapki pasand ki video show kar degi bina kisi insan ke involve hue.

# Example 01:

```py
print(
"""
1. ('cleaner', SimpleImputer(strategy='mean')),
    
    Jab customers Foodpanda app par aate hain, to zaroori nahi ke unka saara data complete ho. Jaise hamare data mein kuch logon ki customer_age missing thi (np.nan). Machine Learning ke algorithms khali data (missing values) dekh kar crash ho jate hain.

    Purpose: Yeh step automatic tareeqe se poore column ke numbers ka Mean (Average) nikalta hai aur jahan jahan khali jagah hoti hai, wahan khud hi woh average number daal kar data ko mukammal (complete) kar deta hai taake code crash na ho.

2. ('scaler', StandardScaler())

    Iska Kaam: Hamare data mein alag-alag kism ke numbers hain. Maslan, time_of_day sirf 0 se 24 tak hota hai, jabke customer_age 18 se 60+ tak ho sakti hai.

    Purpose: AI algorithms aksar bade numbers (jaise Age ya Income) ko dekh kar samajhte hain ke yeh zyada important hain, aur chote numbers (jaise Time) ko ignore kar dete hain. StandardScaler sab numbers ko pakar kar unka scale aik jaisa kar deta hai (unhe 0 ke aaspas le aata hai). Is se computer har feature ko barabar ki ahmiyat deta hai aur prediction sahi hoti hai.

3. ('classifier', RandomForestClassifier(n_estimators=10, random_state=42))

    Iska Kaam: Jab data saaf ho jata hai aur scale ho jata hai, to woh is RandomForestClassifier ke paas aata hai. Yeh algorithm data ke andar patterns dhoondta hai (jaise ke raat ke waqt log kya khate hain, weekend par kya order karte hain).

    n_estimators=10: Iska matlab hai yeh algorithm backend par 10 chote chote Decision Trees (faislay karne wale drakht) banayega, aur un sab ke mashwary se final decision lega.

    random_state=42: Yeh sirf isliye likha jata hai taake jab bhi aap is code ko dubara chalayen, aapka computer har dafa aik jaisa hi result dikhaye (randomness ko control karne ke liye).
"""
)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

data = {
    'time_of_day': [13, 21, 14, 22, 12, 20, 13, 23],  # Ghante (Hours)
    'day_of_week': [0,  5,  1,  6,  2,  5,  0,  6],   # 0=Workday, 5-6=Weekend
    'customer_age': [22, 35, np.nan, 40, 25, np.nan, 19, 30], # Kuch data missing hai (np.nan)
    'order_choice': [0,  1,  0,  1,  0,  1,  0,  1]   # 0=Fast Food, 1=Desi
}

df = pd.DataFrame(data)

# Features -> X (Inputs)
# Target -> Y (Outputs)
X = df[['time_of_day', 'day_of_week', 'customer_age']]
y = df['order_choice']

# Data ko Train aur Test mein divide kardiya
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

foodpanda_pipeline = Pipeline([
    ('cleaner', SimpleImputer(strategy='mean')), 
    ('scaler', StandardScaler()),                 
    ('classifier', RandomForestClassifier(n_estimators=10, random_state=42)) 
])

# Pipiline ko Train kiya
print("AI Pipeline Training Shuru...")
foodpanda_pipeline.fit(X_train, y_train)
print("Training Mukammal!\n")

# New Data Predict karwaya
naya_customer = pd.DataFrame({
    'time_of_day': [22],
    'day_of_week': [6],
    'customer_age': [np.nan]  # Ganda data/missing data
})

# Naya data seedha pipeline mein jayega
prediction = foodpanda_pipeline.predict(naya_customer)

# Result ko aasan alfaz mein dikhana Condtions se
if prediction[0] == 1:
    print("AI Decision: Is customer ko 'Desi Food (Biryani)' sabsay ooper dikhao!")
else:
    print("AI Decision: Is customer ko 'Fast Food (Burger)' sabsay ooper dikhao!")
```