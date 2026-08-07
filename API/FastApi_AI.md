# FastApi with AI:
> **FastAPI ka use AI models ko duniya ke saamne serve karne ke liye karna (Model Deployment).**

> Jaise aapne ek robot banaya jo photo dekhkar bata sakta hai ki usme **billi hai ya kutta**. Lekin ye robot abhi sirf aapke laptop mein band hai. FastAPI ki madad se aap is robot ko **internet par daal sakte hain** — taaki koi bhi mobile app ya website is robot se sawaal kar sake.

---

# AI Model ko "Serve" karna kya hota hai?

Machine Learning model ek file hoti hai (e.g., `.pkl`, `.h5`, `.pt`) jo seekh chuka hota hai patterns pehchanna.  
Lekin ye file akele kuch nahi kar sakti — use ek **server** chahiye jo:

- **Input lega** (jaise ek image, text)
- Model ko **chalayega** (prediction karega)
- **Output dega** (jaise "billi hai", "fraud hai", "price 50 lakh")

FastAPI wahi server banata hai. Ye model ke liye ek **API wrapper** bana deta hai.

---

## ⚡ 2. FastAPI AI ke liye perfect kyun hai?

| Feature | AI ke liye kyun zaroori? |
|--------|---------------------------|
| **Python native** | Zyada tar AI libraries (TensorFlow, PyTorch, sklearn) Python mein hain, FastAPI bhi Python hai – full compatibility. |
| **Asynchronous** | Agar model ko process karne mein thoda time lage, toh FastAPI beech mein aur requests handle kar sakta hai. |
| **Data validation (Pydantic)** | Input galat type ka na ho (jaise image ki jagah text), isse model crash nahi hoga. |
| **Automatic docs** | AI developer ke liye bahut helpful – `/docs` par jaake dekh sakte hain model ka input format, turant test bhi kar sakte hain. |
| **Background tasks** | Prediction ke baad email bhejna, logs likhna — ye sab background mein ho sakta hai, response jaldi milega. |
| **Streaming/WebSocket** | Real-time AI apps (jaise live video analysis, chatbot) banane ke liye. |

---

# AI Model ko FastAPI mein Serve Karna

### Step 1: Model Train karke Save karo:

```python
# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample data: area (sq ft) vs price (lakhs)
data = {
    'area': [800, 1000, 1200, 1500, 1800],
    'price': [40, 50, 60, 75, 90]
}
df = pd.DataFrame(data)

X = df[['area']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Model ko file mein save karo
with open('house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

### Step 2: FastAPI App banao jo model load kare

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Server start hote hi model load karo
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Input ka structure define karo
class HouseFeatures(BaseModel):
    area: float
    bedrooms: int = 3   # optional, default 3
    age: int = 5

# Prediction endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Model ko sirf 'area' chahiye (example ke liye)
    input_data = np.array([[features.area]])
    prediction = model.predict(input_data)
    
    return {
        "predicted_price_lakhs": round(prediction[0], 2),
        "area": features.area
    }
```

### Step 3: Server Start karo

```bash
uvicorn main:app --reload
```

Ab `http://127.0.0.1:8000/docs` par jao, **POST /predict** endpoint khulega. "Try it out" karo aur data bhejo:

```json
{
  "area": 1200,
  "bedrooms": 3,
  "age": 2
}
```

Response aayega:

```json
{
  "predicted_price_lakhs": 60.0,
  "area": 1200
}
```