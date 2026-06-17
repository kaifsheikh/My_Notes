# What is Statistic:
1. Statistic ka matlab hai ka Numbers ko analysics karke oiska kch matlab find karna jaise ka:
2. Class ka Students ka Marks Count karna Average, Max, and Min jaise or bhe kam karna wo sub Statistic mein ata hai

# Min()
1. Array mein sabse chhoti value return karta hai.

```py
import numpy as np

arr = np.array([5, 2, 9, 1, 7])
print(np.min(arr))   # Output: 1
```

# Max()
1. Array mein sabse badi value return karta hai.

```py
import numpy as np

arr = np.array([5, 2, 9, 1, 7])
print(np.max(arr))   # Output: 9
```

# median()
> 1. ### yeah Numbers ko chote se bade mein Arrange / Sort karta hai Ascending Order mein phir jo bhe number bilkul center mein ayga oisa Median bolte hai.

> 2. ### yeah Normal Average ki terha he hota hai yeah oisa alag hota hai


# mean() - Average

> 1. ### yeah sari values ka sum karta hai or Number of Values se Divide kar deta hai.

> 2. ### isko Average find karne ka liya use karte hai 

```py
import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.mean(arr))   # Output: 2.5
```

# mode() - Return Repeated Value

> 1. ### Jo value sabse zyada baar repeat ho.

> 2. ### NumPy direct mode function nahi hai Is liye SciPy use hota hai

```py
from scipy import stats

data = [10, 20, 20, 30, 40]

mode_result = stats.mode(data)

print(mode_result)
```

> 1. ### Flipkart/Amazon jaisi website par lakhon products hain. Aap dekhna chahte ho kaunsi category sabse zyada bikti hai (e.g., “Electronics”, “Clothing”, “Books”). Mode directly batayega — yahan category string mein hai, mean/median nahi nikal sakte, sirf mode.

```py
from scipy import stats
import numpy as np

orders = np.array(["Electronics", "Clothing", "Electronics", "Books", "Electronics", "Clothing"])

mode_category = stats.mode(orders).mode

print(mode_category)  # "Electronics"
```

> 1. ### Support system mein ek lakh tickets hain, har ticket ka “issue_type” hai: “Login failure”, “Payment error”, “Refund request”, etc. Mode nikaalo — pata chalega kaunsa issue sabse zyada users face kar rahe hain. Phir pehle usi pe engineering team focus karegi.

```py
import numpy as np
from scipy import stats

# Possible issue types
issues = ["Login failure", "Payment error", "Refund request", "Account locked", "App crash"]

# Probabilities
probabilities = [0.40, 0.25, 0.20, 0.10, 0.05]

# 1 lakh tickets ka random array generate
np.random.seed(42)
tickets = np.random.choice(issues, size=100000, p=probabilities)

# Check karo first 10 tickets
print(tickets[:10])

print(
"""
1. customer support par aane wale 5 issues:

 - issues = ["Login failure", "Payment error", "Refund 
   request", "Account locked", "App crash"]

2. Probabilities set karte hain:
 
 - probabilities = [0.40, 0.25, 0.20, 0.10, 0.05]

 - Yahan hum har issue ke aane ka chance (percentage) 
   set kar rahe hain. Probability ka total hamesha 1 (yaani 100%) hona chahiye:

    - 0.40 (40% Chance): Sab se zyada tickets "Login failure" ke aayenge.
    - 0.25 (25% Chance): "Payment error" ke aayenge.
    - 0.20 (20% Chance): "Refund request" ke aayenge.
    - 0.10 (10% Chance): "Account locked" ke aayenge.
    - 0.05 (5% Chance): Sab se kam tickets "App crash" ke aayenge.

3. 1 lakh tickets ka random array generate karo:

    - np.random.seed(42)

4. Check karo first 10 tickets:

    - print(tickets[:10])

"""
)
```

# Uber Drive Example:

```py
import pandas as pd

df = pd.read_csv('uber.csv')

print("--- Aapki File Ka Data ---")
print(df)

print("\n--- Real Probabilities ---")
print(df['Issue_Type'].value_counts(normalize=True).map(lambda x: f"{x*100:.2f}%"))
```

```py
import numpy as np
from scipy import stats

marks = np.array([10, 12, 10, 15, 10, 18, 12])
mode_value = stats.mode(marks)
print("Mode:", mode_value.mode)   # 10
print("Number of Time:", mode_value.count)  # 3
```

# std() - Standard Deviation

> 1. ### Standard Deviation variance ka square root hota hai. Ye data ki spread ko original unit mein measure karta hai (variance square units mein hota hai, isliye intuitive nahi).

```py
import numpy as np

arr = np.array([10, 12, 11, 13, 14])
print(np.std(arr))   # Output: ~1.41
```

# Variance - Spreadness
> 1. ### Variance batata hai data mean se kitna door spread hai.

> 2. ### Variance batata hai ki data apni average se kitna door hai or iska answer square units mein aata hai.

```py
import numpy as np

data = [10, 20, 30, 40, 50]

print(np.var(data))
```