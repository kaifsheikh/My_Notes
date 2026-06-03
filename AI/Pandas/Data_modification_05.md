# How to Modify Data in Pandas:

## `Example 01:`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Sara", None, "Hina", "Bilal"],
    "Age": [22, 25, 28, 24, 20],
    "Salary": [None, 59000, None, 52000, "75000"],
    "Performance_Score": [88, 69, 76, 81, 20]
}

df = pd.DataFrame(data) # Dictionary <-> DataFrame

# Salary Column ka Index 0 wali Value change hoge jaha per None likh hua hai
a = df.loc[0 , "Salary"] = 30000

# isa pure Age wale Column ki Age change hojayge
a = df["Age"] = [30 , 20 , 40 , 56 , 78] 

# isa Age wale Column mein aik he Value sari Rows mein ajayge jasie 18
a = df["Age"] = [18] 

# jiski bhe Age 25 se Greater yeah Equal hue tu oiski Age Update hokar 50 hojayge
a = df.loc[ df["Age"] >= 25 , 'Age' ] = 50 

# jiska naam Ali & Age 22 hai oiski Age ko Update karke 50 kardu
a = df.loc[ (df["Name"] == "Ali") & (df['Age'] == 22) , "Age" ] = 50

# Name Column ka Rename hokar FullName hojayga
a = df.rename(columns = { 'Name': 'FullName' }, inplace=True)

print(a)
```

# How to Drop Column and Rows
## `Examples 01:`
```py
import pandas as pd

data = {
    "Name": ["Ali", "Sara", None, "Hina", "Bilal"],
    "Age": [22, 25, 28, 24, 20],
    "Salary": [None, 59000, None, 52000, "75000"],
    "Performance_Score": [88, 69, 76, 81, 20]
}

df = pd.DataFrame(data) # Dictionary <-> DataFrame

# yeah pure 1 Row ko Delete karayga
a = df.drop(1, inplace=True)

# yeah pure Name Column ko Delete karayga
a = df.drop("Name", axis=1, inplace=True)

| **Value**         | **Matlab (Meaning)**                   | **Example (Use Case)**             |
|-------------------|----------------------------------------|------------------------------------|
| `axis=0`          | Rows par kaam ho rah hai              | Row delete karni ho                |
| `axis=1`          | Columns par kaam ho raha hai           | Column delete karna ho             |
| `inplace=False`   | Naya copy return karta hai             | Original data change nahi hota     |
| `inplace=True`    | Original data ko hi modify karta hai   | Data permanently change hota hai   |
```
