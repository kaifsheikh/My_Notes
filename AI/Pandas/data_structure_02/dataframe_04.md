
# DataFrame: 

1. **DataFrame** 2-dimensional table hota hai jisme **rows** + **columns** bilkul Excel ki terha Tablular form mein hote hai.

---

# Row Column and Index Number `(Accessing Rows)`

| Term (Naam) | Matlab (Simple Words)                          | Example (Table me kya hota hai) | Yaad Rakhne ka Easy Trick |
| ----------- | ---------------------------------------------- | ------------------------------- | ------------------------- |
| **Column**  | Data ka **vertical part** (upar se neeche tak) | Jaise “Name”, “Age”, “City”     | Column = **Heading**      |
| **Row**     | Data ka **horizontal part** (ek line)          | Jaise “Ali – 22 – Lahore”       | Row = **Record**          |
| **Index**   | Har row ka **number ya ID**                    | 0 (Ali), 1 (Sara), 2 (Umar)     | Index = **Row ka number** |

---

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

---

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

# ---

print(df.dtype) # Datatype check karne ka liya
print(df['Name'].dtype) # kisi column ka datatype check karne ka liya

# ---

print(df["Name"]) # Name column ka sara data fetch hoga. 
print(df[["Name" , "Age"]]) # Multiple Columns ka sara data fetch hoga.
```

---

## `Examples: (File Save Different Formats)`

1. index=False -> Isse Row Index Numbers ka Column (0,1,2...) nahi likhega. By Default yeah True hota hai jisa Row Index Number likha ate hai

2. `pip install openpyxl` yeah excel ka liya use hone wala package hai.

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
```

---

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

a = df.loc[1] # Row 1 ka sara Data ayga

a = df.loc[[0 , 2]] # sirf 0 or 2 wali Row ka sara data ayga 

a = df.loc[0 : 2] # 0 se 2 tak ki sari Rows ka data ayga 

a = df.loc[: , "Name"] # Name Column ka sara Data ayga

a = df.loc[:, ["Name" , "Age"]] # Name or Age Column ka sara Data milayga

a = df.loc[0:5, ["Name" , "Age"]] # Name or Age Column ka data milayga lakin 0 se 5 tak ki rows ka sirf

a = df.loc[df["Age"] > 10] # wo saray log fetch honge jinki age 10 se greater hai.

df.loc[1, "Age"] = 25 # sirf age column se index 1 ka data ayga.

df.loc[:, "Country"] = "Pakistan" # new column add karna or oisme default value Pakistan set karna ho

df.loc[3] = ["Ali", 22, "Multan"] # new row add karne ho with values.

print(a)
```

---

```py
import pandas as pd

data = {
    "Name": ["Ali", "Shayan", "Smith"],
    "Age": [10, 11, 30],
    "City": ["Hyd", "Karachi", "Lahore"]
}

# Pehle Name ko index bana lein
df.set_index("Name", inplace=True)

# Ab seedha naam se data nikal sakte hain
a = df.loc["Ali", "Age"]  # Ali ki age mil jaye gi
```

---

## `describe()` - Example

1. Pandas ka **describe()** function aik buhat hi powerful aur useful tool hai. Jab aap ke paas bara data ho aur aap ko poore data ka aik nazar mein statistical summary chahiye ho, toh yeh function sab se best hai.

2. By default, yeh function DataFrame ke tamam numerical columns (jin mein numbers hote hain) par kaam karta hai aur unka mukammal data profile la kar deta hai.

```py
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Umar'],
    'Marks': [75, 90, 60]
})

df.describe()

print(a)

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
```

| Term | Simple Matlab (Asaan Alfaaz mein) | Misal (Example) |
| --- | --- | --- |
| **`count`** | Total kitni values mojood hain (Missing values count nahi hoti). | Agar 3 students hain, toh count `3` hoga. |
| **`mean`** | Saari values ki average nikal kar deta hai. | Agar marks 60, 75, 90 hain, toh average `75` aayegi. |
| **`std`** | Data aapas mein kitna mukhtalif ya phaila hua hai. | Agar sab ke marks qareeb hain toh `std` kam hogi. |
| **`min`** | Column ki sab se choti (minimum) value. | Sab se kam marks `60` hain. |
| **`25%`** | 25% data is value se kam ya barabar hota hai. | Shuru ke 25% students is score se neeche hain. |
| **`50%`** | Bilkul beech ki value (Median). | Aadhe students is se upar aur aadhe neeche hain (`75`). |
| **`75%`** | 75% data is value se kam ya barabar hota hai. | 75% students is score ya is se kam par hain. |
| **`max`** | Column ki sab se bari (maximum) value. | Sab se zyada marks `90` hain. |

---

1. **describe()** sirf numbers wale columns par chalta hai. Agar aap ke paas names, cities, ya categories wala data hai aur aap dekhna chahte hain ke total kitne unique names hain ya sab se zyada baar kaun sa naam aaya hai yah bhe bta dayga. 

```py 
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Umar'],
    'Marks': [75, 90, 60]
})

a = df.describe(include=['object']) # sirf Object data ki summary ayge.

a = df.describe(include='all') # pure data ki summary ayge

a = df['Name'].describe() # sirf Name wale column ka data ayga

print(a)
```

