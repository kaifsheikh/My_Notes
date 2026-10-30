# 🔷 Part 1: PyTorch - (Definition)

**PyTorch ek open-source Deep Learning library hai** jo **Meta (Facebook) AI Research** ne 2016 mein banayi.

**Simple definition:**
> PyTorch ek tool hai jo computer ko **insaan ki tarah seekhna** sikhaata hai — data de kar, galtiyan karwa kar, aur khud theek karwa kar.

Ye **Python** mein likhi gayi hai, isliye use karna aasan hai.

**Ek line mein:** PyTorch = **AI ka engine** (jaise car ka engine).

---

# 🔷 Part 2: PyTorch Ka Purpose:

PyTorch ka maqsad kya hai? 5 points:

| # | Purpose | Matlab |
|---|---------|--------|
| 1 | **Neural Networks banana** | Dimagh jaisa structure |
| 2 | **Data se seekhna** | Images, text, audio se pattern nikalna |
| 3 | **Predictions karna** | Naya data → jawab |
| 4 | **GPU par tez chalna** | Bohat fast calculation |
| 5 | **Research karna** | Naye AI models experiment karna |

**Aasan lafzon mein:** PyTorch aapko deta hai wo saare tools jisse aap ek **"artificial dimagh"** bana sakein jo seekh sake.

---

# 🔷 Part 3: PyTorch Ke Main Parts (Building Blocks)

PyTorch ke 4 basic cheezein hain:

### 1️⃣ Tensor — Data Ka Container
Tensor = multi-dimensional array (jaise Excel sheet, lekin GPU par chal sakta hai)

```python
import torch
a = torch.tensor([1, 2, 3])          # 1D
b = torch.tensor([[1,2], [3,4]])     # 2D (matrix)
```

### 2️⃣ Autograd — Automatic Galti Theek Karna
Jab model galti kare, PyTorch **khud** calculate karta hai ke kaunsi cheez kitni badalni hai.

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2
y.backward()
print(x.grad)  # 4.0
```

### 3️⃣ Neural Network (nn) — Model Banane Ke Tools
```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(10, 20),   # input layer
    nn.ReLU(),           # activation
    nn.Linear(20, 1)     # output layer
)
```

### 4️⃣ Optimizer — Model Ko Improve Karna
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

---

# 🔷 Part 4: PyTorch Ka Example (Poora Code)

Chalo ek **simple model** banate hain jo `y = 2x + 1` formula seekh le.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Data banayein
X = torch.tensor([[1.], [2.], [3.], [4.]])
y = torch.tensor([[3.], [5.], [7.], [9.]])   # 2x+1

# 2. Model banao
model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 3. Training Loop (seekhna)
for epoch in range(1000):
    pred = model(X)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 4. Test karo
print(model(torch.tensor([[5.]])))  # ~11 ke qareeb
```

**Ye kya kar raha hai?**
- 1000 baar data dekha
- Har baar galti kam ki
- Aakhir mein formula seekh liya ✅

---

# 🔷 Part 5: PyTorch Kahan Use Hoti Hai? (Real-World)

| Field | Use | Company |
|-------|-----|---------|
| **ChatGPT** | Text generation | OpenAI |
| **Face Recognition** | Facebook photo tagging | Meta |
| **Self-Driving Cars** | Object detection | Tesla |
| **Voice Assistant** | Speech recognition | Siri, Alexa |
| **Medical** | Cancer detection (X-ray) | Hospitals |
| **Netflix/YouTube** | Recommendations | Netflix |
| **Translation** | Google Translate | Google |
| **Gaming** | AI bots | Game companies |
| **Fraud Detection** | Bank security | Banks |
| **Robotics** | Robot learning | Research labs |

**Simple:** Jahan bhi **"AI"** ka zikr hai — wahan PyTorch ya uski behen (TensorFlow) kaam kar rahi hai.

---

# 🔷 Part 6: PyTorch vs Scikit-Learn — Farq

Dono AI ke tools hain, lekin **level alag** hai.

### Tashbeeh (Analogy):

| Tool | Tashbeeh |
|------|----------|
| **Scikit-Learn** | **Readymade Maggi** — bas paani daalo, 2 minute mein ready |
| **PyTorch** | **Khud se biryani pakana** — har masala aap control karo |

