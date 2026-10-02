# What is Scikit-Learn:
1. Scikit-Learn Python ki ek open-source Machine Learning ki library hai. Yeh NumPy, SciPy, aur Matplotlib ki base per bani hai.

2. iska kaam new data ko predict karna hai aur complex Machine Learning models ko boht asani se apply karna hai.

3. Scikit-Learn ek aisa toolbox hai jisme pehle se bane hue Machine Learning algorithms hote hain — aap bas data do, aur model taiyaar.

4. Aap isko Pandas ke DataFrames aur NumPy ke Arrays dete hain $\rightarrow$ Yeh unse seekhta hai (Train hota hai) $\rightarrow$ Aur phir aane wale naye data ke baare mein prediction karta hai.

---

# Purpose of SK Learn:
1. **For Example** aapko aik aisi car banani hai jo khud chale (Self-Driving Car). Agar aap bilkul 0 se shuru karenge, toh aapko pehle loha pighlana padega, engine ka har ek nut-bolt khud design karna padega, tyres banane padenge. Is mein saalon lag jayenge!

2. Lekin agar aapko bani-banayi engine, tyres, aur steering wheel mil jayein, toh aapka kaam sirf unhein jor kar fix karna hoga or car ready.

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

1. SkLearn mein yeah Machine Learning mein **3 Main Categories** hai Models ki.
    - **Supervised Learning**
    - **Unsupervised Learning**
    - **Reinforcement Learning**

2. in teen main categories mein bohot saare **Algorithms (models)** hote hain, jo alag-alag problem types ke liye bane hote hain. bs hume yeah dekhna hota hai ka konsa Data par kaunsa model fit baithega oiska liya hume.

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

---

# Part 1: What is Scikit-Learn:

1. Scikit-Learn Python ki ek open-source Machine Learning ki library hai. Yeh NumPy, SciPy, aur Matplotlib ki base per bani hai.

2. Iska kaam new data ko predict karna hai aur complex Machine Learning models ko boht asani se apply karna hai.

3. Scikit-Learn ek aisa toolbox hai jisme pehle se bane hue Machine Learning algorithms hote hain — aap bas data do, aur model taiyaar.

4. Aap isko Pandas ke DataFrames aur NumPy ke Arrays dete hain → Yeh unse seekhta hai (Train hota hai) → Aur phir aane wale naye data ke baare mein prediction karta hai.

---

# Part 2: Purpose of Scikit-Learn

1. **For Example** aapko aik aisi car banani hai jo khud chale (Self-Driving Car). Agar aap bilkul 0 se shuru karenge, toh aapko pehle loha pighlana padega, engine ka har ek nut-bolt khud design karna padega, tyres banane padenge. Is mein saalon lag jayenge!

2. Lekin agar aapko bani-banayi engine, tyres, aur steering wheel mil jayein, toh aapka kaam sirf unhein jor kar fix karna hoga aur car ready.

3. `Sklearn` ka purpose bhi yehi hai ke Machine Learning ke peeche boht mushkil aur bhaari Mathematics (Linear Algebra, Calculus, Statistics) hoti hai. Agar aap khud se har algorithm ka math code likhne baithenge, toh mahino lag jayenge.

4. `Sklearn` aapko Machine Learning ke saare mushkil mathematical models aur tools (ready-made) de deta hai. Aapko math ke formulae nahi likhne padte, bas un banay banaye tools ko use karna hota hai.

---

# Part 3: Sklearn ka Proper Workflow (Order Wise)

Sklearn mein kaam karne ka ek standard **Workflow** hota hai. Har Machine Learning project **isi order** ko follow karta ha.

```
STEP 1  →  DATA LOAD
STEP 2  →  DATA CLEAN
STEP 3  →  DATA EXPLORE (EDA)
STEP 4  →  DATA PREPARE (X, y, Split)
STEP 5  →  MODEL SELECT
STEP 6  →  MODEL TRAIN (.fit)
STEP 7  →  PREDICT (.predict)
STEP 8  →  EVALUATE (Check Result)
STEP 9  →  IMPROVE (Optional)
```

