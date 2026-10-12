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

| Term                             | Simple                                                           | Example                                                                                                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`count`**                      | Total kitni values mojood hain (Missing values count nahi hoti). | Agar 3 students hain, toh count `3` hoga.                                                                                                                                                                                    |
| **`mean`**                       | Saari values ka average nikal kar deta hai.                      | Agar marks 60, 75, 90 hain, toh average `75` aayegi.                                                                                                                                                                         |
| **`Standard Deviation`** - (Std) | Data aapas mein kitna mukhtalif ya phaila hua hai.               | Agar std ki value choti hai tu means Sab values average ke qareeb hain tu iska matlab → data consistent hai <br><br> Agar std ki value bari hai means Values average se bohat door hain tu iska matlab → data phaila hua hai |
| **`min`**                        | Column ki sab se choti (minimum) value.                          | Sab se kam marks `60` hain.                                                                                                                                                                                                  |
| **`25%`**                        | 25% data is value se kam ya barabar hota hai.                    | Shuru ke 25% students is score se neeche hain.                                                                                                                                                                               |
| **`50%`**                        | Bilkul beech ki value (Median).                                  | Aadhe students is se upar aur aadhe neeche hain (`75`).                                                                                                                                                                      |
| **`75%`**                        | 75% data is value se kam ya barabar hota hai.                    | 75% students is score ya is se kam par hain.                                                                                                                                                                                 |
| **`max`**                        | Column ki sab se bari (maximum) value.                           | Sab se zyada marks `90` hain.                                                                                                                                                                                                |

# `25%` - full explain:

## Example:

1. **Step 01**: yeah original marks hai abhe iski sorting nhe hue ve hai subse phela hum isko **ascending order** mein karengay.

```py
'Marks': [
        45, 78, 92, 33, 67, 88, 54, 91, 72, 85,
        61, 79, 48, 95, 38, 82, 59, 74, 98, 41,
        66, 81, 70, 52, 89, 44, 76, 63, 94, 55,
        87, 39, 73, 60, 96, 50, 83, 69, 57, 90,
        47, 75, 84, 51, 99, 42, 68, 77, 86, 62,
        93, 40, 80, 53, 71, 65, 49, 97, 56, 85,
        43, 78, 64, 58, 82, 37, 72, 90, 46, 89,
        55, 67, 91, 35, 79, 88, 61, 74, 52, 95,
        44, 86, 63, 70, 98, 50, 81, 69, 59, 76,
        41, 84, 66, 92, 48, 75, 87, 54, 83, 60
    ]
```

---

2. ab yeah marks actual `ascending order` mein hogay hai kch is terha se.
3. ab humne 33 se 25 tak bilkul sequence mein count karna hai `ascending order` wale numbers ko tu 24 number per value ati hai `53` or 25 number per value ati hai `54`
   - means `24th` number per hai → **53**
   - means `25th` number per hai → **54**

```py
[
    33, 35, 37, 38, 39, 40, 41, 41, 42, 43,
    44, 44, 45, 46, 47, 48, 48, 49, 50, 50,
    51, 52, 52, 53, 54, 54, 55, 55, 56, 57,
    58, 59, 59, 60, 60, 61, 61, 62, 63, 63,
    64, 65, 66, 66, 67, 67, 68, 69, 69, 70,
    70, 71, 72, 72, 73, 74, 74, 75, 75, 76,
    76, 77, 78, 78, 79, 79, 80, 81, 81, 82,
    82, 83, 83, 84, 84, 85, 85, 86, 86, 87,
    87, 88, 88, 89, 89, 90, 90, 91, 91, 92,
    92, 93, 94, 95, 95, 96, 97, 98, 98, 99
]
```

4. tu **describe()** function bhe isi terha kam karta hai or jo value **25th number** per ati hai wo show kar deta hai bs.

5. iska matlab hua ka **25% percent Students** ka marks **54 ka equal** hai yeah **54 se less than** hai bs.

6. same is terha terha **75%** percent nikalta hai

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