---

### Table Mein Farq:

| Feature | Scikit-Learn | PyTorch |
|---------|--------------|---------|
| **Type** | Traditional ML | Deep Learning |
| **Banaya** | Community | Meta (Facebook) |
| **Algorithms** | Ready-made (Linear Regression, SVM, Random Forest) | Neural Networks (khud banana parta hai) |
| **Data** | Excel / CSV (rows & columns) | Images, Text, Audio, Video |
| **Data Size** | Chhota (hazaron rows) | Bara (lakhon rows) |
| **Hardware** | CPU | CPU + **GPU** |
| **Code** | 3 lines mein kaam | 20+ lines |
| **Training Time** | Seconds | Hours / Days |
| **Seekhna** | Aasan (1-2 hafte) | Mushkil (2-3 mahine) |
| **Best For** | Simple predictions | ChatGPT, Face AI, Self-driving |

---

### Same Kaam Dono Mein (Comparison):

**Scikit-Learn (3 lines):**
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
print(model.predict([[3000]]))
```

**PyTorch (20 lines):**
```python
model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
for epoch in range(1000):
    pred = model(X)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print(model(torch.tensor([[3000.]])))
```

**Dekha?** Same kaam, lekin PyTorch mein zyada control aur code.

---

### Kis Kaam Ke Liye Kya Use Karein?

| Kaam | Tool |
|------|------|
| Bank loan approve karna | ✅ Scikit-Learn |
| Customer churn predict | ✅ Scikit-Learn |
| Sales forecast | ✅ Scikit-Learn |
| Spam email detect (simple) | ✅ Scikit-Learn |
| **Face recognition** | ✅ PyTorch |
| **ChatGPT jaisa model** | ✅ PyTorch |
| **Self-driving car** | ✅ PyTorch |
| **Cancer detection (X-ray)** | ✅ PyTorch |
| **Voice assistant** | ✅ PyTorch |

---

# 🔷 Part 7: Kya Dono Saath Use Ho Sakte Hain?

**Bilkul!** Ye real projects mein hota hai.

```python
# Step 1: Scikit-Learn se data clean karo
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_clean = scaler.fit_transform(X)

# Step 2: PyTorch se neural network train karo
X_tensor = torch.tensor(X_clean)
# ... PyTorch model aage
```

**Rule:** Scikit-Learn = **data taiyaar karna**, PyTorch = **model banana**.

---

# 🔷 Part 8: Kaunsa Pehle Seekhein? (Roadmap)

```
1. Python Basics        →  2 hafte
2. NumPy                →  1 hafta
3. Scikit-Learn         →  2-3 hafte  ← pehle yahan
4. PyTorch Basics       →  1 mahina
5. Neural Networks      →  1 mahina
6. CNN / RNN / Transformer → 2 mahine
7. Real Project         →  ongoing
```

**Logic:** Scikit-Learn se **ML ke basics** aayenge (train/test, overfitting). Phir PyTorch aasan lagega.

---

# 🔷 Part 9: Summary (Ek Nazar Mein)

| Sawal | Jawab |
|-------|-------|
| **PyTorch kya hai?** | Deep Learning library (AI ka engine) |
| **Kis ne banayi?** | Meta (Facebook) |
| **Kis liye?** | Neural Networks, AI models |
| **Kahan use?** | ChatGPT, Face AI, Self-driving, Medical |
| **Scikit-Learn se farq?** | Scikit-Learn = simple/ready-made, PyTorch = complex/custom |
| **Kaunsa mushkil?** | PyTorch (lekin zyada powerful) |
| **Kaunsa pehle?** | Scikit-Learn → phir PyTorch |
| **Dono saath?** | Haan! Scikit-Learn = data prep, PyTorch = model |

---

## 🎯 Aakhri Baat (Ek Line Mein)

> **Scikit-Learn** = "**Readymade tools** se simple kaam karo"
> **PyTorch** = "**Apna dimagh** khud banao, bara kaam karo"

Dono **dushman nahi**, **team members** hain. Ek data taiyaar karta hai, doosra AI banata hai.

---

Agar aap chahein to main **ek hi problem (Titanic survival ya House price)** dono tools mein side-by-side solve karke dikha sakta hoon — code ke saath. Batao kis pe focus karna hai? 🚀