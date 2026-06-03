
# How to Read Data in Pandas in Different Formats
1. Pandas mein data read karne ke liye alag-alag functions hote hain.
2. depend karta hai data kis format mein hai.

| File Type    | Function          | Example                                          |
| ------------ | ----------------- | ------------------------------------------------ |
| CSV file     | `pd.read_csv()`   | `pd.read_csv("data.csv")`                        |
| Excel file   | `pd.read_excel()` | `pd.read_excel("data.xlsx")`                     |
| JSON file    | `pd.read_json()`  | `pd.read_json("data.json")`                      |
| SQL database | `pd.read_sql()`   | `pd.read_sql("SELECT * FROM table", connection)` |
| Text file    | `pd.read_table()` | `pd.read_table("data.txt")`                      |

---

## `read_csv` - Dataframe mein CSV file load karne ke liye

```py
# Read CSV File Data
import pandas as pd
df = pd.read_csv("tested.csv")
```

## `isnull.sum()` - Missing values (Null) find karta hai or total missing values count karke batata hai pure table mein se.

```py
import pandas as pd
df = pd.read_csv("data.csv" , encoding='latin1')

null_counts = df.isnull().sum()
print(null_counts) 
```

## `df['column_name'].isnull().sum()` - Kisi Aik Specific Column Ki sirf Null Values ko Count Karne Ke Liye

```py
import pandas as pd
df = pd.read_csv("data.csv" , encoding='latin1')

customer_null_count = df["column_name"].isnull().sum()
print(customer_null_count)
```

## `df['column_name'].isnull().sum()` - kisi specific column mein se sari null values ka index number find karke dega yeah

```py
import pandas as pd

df = pd.read_csv("data.csv", encoding="latin1")

null_description_indices = df[df["Description"].isnull()].index

print(list(null_description_indices))
```

## `` - ager kisi sequence mein jaise ka starting ending yeah kisi number se kisi dosre number ka ka null values find karne ka liya.

```py
import pandas as pd
df = pd.read_csv("data.csv", encoding="latin1")

null_description_indices = list(df[df["Description"].isnull()].index)

first_10 = null_description_indices[:10] # starting ka 10 null values find karke dega
print(first_10)

# ==========

import pandas as pd
df = pd.read_csv("data.csv", encoding="latin1")

null_description_indices = list(df[df["Description"].isnull()].index)

last_10 = null_description_indices[-10:] # Last ka 10 null values find karke dega
print(last_10)

# ==========

import pandas as pd
df = pd.read_csv("data.csv", encoding="latin1")

null_description_indices = list(df[df["Description"].isnull()].index)

specific_range = null_description_indices[20:50] # 20 se 50 tak null values find karke deta hai
print(specific_range)
```

## `fillna()` - sirf Null values ko fixed value provide karayga sirf

> 1. ### `inplace=True` lagane se aap ka original table/dataframe ka andar he update ho jata hai or yeah kch return bhe nhe karta hai.

```py
import pandas as pd
df = pd.read_csv("tested.csv" , encoding='latin1')

a = df["CustomerID"].fillna(00000, inplace=True)
print(a)
```

## `fillna()` - Null values ko kisi specific value se update/fill karne ke liye use hota hai

> 1. ### yeah kisi specific column ki sari null values ko 12 mein update kar dyga sirf null values ko

```py
import pandas as pd
df = pd.read_csv('data.csv' , encoding='latin1')

df['column_name'] = df['column_name'].fillna(12)
null_counts = df.isnull().sum()

print(null_counts)
```

## `fillna()` - Har column ke liye alag alag fixed value karne ka liya 

> 1. ### Real-time mein hamare paas aik sath bohot saaray columns hote hain. Agar aap chahte hain ke aik hi line mein CustomerID mein 0000 chala jaye, Description mein 'Unknown' chala jaye toh hum dictionary pass karte hain.

```py
import pandas as pd
df = pd.read_csv('data.csv' , encoding='latin1')

fill_rules = {
    "column_name": 0000,
    "column_name": "Unknown"
}

df = df.fillna(value=fill_rules)

null_counts = df.isnull().sum()

print(null_counts)
```



## Example 01:

```py
# Read Excel File Data
import pandas as pd
df = pd.read_excel("tested.xlsx")
print(df)

# ______________________

# Read Json File Data
import pandas as pd
df = pd.read_json("tested.json")
print(df)

# ______________________

# Read SQL File Data
import pandas as pd
df = pd.read_sql("SELECT * FROM table", connection)
print(df)

# ______________________

# Read Table File Data
import pandas as pd
df = pd.read_table("tested.txt")
print(df)
```