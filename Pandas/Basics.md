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
## `Examples:  (Accessing Rows)`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df.loc[0]) # Index number ke zariye row access karta hai (label-based).
print(df.iloc[0]) # Index number ke zariye row access karta hai (Number-based).
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
