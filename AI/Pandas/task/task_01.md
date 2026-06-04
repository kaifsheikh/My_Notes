# Task 01:

```py
import pandas as pd

student_names = ['ali', 'sara', 'zain', 'hina']

age_series = pd.Series([22, 24, 21, 25], index=student_names)
city_series = pd.Series(['Karachi', 'Lahore', 'Hyderabad', 'Islamabad'], index=student_names)
salary_series = pd.Series([50000, 60000, 45000, 70000], index=student_names)

series_dict = {
    'Age': age_series,
    'City': city_series,
    'Salary': salary_series
}

df = pd.DataFrame(series_dict)

print("--- Ali Ka Data ---")
print(df.loc[['ali']])
```