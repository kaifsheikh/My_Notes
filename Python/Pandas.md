# 🐼 Pandas Guide — Easy Explanation (Markdown)

> 1. **Pandas** ek powerful Python library hai jiska kam tabular data (rows and columns) ko handle karne hai. <br>
> 2. Pandas se hum data ko read, clean, analyze, aur convert karne ke liye use hoti hai. <br>
> 3. Yeh Excel jaisi functionality code ke zariye provide karti hai — lekin fast aur automatable.
> 4. Simple words: **"Pandas = Python + Excel-like data handling"**

---

## 🔹 Pandas ka purpose (kya kaam karta hai)

* **Data Read Karna:** CSV, Excel, JSON, SQL se data load karna.
* **Data Clean Karna:** Missing values remove/replace karna, wrong data fix karna.
* **Data Analyze Karna:** Average, sum, filter, sort, group operations.
* **Data Convert Karna:** CSV ↔ Excel ↔ JSON ↔ SQL.
* **Data Show Karna:** Summaries aur charts ke liye prepare karna.

---

## 🔹 Pandas vs Excel (Easy Comparison)

| Feature      |                    Excel |                            Pandas |
| ------------ | -----------------------: | --------------------------------: |
| Interface    |    GUI (clicks & sheets) |            Code (Python commands) |
| Speed        | Slow for very large data |           Fast (millions of rows) |
| Automation   |              Manual work |           Scriptable / repeatable |
| Flexibility  |                  Limited |    Highly flexible & programmable |
| File Support |             Mostly Excel |       CSV, Excel, JSON, SQL, etc. |
| Best for     |      Quick small reports | Data analysis, pipelines, ML prep |

**Simple:** Excel = manual; Pandas = automatic & programmable.

---

## 🔹 Installation (How to install pandas)

1. Check Python installed:

```
python --version
```

2. Check pip installed:

```
pip --version
```

3. Install pandas:

```
pip install pandas
```

4. Verify:

```
pip show pandas
# or in Python
import pandas as pd
print(pd.__version__)
```
--- 

## 🔹 Pandas ke main data structures
## `Series`
> **Series**: Series ek single column data structure hai.
> Matlab ek hi type ka data ya mixed data ek line mein store hota hai. <br>
> Har item ka ek index (number) hota hai, jisse hum item ko access kar sakte hain.

## `Example 01 for Series`
```py
import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)
print(s[0]) # 10
```
## `DataFrame` 
> **DataFrame**: DataFrame 2-dimensional table hota hai (rows + columns) bilkul Excel ki terha Tablular form ki terha
---

## `Example 01 for DataFrame`
```py
import pandas as pd

data = {
    'Name': ['Ali','Sara','Umar'], 
    'Age': [22,25,20],
    'City': ['Lahore','Karachi','Multan']
} # yeah Dictionary hai Python mein

df = pd.DataFrame(data)

print(df)

# df = pd.DataFrame(data) -> DataFrame function dictionary ko table format mein convert karta hai.

# Isme teen keys hain: 'Name', 'Age', 'City'

# Har key ke paas ek list of values hai.
```
---

## Pandas Methods:
   
## `Examples: (File Save Different Formats)`

```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

# 1. DataFrame ko CSV file me save karna
df.to_csv("students.csv", index=False)

# 2. DataFrame ko Excel file me save karna
df.to_excel("students.xlsx", index=False)

# 3. DataFrame ko Json file me save karna
df.to_json("students.json", index=False)

# 4. index=False -> Isse Row Index Numbers ka Column (0,1,2...) nahi likhega.

# By Default yeah True hota hai jisa Row Index Number likha ate hai
```
## `Examples: (More Methods in Pandas)`

```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df.head()) # Pehli 5 rows dikhata hai
print(df.tail()) # Aakhri 5 rows dikhata hai
print(df.shape) # Kitni rows aur columns hain
print(df.info()) # Column aur datatype ki info 
print(df.describe()) # Numbers ka summary (avg, max, min)
print(df.dtype) # Datatype batata hai
print(df['Name'].dtype) # yeah Name ki Datatype batayga

print(df[["Name"]]) # yeah Name key ka sara Data dyga

print(df.loc[0]) # Index number ke zariye row access karta hai (label-based).

print(df.iloc[0]) # Index number ke zariye row access karta hai (Number-based).

print(df.columns) # Column ke naam dikhata hai
 
```

# How to Read Data in Pandas

