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

# median() - Median value
> 1. ### yeah Numbers ko chote se bade mein Arrange / Sort karta hai Ascending Order mein phir jo bhe number bilkul center mein ayga oisa Median bolte hai.

> 2. ### yeah Normal Average ki terha he hota hai yeah oisa alag hota hai

```py
print(

    """
    Koi baat nahi, bilkul aasan lafzon mein samajhte hain. Statisticians aur data scientists **Median** ko sabse bharosemand darmiyani qeemat (middle value) kyun maante hain, isko step-by-step dekhte hain.

---

## Median Ki Proper Definition (Aasan Urdu Mein)

> **Definition:** Jab aap kisi data (numbers ki list) ko chote se bare ki taraf (Ascending Order) mein aik line se lagate hain, to jo number **bilkul center (darmiyan) mein** aata hai, use **Median** kehte hain.

Iska maqsad yeh hota hai ke aap ke aadhe (50%) numbers is median se chote hote hain, aur aadhe (50%) numbers is se bare hote hain. Yeh data ko barabar do hisson mein kaat deta hai.

---

## Simple Maths Formula (Easy Method)

Median nikalne ke do simple tareeqe hain, jo is baat par depend karte hain ke aap ke paas kul kitne numbers hain (Total items = $n$).

### Case 1: Agar Total Numbers Odd (Taaq) hon — Jaise 3, 5, 7, 9...

Iska formula bht simple hai. Aap line mein khare sabse center wale number ko utha lete hain:

$$\text{Median} = \left(\frac{n + 1}{2}\right)\text{th term}$$

**Example:** Agar 5 numbers hain, to $\frac{5+1}{2} = 3$rd (teesra) number aap ka median hoga.

### Case 2: Agar Total Numbers Even (Juft) hon — Jaise 4, 6, 8, 10...

Kyunke even numbers mein bilkul center mein koi aik number nahi hota, balki do numbers hote hain. Isliye hum **center ke do numbers ka average (mean)** nikalte hain:

$$\text{Median} = \frac{\left(\frac{n}{2}\right)\text{th term} + \left(\frac{n}{2} + 1\right)\text{th term}}{2}$$

**Example:** Agar 4 numbers hain, to 2nd aur 3rd number ko jama kar ke 2 se divide kar denge.

---

## Manual Maths Examples (Step-by-Step)

Aayein dono cases ko haath se solve kar ke dekhte hain taake dimaag mein baith jaye.

### Example 1: (Odd Numbers ka Case)

Farz karein aap ke paas 5 doston ki umar (ages) hain: `[12, 15, 10, 19, 11]`

* **Step 1: Data ko chote se bara arrange karein (Sort):**
`[10, 11, 12, 15, 19]`
* **Step 2: Center wala number dhoondein:**
Yahan Kul numbers $n = 5$ hain. Formula ke mutabiq: $\frac{5+1}{2} = 3$rd term.
Teesra number hai **12**.
* **Result:** Median = **12**

### Example 2: (Even Numbers ka Case)

Farz karein ab doston ki tadad 6 ho gayi hai: `[12, 15, 10, 19, 11, 22]`

* **Step 1: Data ko chote se bara arrange karein (Sort):**
`[10, 11, 12, 15, 19, 22]`
* **Step 2: Center ke do numbers dhoondein:**
Yahan center mein do numbers hain: **12** aur **15** (do iske left par hain, do right par).
* **Step 3: Dono ka average nikalein:**

$$\text{Median} = \frac{12 + 15}{2} = \frac{27}{2} = 13.5$$


* **Result:** Median = **13.5**

---

## Python Numpy Code (Dono Cases Ka)

Ab isi maths ko NumPy ke zariye code mein dekhte hain ke woh kaise handle karta hai:

```py
import numpy as np

# Case 1: Odd numbers wala data
data_odd = np.array([12, 15, 10, 19, 11])
print("Odd Data ka Median:", np.median(data_odd))  
# Output: 12.0

# Case 2: Even numbers wala data
data_even = np.array([12, 15, 10, 19, 11, 22])
print("Even Data ka Median:", np.median(data_even))  
# Output: 13.5

```

---

## Asal Use: Hamein Median ki Zaroorat Kyun Pari? (The "Why")

Aap soch rahe honge ke hum sab numbers ko jama kar ke total se divide bhi to kar sakte the (jise Mean ya Average kehte hain). Hum ne itni mehnat se center wala number kyun dhoonda?

Aayein aik real story se samajhte hain.

### Ek Real-World Kahani:

Farz karein aik choti company hai jahan 4 employees kaam karte hain aur unki tankhwah (salary) yeh hai:

* Employee 1: **Rs. 30,000**
* Employee 2: **Rs. 35,000**
* Employee 3: **Rs. 40,000**
* Employee 4: **Rs. 45,000**

Inki **Mean (Average)** salary hogi: $\frac{30+35+40+45}{4} =$ **Rs. 37,500**. Yeh bilkul sahi batati hai ke wahan aam taur par logon ko kya mil raha hai.

**Twist:** Ab us company mein aik naya **CEO** aata hai, jis ki salary hai **Rs. 1,000,000 (10 Lakh)**. Now the data is: `[30000, 35000, 40000, 45000, 1000000]`

Ab agar hum **Mean (Average)** nikalenge:


$$\text{Mean} = \frac{30000 + 35000 + 40000 + 45000 + 1000000}{5} = \textbf{Rs. 230,000}$$

Agar koi bahar ka banda yeh dekhega to sochega, *"Wah! Is company mein har bande ko taqreeban 2 Lakh se zyada milte hain."* Jo ke bilkul jhoot hai! Baqi log to abhi bhi 30-40 hazar par hain. Is 10 Lakh wale number ko data science mein **Outlier** (Anokha Number) kehte hain jo average ko kharab kar deta hai.

### Yahan Kaam Aata Hai Median:

Agar hum isi naye data ka **Median** nikalen:

1. Data sorted hai: `[30000, 35000, 40000, 45000, 1000000]`
2. Center wala number dhoondein: **40,000**

Median aaya **Rs. 40,000**. Dekha aapne? CEO ke 10 Lakh aane ke baad bhi Median ne dhoka nahi diya aur company ki bilkul sachi aur darmiyani tasveer pesh ki.

### Proper Real-Time Uses:

1. **Salary Surveys:** Jab dunya mein mulkon ki aamdani check hoti hai, to hamesha **Median Income** dekhi jati hai taake Elon Musk ya Bill Gates jaise ameeron ki wajah se aam awam ka data kharab na dikhe.
2. **Gharon ki Qeematen (Real Estate):** Kisi ilaqe mein gharon ka rate check karne ke liye Median price dekhi jati hai, taake wahan majood kisi aik aadhi bht bari kothi (Mansion) ki wajah se baqi chote gharon ka rate asman par na dikhe.

Ab batao, kya ab Median ka concept bilkul crystal clear hua?
    """
)
```

```py
import numpy as np

arr = np.array([1, 2, 3, 100, 200])
print(np.median(arr))   # Output: 3.0 (Middle Value)
```

```py
import numpy as np

salary = [20000,25000,30000,500000]

print(np.median(salary)) # 27500

```

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


