# What is Scikit-Learn:
1. Scikit-Learn Python ki ek open-source Machine Learning ki library hai. Yeh NumPy, SciPy, aur Matplotlib ke upar bani hai, aur iska kaam data par Predictive Data Analysis (future ki prediction) aur complex Machine Learning models ko boht asani se apply karna hai.

2. Aap isko Pandas ke DataFrames aur NumPy ke Arrays dete hain $\rightarrow$ Yeh unse seekhta hai (Train hota hai) $\rightarrow$ Aur phir aane wale naye data ke baare mein prediction karta hai.

---

# Purpose of SK Learn:
1. **For Example** aapko aik aisi car banani hai jo khud chale (Self-Driving Car). Agar aap bilkul 0 se shuru karenge, toh aapko pehle loha pighlana padega, engine ka har ek nut-bolt khud design karna padega, tyres banane padenge. Is mein saalon lag jayenge!

2. Lekin agar aapko bani-banayi engine, tyres, aur steering wheel mil jayein, toh aapka kaam sirf unhein jor kar apni gari chalana hoga.

3. `Sklearn` ka purpose bhe yehi hai ka Machine Learning ke peeche boht mushkil aur bhaari Mathematics (Linear Algebra, Calculus, Statistics) hoti hai. Agar aap khud se har algorithm ka math code likhne baithenge, toh mahino lag jayenge.

4. `Sklearn` Yeh aapko Machine Learning ke saare mushkil mathematical models aur tools (ready-made) de deta hai. Aapko math ke formulae nahi likhne padte, bas un banay banaye tools ko use karna hota hai.

---

# Step 01: Sklearn ka Proper Workflow:
1. Sklearn mein kaam karne ka ek standard tareeqa (Workflow) hota hai. Har Machine Learning project isi raste se guzarta hai

### Data Preparation:

1. Machine Learning mein data ko hamesha 2 main hisson mein divide kiya jata hai.
    - **Features** $\rightarrow$ (Isko hum $X$ kehte hain)
    - **Target** $\rightarrow$ Label (Isko hum $y$ kehte hain)

2. **Features**: Features ka matlab hai woh saari informational cheezain ya qualities jin ki madad se hum koi faisla karte hain. Yeh hamare inputs hote hain.

    - **Car Example**: Car ka Model (Year), Engine CC, Milage (kitni chali hui hai), aur Company (Toyota/Suzuki).

    - **Pandas mein**: Yeh hamare DataFrame ke woh columns hote hain jo input ka kaam karte hain.

3. **Target**: woh khaas cheez hoti hai jo humein predict karni hoti है, ya jiska jawab humein chahiye hota hai. Yeh hamara output hota hai.

    - **Car Example**: Car ki Price hamara target hai.

    - **Pandas mein**: Yeh aam tor par ek single column hota hai jiska answer hum dhoond rahe hote hain.

4. **Formula**: $X$ (Features) ki madad se hum $y$ (Target) ka pata lagate hain aik real example se samajte hai.

    - **Real Example**: Hum computer ko sikhayenge ke "Kitne **hours** parhne se kitne **marks** aate hain" aur phir us se naye student ke marks predict karwayenge.

    - Yahan hamara Feature **($X$)** hai: **Study Hours** Aur hamara Target **($y$)** hai: **Marks** jo hum predict karengay.

---

# Step 02: Train-Test Split (Data ke do hissay karna)

1. Farz karein aapke paas 100 gariyon ka total data (Pandas DataFrame) maujood hai. Aap yeh saara ka saara data computer ko seekhne ke liye nahi dete. Kyun?

2. Agar aap saara data sikhane mein use kar lenge, toh aap check kaise karenge ke computer ne sach mein seekha hai ya bas ratta (memorize) maara hai?

3. Isliye hum Sklearn ka ek tool use karte hain jo is data ko do hisson mein baant deta hai:

    - Training Data (70% - 80%): Farz karein 80 gariyon ka data. Yeh data hum computer ko dikhate hain ke "Yeh dekho, agar gari 1300cc ho aur 2020 model ho toh price 30 Lakh hoti hai". Computer isse seekhta hai.

    - Testing Data (20% - 30%): Baqi 20 gariyon ka data. Yeh data hum computer se chhupa kar side par rakh dete hain. Is par hum baad mein computer ka exam (test) lenge.

# Step 03: Model Choose Karna 

1. Ab aapko sochna hai ke is data par kaunsa model fit baithega.
2. SkLearn mein **3 Main Categories** hai Models ki jinke Kam Data or According kiya jata ai hai.

    - **Supervised Learning** Models
        - **Regression Models** (Numbers Predict Karne Ke Liye)
        - **Classification Models** (Groups/Categories ka liya)

    - **Unsupervised Learning** Models
        - **Clustering Models** (Groups Khud Banana)
        - **Dimensionality Reduction** Models (Data Chota Karne Ke Liye)

    - **Reinforcement Learning** Models


    <!-- - Chunke humein gari ki Price (jo ke ek number hai) predict karni hai, toh hum Sklearn se kahenge ke bhai hamein **LinearRegression** ka model nikal kar do. -->

    <!-- - Agar hamein yeh predict karna hota ke gari "Automatic" hai ya "Manual" (Yes/No), toh hum **LogisticRegression** choose karte. -->

# Final Workflow:

```py
              MACHINE LEARNING BASIC WORKFLOW


        ┌─────────────────────────┐
        │      1. DATA LOAD       │
        │  (CSV, Database, Files) │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │      2. DATA CLEAN      │
        │  Pandas / NumPy use     │
        │  - Missing Values       │
        │  - Duplicates           │
        │  - Data Formatting      │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │     3. DATA PREPARE     │
        │  Features (X)           │
        │  Target (y)             │
        │  Train/Test Split       │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │     4. MODEL SELECT     │
        │  Scikit-learn (Sklearn) │
        │  Example:               │
        │  Linear Regression      │
        │  Decision Tree          │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │     5. TRAIN MODEL      │
        │        .fit()           │
        │  Model data se seekhta  │
        │  hai patterns           │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │       6. PREDICT        │
        │       .predict()        │
        │  New data ka result     │
        │  nikalta hai             │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │      7. EVALUATE        │
        │  Accuracy / Error Check │
        │  Model acha hai ya nahi │
        └─────────────────────────┘


DATA
 ↓
CLEAN
 ↓
PREPARE
 ↓
SELECT MODEL
 ↓
.fit()
 ↓
.predict()
 ↓
CHECK RESULT
```