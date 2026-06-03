# 🐼 Pandas DataTypes

> 1. ### Datatype batata hai ke ek value kis qisam ki hai.

# 🐼 Pandas Datatypes:

| Data Type          | Example        | Means                                            | Use / Kab use hota hai                                    |
| ------------------ | -------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| **int64**          | 10, 25, 100    | Ye pure numbers hote hain jisme point (.) nahi hota.           | Jab hum counting ya age jese numbers store karte hain.    |
| **float64**        | 10.5, 99.9     | Ye decimal numbers hote hain, yani point ke sath wale numbers. | Jab hum marks, prices ya measurements store karte hain.   |
| **String / objects**        | "Hello World"     | yeah text hota hai jisko Double quotes("") ya single quotes('') mein likha jata hai.  | Jab hum names, cities, ya koi text data store karte hain.   |
| **bool**           | True, False    | Ye logical values hote hain (Yes/No jese).                     | Jab hume check karna ho ke koi cheez true hai ya false.   |
| **datetime64[ns]** | 2025-11-04     | Ye date aur time ko represent karta hai.                       | Jab hum date ya time ke sath kaam karte hain.             |
| **timedelta64[ns]** | 2025-11-04     | Ye date ka fark ko represent karta hai.                       | jab do dates kay darmiyan time diff ko store karna hu |  
| **category**       | Male, Female   | Ye fixed ya limited values hoti hain jo repeat hoti hain.      | Jab hum gender, city type ya class jese data rakhte hain. |

---

## Datatype Examples:

1. Datatypes in Pandas

```py
import pandas as pd

age = 25
price = 99.99
city = 'Karachi'
is_logged_in = True

print(age)
print(price)
print(city)
print(is_logged_in)

print(type(age))
print(type(price))
print(type(city))
print(type(is_logged_in))

```

## `Datetime` Examples:
> 1. ### Jab aap ko timeline par kisi ek specific din ko point karna ho. Is mein years, months, Days, or Time shamil hota hai.

```py
import pandas as pd
date = pd.to_datetime("2026-12-25") # Specific date
```

## `Timedelta` Examples:
> 1. ### Yeh koi tareekh ya calendar ka din nahi hota. Yeh do waqt ke darmiyan ka gap (faasla) hota hai. Is mein sirf ginti hoti hai ke kitne din, kitne ghante ya kitne minutes guzre.

```py
today_date = pd.to_datetime("2026-06-01")
after_date = pd.to_datetime("2026-12-25")

final = after_date - today_date # 207 days 00:00:00
```

## `datetime` Examples:
1. 

```py
from datetime import datetime
today = datetime.now()
print(today) # 2026-06-01 06:00:32.560009

# ---

from datetime import date
today = date.today()
print(today) # 2026-06-01

# ---

from datetime import datetime
today = datetime.now()
good_format = today.strftime("%d %B, %Y")
print(good_format) # 01 June, 2026

```

## `Category` in Pandas:
> 1. ### Jab humera paas koi aesa text yeah data ho jisme values limited hoon aur baar baar repeat ho rahi hoon, toh use hum category kehte hain.

> 2. ### Gender: Male, Female, Male, Male, Female... (Sirf do-teen options hain jo repeat ho rahe hain).

```py
import pandas as pd

genders = ["Male", "Female", "Female", "Male", "Male"] # List

gender_series = pd.Series(genders) # convert into Series

gender_category = gender_series.astype('category') # Series into category type

print(gender_category)

```

> 1. ### `.astype()` -> means Type Casting ya Data Type Converter.
> 2. ### Yeh Pandas ka ek built-in function (tool) hai jiska putpose ha kisi bhi column ka data type ko (explicitly) change karna hota hai. Aap computer ko order dete hain ke: "Abhi is column ka jo bhi data type hai, use bhool jao aur isko is naye data type mein badal do."

---

```py
import pandas as pd
from pandas.api.types import CategoricalDtype

sizes = ["Medium", "Small", "Large", "Small", "Medium"] # List

s_series = pd.Series(sizes) # Convert into Series

size_order = CategoricalDtype(categories=["Small", "Medium", "Large"], ordered=True)

ordered_sizes = s_series.astype(size_order) # Series into Categories with Order

print(ordered_sizes.sort_values())
```

> 1. ### `CategoricalDtype(...)`: Aap computer ko bata rahe hain ke main ek naya, custom data type design kar raha hoon.

> 2. ### `categories=["Small", "Medium", "Large"]`: Aap ne computer ko bataya ke is column mein sirf aur sirf yeh teen lafaz hi aa sakte hain. Inke alawa agar koi aur lafaz aaya (jaise "Extra-Large"), toh use reject kar dena.

> 3. ### `ordered=True`: computer ko nahi pata ke Small chota hota hai aur Large bara hota hai. Jab aap ne ordered=True likha, toh aap ne computer ko bola ka Is list mein jo lafaz jis order mein likha hai, woh waisa hi show hone chaiya."