Ab har step ko detail mein samajhte hain:

---

## 🟦 Step 01: Data Load (Data Uthana)

1. Sab se pehla kaam hai **data lana**. Data kahan se aata hai?
   - CSV file (Excel jaisi file)
   - Database (SQL)
   - Online source (Kaggle, GitHub)
   - Company ki apni files

2. Pandas ki madad se hum data load karte hain:

```python
import pandas as pd
df = pd.read_csv('cars.csv')
```

3. Iske baad hum data ko **DataFrame** kehlata hai — jo ek Excel sheet jaisa hota hai (rows aur columns).

**Aasan lafzon mein:** Pehle data lao, warna seekhoge kis se?

---

## 🟦 Step 02: Data Clean (Data Saaf Karna)

1. Real data **hamesha unclean** hota hai. Usme kuch na kuch kharabi hoti hai. Isliye sab se pehle usko **Clean** karna parta hai.

2. Data Clean mein **4 main kaam** hote hain:

### (A) Missing Values (Khaali Dabbe)
Kuch cells khaali hote hain — jaise kisi gari ki Age nahi likhi.

```python
# Tareeqa 1: Row delete karo
df = df.dropna()

# Tareeqa 2: Average se bhar do
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Tareeqa 3: Median se bhar do
df['Price'] = df['Price'].fillna(df['Price'].median())
```

### (B) Duplicates (Repeat Rows)
Ek hi row 2 baar aa jati hai — isko hatao.

```python
df = df.drop_duplicates()
```

### (C) Wrong Format (Ghalat Format)
Jaise Price column mein "30 Lakh" likha ho, jabke sirf 30 hona chahiye.

```python
df['Price'] = df['Price'].str.replace(' Lakh', '').astype(float)
```

### (D) Outliers (Ajeeb Values)
Jaise gari ki price 99999999 Lakh — ye impossible hai, hatao.

**Aasan lafzon mein:** Data ko **Clean** karo — warna model ghalat learn karayga or phir bad mein output bhe galat ayga.

---

## 🟦 Step 03: Data Explore (EDA — Data Dekhna)

1. Cleaning ke baad hum data ko **dekhte** hain. Isko **EDA (Exploratory Data Analysis)** kehte hain.

2. Iska maqsad: Samajhna ke data mein kya kya hai.

### Kya Kya Dekhte Hain:

```python
df.head()        # Pehli 5 rows dekho
df.shape         # Kitni rows, kitne columns
df.describe()    # Summary (mean, min, max)
df.info()        # Data types
```

3. Charts bana kar bhi dekhte hain (Matplotlib/Seaborn se).

**Aasan lafzon mein:** Data ko **ghaur se dekho** — kya cheez kaise related hai.

---

## 🟦 Step 04: Data Prepare (Features, Target, Split)

Ab data ko model ke liye taiyaar karte hain. Isme 3 kaam hain:

### (A) Features aur Target Alag Karna

1. Machine Learning mein data ko hamesha 2 main hisson mein divide kiya jata hai.
   - **Features** → (Isko hum $X$ kehte hain)
   - **Target** → Label (Isko hum $y$ kehte hain)

2. **Features**: Features ka matlab hai woh saari informational cheezain ya qualities jin ki madad se hum koi faisla karte hain. Yeh hamare inputs hote hain.
   - **Car Example**: Car ka Model (Year), Engine CC, Mileage (kitni chali hui hai), aur Company (Toyota/Suzuki).
   - **Pandas mein**: Yeh hamare DataFrame ke woh columns hote hain jo input ka kaam karte hain.

