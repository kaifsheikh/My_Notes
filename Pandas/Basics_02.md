## 🔹 Pandas ke main data structures
## `Series`
> **Series**: Series ek single column data structure hai.
> Matlab ek hi type ka data ya mixed data ek line mein store hota hai. jisa hum 1 Dimensional data bolte hai <br>
> Har item ka ek index (number) hota hai, jisse hum item ko access kar sakte hain or index number 0 se start hota hai.

## `Example 01 for Series`
```py
import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)
print(s[0]) # 10

# --- Custom index
import pandas as pd
data = [10, 20, 30]
s = pd.Series(data, index=["a", "b", "c"])
print(s)
print(s['a'])

# --- Multiple Value Fetch
import pandas as pd
data = [10, 20, 30 , 30 , 45, 78, 78 , 100]
s = pd.Series(data)
print(s[[0,4]]) # 10 , 45

# --- 0 se 4 tak sari values fetch honge
import pandas as pd
data = [10, 20, 30 , 30 , 45, 78, 78 , 100]
s = pd.Series(data)
print(s[0:4]) # 10 , 20 , 30 , 30

# --- Fetch with condition
import pandas as pd
data = [10, 20, 30 , 30 , 45, 78, 78 , 100]
s = pd.Series(data)
print(s[s > 78]) # 100 

# --- Checking if any Value Null so return TRUE if Not Null so return FALSE
import pandas as pd
data = [10, 20, 30 , 30 , 45, 100, 78, 400]
s = pd.Series(data)
print(s.isnull()) # FALSE

# --- Series ko Dictionary Datatype mein convert kardyga
import pandas as pd
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
d = s.to_dict()
print(d) # {'a': 10, 'b': 20, 'c': 30}

# --- Series ko List Datatype mein convert kardyga
import pandas as pd
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
d = s.tolist()
print(d) # [10, 20, 30]
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

# --- Create Columns
import pandas as pd
data = [
    ["Ali", 20],
    ["Sara", 22]
]

df = pd.DataFrame(data, columns=["name", "age"])


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

## `Examples: (Basic Data Viewing)`

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
 
```

## `Examples: (Structure and Summary)`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df.shape) # Kitni rows aur columns hain
print(df.info()) # Column aur datatype ki info 
print(df.describe()) # Numbers ka summary (avg, max, min)
print(df.columns) # Column ke naam dikhata hai

```

## `Examples: (Data Types)`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df.dtype) # Datatype batata hai
print(df['Name'].dtype) # yeah Name ki Datatype batayga
```

## `Examples:  (Selecting Columns)`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df["Name"]) # yeah Single Column means Name key ka sara Data dyga 
print(df[["Name" , "Age"]]) # Ager multiple Columns dehkne ho tu oiska sara Data dyga
```
# Row Column and Index Number `(Accessing Rows)`

| Term (Naam) | Matlab (Simple Words)                          | Example (Table me kya hota hai) | Yaad Rakhne ka Easy Trick |
| ----------- | ---------------------------------------------- | ------------------------------- | ------------------------- |
| **Column**  | Data ka **vertical part** (upar se neeche tak) | Jaise “Name”, “Age”, “City”     | Column = **Heading**      |
| **Row**     | Data ka **horizontal part** (ek line)          | Jaise “Ali – 22 – Lahore”       | Row = **Record**          |
| **Index**   | Har row ka **number ya ID**                    | 0 (Ali), 1 (Sara), 2 (Umar)     | Index = **Row ka number** |

## `loc[] -> ()`
1. loc[] ek function (tool) hai.
2. jo DataFrame me se row aur column ka data “naam se” or (Index Number se) nikalta hai.
```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

a = df.loc[1, "Name"] # Name Column se Index 1 ka data ayga -> Shayan

a = df.loc[1]       # Row 1 ka sara Data ayga
a = df.loc[[0 , 2]] # sirf 0 or 2 wali Row ka sara data ayga 
a = df.loc[0 : 2]   # 0 se 2 tak ki sari Rows ka data ayga 

a = df.loc[: , "Name"]          # Name Column ka sara Data ayga
a = df.loc[:, ["Name" , "Age"]] # Name or Age Column ka sara Data milayga


a = df.loc[0:5, ["Name" , "Age"]] # Name or Age Column ka data milayga lakin 0 se 5 tak ki rows ka sirf

print(a)
```
## `Examples: describe()`

1. Ye function DataFrame ke numbers ka summary deta hai

```py
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Umar'],
    'Marks': [75, 90, 60]
})

# Output:
 
+-------+---------+
|       |   Marks |
+=======+=========+
| count |     3   |
+-------+---------+
| mean  |    75   |
+-------+---------+
| std   |    15   |
+-------+---------+
| min   |    60   |
+-------+---------+
| 25%   |    67.5 |
+-------+---------+
| 50%   |    75   |
+-------+---------+
| 75%   |    82.5 |
+-------+---------+
| max   |    90   |
+-------+---------+ 


| **count**        | Kitni values hain column mein        | Yahan `3` hain → 3 students ke marks                                                          |
| **mean**         | Average value                        | (60 + 75 + 90) / 3 = **75**                                                                   |
| **std**          | Standard deviation                   | Ye batata hai ke numbers kitne farq mein hain (variation) — jitna zyada std, utna data spread |
| **min**          | Sabse chhoti value                   | **60** lowest marks                                                                           |
| **25%**          | 25 percent data ke neeche wali value | **67.5**                                                                                      |
| **50% (Median)** | Beech wali value                     | **75**                                                                                        |
| **75%**          | 75 percent data ke neeche wali value | **82.5**                                                                                      |
| **max**          | Sabse badi value                     | **90**                                                                                        |
```
