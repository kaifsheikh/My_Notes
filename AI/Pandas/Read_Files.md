
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

## Example 01:

```py
# Read CSV File Data
import pandas as pd
df = pd.read_csv("tested.csv")
print(df)

# ______________________

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