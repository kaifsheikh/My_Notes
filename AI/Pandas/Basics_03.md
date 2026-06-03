## 🔹 What is Data Structure in Pandas:
> 1. ### Data structure ka matlab hota hai data ko aise format mein rakhna jisse us par kaam karna easy ho. Pandas mein data ko table, column, row, ya labeled form mein store kiya jata hai, taa ke aap usay quickly access aur modify kar sako
> 2. ### Data structure batata hai ke bohat saara data kis format mein rakha gaya hai means.
> 3. ### Data structure 2 tarah ka hote hai.

## 🔹 Types of Data Structure in Pandas:
1. `Linear Data Structure`
    - Linear data structure woh hota hai jisme data ek seedhi line mein store hota hai. Yani ek element ke baad doosra, phir teesra — bilkul queue ya line ki tarah.
    - is terha ka data ko hum `1 Dimentional` data bhi bolte hai. 
    
2. `Non-Linear Data Structure`
    - Non-Linear Data Structure woh hota hai jisme data ek seedhi line mein store nahi hota hai. Yani data ko kisi tree, graph, ya kisi aur complex structure mein rakha jata hai.
    - is terha ka data ko hum `2 Dimentional` data bhi bolte hai. 

---

## `Series` (Linear Data Structure)
> 1. ### **Series**: Series ek single column data structure hai.
> 2. ### Matlab ek hi type ka data ya mixed data ek line mein store hota hai. jisa hum 1 Dimensional data bolte hai <br>
> 3. ### Har item ka ek index (number) hota hai, jisse hum item ko access kar sakte hain or index number 0 se start hota hai.

## `Examples for Series`
```py
import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)
print(s[0]) # 10
```

## `Series` - Custom Index Assign karna
```py
import pandas as pd
data = [10, 20, 30]
s = pd.Series(data, index=["a", "b", "c"])
print(s)
print(s['a']) # 10
print(s[['a' , 'b' , 'c']]) # 10 20 30
print(s['a':'c']) # a se lekar c tak ka sub data ayga
```

## `Series` - Multiple Value Fetch karna
```py
import pandas as pd
data = [10, 20, 30 , 30 , 45, 78, 78 , 100]
s = pd.Series(data)
print(s[[0,4]]) # 10 , 45
```

## `Series` - 0 se 4 tak sari values fetch karna
```py
import pandas as pd
data = [10, 20, 30 , 30 , 45, 78, 78 , 100]
s = pd.Series(data)
print(s[0:4]) # 10 , 20 , 30 , 30
```

## `Series` - Series ko List Datatype mein convert karna
```py
import pandas as pd
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
d = s.tolist()
print(d) # [10, 20, 30]
```

## `Series` - Series ko Dictionary Datatype mein convert kardyga
```py
import pandas as pd
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
d = s.to_dict()
print(d) # {'a': 10, 'b': 20, 'c': 30}
```

## `Series` - Checking if any Value Null so return TRUE if Not Null so return FALSE
```py
import pandas as pd
data = [10, 20, 30 , 30 , 45, 100, 78, 400]
s = pd.Series(data)
print(s.isnull()) # FALSE
```

## `Series` - Missing Values ko drop/delete karna

```py
import pandas as pd

# None likhne se Pandas isko khud hi missing value (NaN) samajh leta hai
data = [10, 20, None, 40, None, 50]
s = pd.Series(data)

# dropna() missing values ko list se hata dega
cleaned_s = s.dropna()
print(cleaned_s) 

```

## `Series` - Missing Values ko bina numpy ke kisi value se fill karna

```py
import pandas as pd

data = [10, 20, None, 40]
s = pd.Series(data)

# fillna() se None ki jagah koi bhi default number set karna
filled_s = s.fillna(0)
print(filled_s) # 10.0, 20.0, 0.0, 40.0

```

## `Series` - Duplicate values ko remove karna

```py
import pandas as pd

data = [10, 20, 20, 30, 10, 40]
s = pd.Series(data)

unique_s = s.drop_duplicates()
print(unique_s) # 10, 20, 30, 40

```

## `Series` - Kisi specific index ka data remove/delete karna

```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# drop() ke zariye kisi bhi label/index ka data delete kar sakte hain
s = s.drop("b")
print(s) # Sirf 'a' aur 'c' bachenge

```

## `Series` - Ek se zyada indexes ko ek sath delete karna

```py
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

# List ki surat mein multiple indexes pass karke delete karna
s = s.drop(["a", "c"])
print(s) # Sirf 'b' aur 'd' bachenge

```

## `Series` - Single value ko update karna

```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

s["b"] = 99
print(s) # 'b' ki jagah 99 ho jayega

```

## `Series` - Poori Series par ek sath math operation chala kar update karna