3. **Target**: woh khaas cheez hoti hai jo humein predict karni hoti hai, ya jiska jawab humein chahiye hota hai. Yeh hamara output hota hai.
   - **Car Example**: Car ki Price hamara target hai.
   - **Pandas mein**: Yeh aam tor par ek single column hota hai jiska answer hum dhoond rahe hote hain.

4. **Formula**: $X$ (Features) ki madad se hum $y$ (Target) ka pata lagate hain. Aik real example se samajhte hain:
   - **Real Example**: Hum computer ko sikhayenge ke "Kitne **hours** parhne se kitne **marks** aate hain" aur phir us se naye student ke marks predict karwayenge.
   - Yahan hamara Feature **($X$)** hai: **Study Hours**, Aur hamara Target **($y$)** hai: **Marks** jo hum predict karenge.

### Code:

```python
# X = Features (saare input columns)
X = df[['Model', 'Engine_CC', 'Mileage', 'Company']]

# y = Target (jo predict karna hai)
y = df['Price']
```

### (B) Scaling (Optional — Numbers Ko Barabar Karna)

Kabhi kabhi features ki values boht alag hoti hain (jaise Age = 5, Price = 5000000). Isko same range mein laate hain.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**Aasan lafzon mein:** Sab numbers ko **same level** par lao, warna model confuse hoga.

### (C) Train-Test Split (Data ke Do Hissay Karna)

1. Farz karein aapke paas 100 gariyon ka total data (Pandas DataFrame) maujood hai. Aap yeh saara ka saara data computer ko seekhne ke liye nahi dete. Kyun?

2. Agar aap saara data sikhane mein use kar lenge, toh aap check kaise karenge ke computer ne sach mein seekha hai ya bas ratta (memorize) maara hai?

3. Isliye hum Sklearn ka ek tool use karte hain jo is data ko do hisson mein baant deta hai:

   - **Training Data (70% - 80%)**: Farz karein 80 gariyon ka data. Yeh data hum computer ko dikhate hain ke "Yeh dekho, agar gari 1300cc ho aur 2020 model ho toh price 30 Lakh hoti hai". Computer isse seekhta hai.

   - **Testing Data (20% - 30%)**: Baqi 20 gariyon ka data. Yeh data hum computer se chhupa kar side par rakh dete hain. Is par hum baad mein computer ka exam (test) lenge.

### Code:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 20% test ke liye
    random_state=42       # har baar same split
)
```

**Aasan lafzon mein:** Data ke **do hissay** karo — ek par seekho, doosre par test do.

---

## 🟦 Step 05: Model Select (Kaunsa Model Choose Karna)

1. Sklearn mein Machine Learning ke **3 Main Categories** hain Models ki:
   - **Supervised Learning**
   - **Unsupervised Learning**
   - **Reinforcement Learning**

2. In teen main categories mein bohot saare **Algorithms (models)** hote hain, jo alag-alag problem types ke liye bane hote hain. Bas humein yeh dekhna hota hai ke kaunse Data par kaunsa model fit baithega, uske liye humein:

   - **Supervised Learning** Models
     - **Regression Models** (Numbers Predict Karne Ke Liye)
       - Linear Regression
       - Decision Tree Regressor
       - Random Forest Regressor
       - Ridge / Lasso
     - **Classification Models** (Groups/Categories ke liye)
       - Logistic Regression
       - Decision Tree Classifier
       - Random Forest Classifier
       - SVM
       - KNN
       - Naive Bayes

   - **Unsupervised Learning** Models
     - **Clustering Models** (Groups Khud Banana)
       - K-Means
       - DBSCAN
       - Hierarchical
     - **Dimensionality Reduction** Models (Data Chota Karne Ke Liye)
       - PCA
       - t-SNE

   - **Reinforcement Learning** Models
     - Q-Learning
     - Deep Q-Network (DQN)
     - (Ye models game khel kar seekhte hain — jaise AlphaGo)

### Kaunsa Model Kab Choose Karein?

| Problem | Model Type | Example |
|---------|-----------|---------|
| Number predict | **Regression** | Gari ki Price |
| Yes/No predict | **Classification** | Automatic/Manual |
| Groups banana | **Clustering** | Customer types |
| Game seekhna | **Reinforcement** | Chess bot |

**Aasan lafzon mein:** Pehle dekho **problem kaisi hai**, phir **usi ka model** uthao.

---

## 🟦 Step 06: Model Train (Seekhana — `.fit()`)

1. Model select karne ke baad, hum usay **train** karte hain. Isko `.fit()` kehte hain.

2. Is step mein model **Training Data** (X_train, y_train) dekhta hai aur patterns seekhta hai.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)     # Yahan model seekh raha hai
```

