# How to Find Empty or Misssing Data?

## `isnull() | notnull()`
1. missing (NaN) values ko detect karte hain.
2. `True` matlab missing hai, `False` matlab value hai.
```py
import pandas as pd

data = pd.DataFrame({
    "Name": ["Ali", "Sara", "Umar", "Hina", "Bilal"],
    "Age": [22, 25, 28, 24, 30],
    "Salary": [50000, 55000, 60000, 52000, 75000],
    "Performance_Score": [88, 92, 76, 81, 95]
})

a = data["Salary"].isnull()

# yeah Salary Column ki info dyga jisme False likha ayga sub mein kue ka Salary Column ki sari value hai koi bhe Empty nahe hai ager Missing hoti tu True likha ata

a = data["Salary"].notnull()
# yeah bhe same hai bas yeah Oppsite result dyta hai means ka False ko True kardyga
```
## `isnull().sum()`
```py
import pandas as pd

data = pd.DataFrame({
    "Name": ["Ali", "Sara", None, "Hina", "Bilal"],
    "Age": [22, 25, 28, 24, 30],
    "Salary": [50000, None, 60000, 52000, 75000],
    "Performance_Score": [88, None, 76, 81, None]
})

a = data.isnull().sum()
# yeah saray Columns ki Missing value count karke batayga kch is terha se.

Name                 1
Age                  0
Salary               1
Performance_Score    2
dtype: int64


a = data.isnull().sum().sum()
# yeah Sara Column ki Missing Value Count karke oiska Total batayga -> 4


a = data["Salary"].isnull().sum()
# yeah Sirf Salary wala Column ki missing Value Count karayga -> 1


a = data[ data.isnull().any(axis=1) ]
# Output me sirf wo rows milengi jahan Value Missing hai.

```