```py
import pandas as pd

s = pd.Series([10, 20, 30])

# Saari values mein ek sath 5 plus ho jayega
s = s + 5
print(s) # 15, 25, 35

```

## `Series` - Condition lagakar specific values ko update karna

```py
import pandas as pd

s = pd.Series([10, 50, 20, 60, 30])

# Jo values 30 se barhi hain, unki jagah 100 likh do
s[s > 30] = 100
print(s) # 10, 100, 20, 100, 30

```

## `Series` - Ek naya single record add karna

```py
import pandas as pd

s = pd.Series([10, 20], index=["a", "b"])

s["c"] = 30
print(s) # 'c' add ho jayega

```

## `Series` - Do mukhtalif Series ko aapas mein jodna (Add Multiple Records)

```py
import pandas as pd

s1 = pd.Series([10, 20], index=["a", "b"])
s2 = pd.Series([30, 40], index=["c", "d"])

combined_s = pd.concat([s1, s2])
print(combined_s)

```

## `Series` - Multiple conditions apply karke filter karna

```py
import pandas as pd

s = pd.Series([10, 25, 40, 55, 70])

# Jin values jo 20 se barhi hon AUR 60 se choti hon (& = AND)
filtered_s = s[(s > 20) & (s < 60)]
print(filtered_s) # 25, 40, 55

```

## `Series` - Aggregate Functions (Calculations karna)

```py
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s.sum())   # Total sum nikaalega (100)
print(s.mean())  # Average nikaalega (25.0)
print(s.max())   # Sab se barhi value (40)
print(s.min())   # Sab se choti value (10)
print(s.count()) # Khali jagah (None) ke ilawa total kitne items hain (4)

```

---

## `Array` (Linear Data Structure)
> 1. ### **Array**: mein hum Same type ka Data store karta hai isme Multi type ka data aik Array mein store nhe kar sekhte hai.

> 2. ### aik Array numbers ke liye bana hai, to usmein sirf numbers hoge yeah agar text ke liye bana hai, to oisme sirf text hoga.

> 3. ### Array ka size fixed hota hai means, array bante time usmein kitne values rekhne hai , woh pehle se decide karni padti hai bad mein oisme add nahe kar sekhte hai lakin old values ko update kar sekhte ha.

> 4. ### Array ki values ko hum Index Number se access kar sekhte hai or index number 0 se start hota hai.

## `Example 01 for Array` (Linear Data Structure)

```py
import pandas as pd

country = ["Pak", "India", "USA", "UK"]
final_data = pd.Series(country)

print(final_data)

# Output:
# 0      Pak
# 1    India
# 2      USA
# 3       UK
# dtype: object

# ---

import pandas as pd

country = ["Pak", "India", "USA", "UK"]
final_data = pd.array(country)

print(final_data)

# Output:
# <StringArray>
# ['Pak', 'India', 'USA', 'UK']
# Length: 4, dtype: string

# ---

import pandas as pd

arr = [10, 20, None, 40, None, 60]
clean_arr = pd.array(arr).dropna().tolist()
print(clean_arr)

# Output:
# [10, 20, 40, 60]

# ---

import pandas as pd

arr = [10, 20, 40, 60]
a = pd.array(arr)[0]
print(a) 

# Output:
# 10
```

---

## `DataFrame` 
> **DataFrame**: DataFrame 2-dimensional table hota hai (rows + columns) bilkul Excel ki terha Tablular form ki terha

## `Dataframe` - Dataframe create karna ka Process
```py
import pandas as pd

data = {
    'Name': ['Ali','Sara','Umar'], 
    'Age': [22,25,20],
    'City': ['Lahore','Karachi','Multan']
} # Dictionary

df = pd.DataFrame(data)
print(df)

# df = pd.DataFrame(data) -> DataFrame function dictionary ko table format mein convert karta hai.
# Isme teen keys hain: 'Name', 'Age', 'City'
# Har key ke paas ek list of values hai.
```

## `Dataframe` - Column create karne ka liya
```py
# --- Create Columns
import pandas as pd
data = [
    ["Ali", 20], # List 
    ["Sara", 22] # List
]

df = pd.DataFrame(data, columns=["name", "age"])
```

## `Dataframe` - Read Data in Dataframe

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
print(df.info()) # fetch full Summary
print(df.describe()) # yeah statistical Summary fetch karke deta hai
print(df.shape) # yeah Rows aur Columns ki full summary fetch karta hai
print(df.columns) # fetch all Columns
print(df.index) # show all Index numbers
print(df.dtypes) # Show all columns Datatypes
print(df.sample(n=2)) # Random Row show karta hai
print(df.memory_usage()) # Ram Memory ki Summary show karta hai

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