3. Jaise student kitaab parh kar seekhta hai, waise hi model data dekh kar seekhta hai.

**Aasan lafzon mein:** Model ko **data dikhao** — wo khud patterns seekh lega.

---

## 🟦 Step 07: Predict (Jawab Nikalna — `.predict()`)

1. Train hone ke baad, ab **Test Data** (X_test) par prediction karte hain.

2. Model ne jo seekha hai, uske hisaab se naya data ka jawab deta hai.

```python
predictions = model.predict(X_test)
```

3. Ye predictions hum **asli jawab** (y_test) se compare karenge.

**Aasan lafzon mein:** Model se **naya sawal** poocho — wo jawab dega.

---

## 🟦 Step 08: Evaluate (Result Check Karna)

1. Ab hum dekhte hain ke model ne **kitna sahi** jawab diya. Isko **Evaluation** kehte hain.

2. **Regression** (Numbers) ke liye metrics:

| Metric | Matlab | Acha Kab? |
|--------|--------|-----------|
| **MSE** (Mean Squared Error) | Galti ka square average | Kam = Acha |
| **RMSE** | MSE ka square root | Kam = Acha |
| **MAE** | Average galti | Kam = Acha |
| **R² Score** | 0 se 1 tak | 1 ke qareeb = Acha |

3. **Classification** (Categories) ke liye metrics:

| Metric | Matlab |
|--------|--------|
| **Accuracy** | Kitne % sahi |
| **Precision** | Jo "Yes" bola, wo sach mein Yes? |
| **Recall** | Jo asli "Yes" the, unhe pakra? |
| **F1 Score** | Precision + Recall ka mix |
| **Confusion Matrix** | Table: Sahi vs Ghalat |

### Code:

```python
from sklearn.metrics import mean_squared_error, r2_score

print("MSE:", mean_squared_error(y_test, predictions))
print("R² Score:", r2_score(y_test, predictions))
```

**Aasan lafzon mein:** Model ka **exam lo** — kitna pass hua?

---

## 🟦 Step 09: Improve (Behtar Karna — Optional)

1. Agar result kharaab aaye, toh model ko **behtar** karte hain. Iske 3 tareeqe hain:

### (A) Naya Model Try Karo
Linear Regression se kharaab aaya? Random Forest try karo.

```python
from sklearn.ensemble import RandomForestRegressor
model2 = RandomForestRegressor(n_estimators=100)
model2.fit(X_train, y_train)
```

### (B) Hyperparameter Tuning
Model ki settings badlo — jaise `n_estimators=100` ko `200` karo.

```python
from sklearn.model_selection import GridSearchCV
# Best settings dhoondta hai automatically
```

### (C) Feature Engineering
Naye features banao — jaise "Gari ki Age" (2024 - Model Year).

**Aasan lafzon mein:** Agar pehli baar mein **sahi na aaye**, toh badlo aur phir try karo.

---

# Part 4: Final Workflow (Complete Diagram)

