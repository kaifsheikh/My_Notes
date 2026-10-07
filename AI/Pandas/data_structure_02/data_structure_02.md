# 🔹 What is Data Structure in Pandas:
1. Data ko computer ki memory mein arrange aur organize karne ka tareeqa hai isa hum Data Structure bolte hai means.

2. **Data structure** ka matlab hota hai data ko aise format mein rakhna jisse us par kaam karna easy ho.

3. tu Pandas mein data ko **table** **column** **row** ya **labeled** ki form mein store kiya jata hai, taa ke aap usay quickly **access** aur **modify** **add** yeah delete kiya ja sekhe.

4. Data structure batata hai ke bohat saara data kis format mein rakha gaya hai.

5. Data structure 2 tarah ka hote hai.

# 🔹 Types of Data Structure in Pandas:
1. **`Linear Data Structure`**
    - Linear data structure woh hota hai jisme data ek seedhi line mein store hota hai. Yani ek element ke baad doosra, phir teesra — bilkul queue ya line ki tarah.
    - is terha ka data ko hum `1 Dimentional` data bhi bolte hai. 
    
2. **`Non-Linear Data Structure`**
    - Non-Linear Data Structure woh hota hai jisme data ek seedhi line mein store nahi hota hai. Yani data ko kisi tree, graph, ya kisi aur complex structure mein rakha jata hai.
    - is terha ka data ko hum `2 Dimentional` data bhi bolte hai. 

---

# `Series` - Linear Data Structure
1. **Series**: Series ek single column data structure hai means.

2. Series ek hi type ka data ya mixed data ko ek he line mein store karta hai. jisa hum **1 Dimensional** data bolte hai.

3. Har item ka ek **index number** hota hai, jisse hum item ko access kar sakte hain or index number 0 se start hota hai.

## `Series` - Examples
```py
import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)
print(s[0])

# ---

import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

## `Series` - Custom Index Assign karna
```py
import pandas as pd

data = [10, 20, 30]

s = pd.Series(data, index=["a", "b", "c"])

print(s)

print(s['a'])

print(s[['a' , 'b' , 'c']])

print(s['a':'c']) # a se lekar c tak ka sub data ayga
```

## `Series` - Specific Multiple Values Fetch karna
```py
import pandas as pd

data = [10, 20, 30 , 30 , 45, 78, 78 , 100]

s = pd.Series(data)

print(s[[0,4]]) # 10 , 45
```

## `Series` - 0 se 4 tak sari values fetch hoge

1. ager hum **0:5** likhte hai tu yeah **0 se 4** tak jayga means 1 number less.

```py
import pandas as pd

data = [10, 20, 30 , 30 , 45, 78, 78 , 100]

s = pd.Series(data)

print(s[0:4]) # 10 , 20 , 30 , 30
```

## `Series` - same index number in a single value

1. **value 1** hai or oisa **index number 3** hai. 

```py
import pandas as pd

s = pd.Series(5, index=['a', 'b', 'c'])

print(s)

print(s['c'])
```

## `Series` - Series ki full information

```py
import pandas as pd

s = pd.Series(
    [10, 20, 30],
    index=['a', 'b', 'c']
)

print(s.values) # [10 20 30]

print(s.index)  # Index(['a', 'b', 'c'], dtype='str')

print(s.dtype)  # int64

print(s.name)   # None

print(s.size)   # 3
```

## `Series` - Series ko List Datatype mein convert karna
```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

d = s.tolist() # Series into List

print(type(d))

print(d)

# ---

import pandas as pd

data = [10, 20, 30]

s = pd.Series(data)

d = s.tolist() # Series into List

print(type(d))

print(d)
```

## `Series` - Series ko Dictionary Datatype mein convert karna
```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

d = s.to_dict()

print(d) # {'a': 10, 'b': 20, 'c': 30}
```

## `Series` - Series mein Dictionary create karna direct

```py
import pandas as pd

s = pd.Series(
    {
        'Ali': 25, 
        'Sara': 30, 
        'John': 35
    }
)

print(s)

print(s['Ali'])
```

## `Series` - **name()** parameter

```py
import pandas as pd

marks = pd.Series(
    [85, 90, 78, 92, 88],
    index=['Ali', 'Sara', 'John', 'Ayesha', 'Bilal'],
    name='Marks'
)

print(marks)
```

## `Series` - Checking if any Value Null so return TRUE if Not Null so return FALSE
```py
import pandas as pd

data = [10, 20, 30 , 30 , 45, 100, 78, 400]

s = pd.Series(data)

print(s.isnull()) # FALSE

# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6    False
# 7    False

# dtype: bool

# ---

import pandas as pd

data = [10, 20, 30 , None , 45, 100, 78, 400]

s = pd.Series(data)

print(s.isnull()) # FALSE

# 0    False
# 1    False
# 2    False
# 3    True
# 4    False
# 5    False
# 6    False
# 7    False

# dtype: bool
```

## `Series` - Missing Values ko drop/delete karna

1. **None** likhne se Pandas isko khud hi missing value (NaN) samajh leta hai

2. **dropna()** missing values ko list se remove karta hai.

```py
import pandas as pd

data = [10, 20, None, 40, None, 50]

s = pd.Series(data)

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

1. jo bhe duplicate values honge wo sari remove hojaynge.

```py
import pandas as pd

data = [10, 20, 20, 30, 10, 40]

s = pd.Series(data)

unique_s = s.drop_duplicates()

print(unique_s)
```

## `Series` - Kisi specific index ka data remove/delete karna ho

1. **drop()** ke zariye kisi bhi label/index ka data delete kar sakte hain

```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

s = s.drop("b")

print(s)

# ---

import pandas as pd

data = [10, 20, 30]

s = pd.Series(data)

s = s.drop(1)

print(s)
```

## `Series` - Ek se zyada indexes ko ek sath delete karna

1. List ki surat mein multiple indexes pass karke delete karna

```py
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

s = s.drop(["a", "c"])

print(s)

# ---

import pandas as pd

data = [10, 20, 30, 40]

s = pd.Series(data)

s = s.drop([0 , 2])

print(s)

```

## `Series` - Single value ko update karna

```py
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

s["b"] = 99
print(s)

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