```py
              MACHINE LEARNING BASIC WORKFLOW


        ┌─────────────────────────┐
        │   1. DATA LOAD          │
        │  (CSV, Database, Files) │
        │  pd.read_csv()          │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   2. DATA CLEAN         │
        │  - Missing Values       │
        │  - Duplicates           │
        │  - Wrong Format         │
        │  - Outliers             │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   3. DATA EXPLORE (EDA) │
        │  - head(), describe()   │
        │  - Charts banayein      │
        │  - Correlation dekhein  │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   4. DATA PREPARE       │
        │  - Features (X)         │
        │  - Target (y)           │
        │  - Scaling (optional)   │
        │  - Train/Test Split     │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   5. MODEL SELECT       │
        │  Regression? Classify?  │
        │  Linear? Random Forest? │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   6. TRAIN MODEL        │
        │        .fit()           │
        │  X_train, y_train par   │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   7. PREDICT            │
        │       .predict()        │
        │  X_test par             │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   8. EVALUATE           │
        │  Regression: MSE, R²    │
        │  Classify: Accuracy, F1 │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │   9. IMPROVE (Optional) │
        │  - Naya model try       │
        │  - Hyperparameter tune  │
        │  - Feature engineering  │
        └─────────────────────────┘


DATA
 ↓
CLEAN
 ↓
EXPLORE
 ↓
PREPARE (X, y, Split)
 ↓
SELECT MODEL
 ↓
.fit()
 ↓
.predict()
 ↓
EVALUATE
 ↓
IMPROVE
```

---

# Part 5: Complete Example (Car Price Prediction)

Ye poora code hai — aapke workflow ke mutabiq, step by step:

```python
# ===== STEP 1: DATA LOAD =====
import pandas as pd
df = pd.read_csv('cars.csv')

# ===== STEP 2: DATA CLEAN =====
df = df.dropna()                    # khaali hatao
df = df.drop_duplicates()           # duplicate hatao

# ===== STEP 3: DATA EXPLORE (EDA) =====
print(df.head())                    # pehli 5 rows
print(df.describe())                # summary

# ===== STEP 4: DATA PREPARE =====
X = df[['Model', 'Engine_CC', 'Mileage']]   # Features
y = df['Price']                              # Target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===== STEP 5: MODEL SELECT =====
from sklearn.linear_model import LinearRegression
model = LinearRegression()          # Price = number, isliye Regression

# ===== STEP 6: TRAIN =====
model.fit(X_train, y_train)         # Model seekh raha hai

# ===== STEP 7: PREDICT =====
predictions = model.predict(X_test)

# ===== STEP 8: EVALUATE =====
from sklearn.metrics import mean_squared_error, r2_score
print("MSE:", mean_squared_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))

# ===== STEP 9: IMPROVE (agar zaroorat ho) =====
from sklearn.ensemble import RandomForestRegressor
model2 = RandomForestRegressor(n_estimators=100)
model2.fit(X_train, y_train)
```

---

# Part 6: Summary (Ek Nazar Mein)

| Step | Kaam | Tool |
|------|------|------|
| 1 | Data Load | `pd.read_csv()` |
| 2 | Data Clean | `dropna()`, `fillna()` |
| 3 | Data Explore | `head()`, `describe()` |
| 4 | Data Prepare | `train_test_split()` |
| 5 | Model Select | `LinearRegression()` |
| 6 | Train | `.fit()` |
| 7 | Predict | `.predict()` |
| 8 | Evaluate | `accuracy_score()`, `MSE` |
| 9 | Improve | `GridSearchCV()` |

---

## 🎯 Aakhri Baat

- **Har ML project** isi **9-step workflow** se guzarta hai
- **Order matters** — pehle data, phir clean, phir prepare, phir model
- **`.fit()` = seekhna**, **`.predict()` = jawab dena**
- Result kharaab aaye toh **Step 9 (Improve)** par wapas jao

Bas itna yaad rakho: **DATA → CLEAN → EXPLORE → PREPARE → SELECT → TRAIN → PREDICT → EVALUATE → IMPROVE** 🚀