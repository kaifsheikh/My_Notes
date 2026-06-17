# What is Numpy:
1. Numpy Means (Numerical Python) yeah aik Python ki Library hai.
2. Numpy ka main use Numbers aur Calculations jaise kamo mein kiya jata hai.
3. Numpy Maths, Statistics, Arrays or Numbers jaise kamo ko ache se Manage karta hai. 

---

# What is Array:
1. Array ek container hai jisme hum Multiple Data Store karte hai
2. Array mein hum same type ka Data store karte hai.
3. Array mein hum Mixed Datatype store nhe kar sekhte hai
4. Array mein Data aik Order mein store hota jisa hum Index Number bolte hai jo 0 se start hota hai.
5. Index Number ek address hai — jisse hum array mein se koi bhi specific value ko nikal sakte ho.
6. Array mein hum Number, String, Boolean or Float etc her type ka Data store kar sekhte hai.

# Types of Array:
1. 1D Array
2. 2D Array
3. 3D Array

# 1D Array: 
1. 1D Array mein data sirf aik line mein store hota hai — na koi row, na koi column — bas ek seedhi line mein.
2. isko aksar Vector bhe bolte hai 

## Example 01 - 1D Array Mix vs same Datatype:
```py
✅ Sab numbers          →  [10, 20, 30, 40]
✅ Sab words            →  ["Ali", "Sara", "Ahmed"]

❌ Mix nahi ho sakta    →  [10, "Ali", 30]  ← Yeh list hai, array nahi!
```

## Example 02 - 1D Array with Positive Index Number:
```py
[10,  20,  30,  40,  50]
  ↑    ↑    ↑    ↑    ↑
  0    1    2    3    4   ← Yeh INDEX numbers hain jo 0 se start hota hai
```

## Example 03 - 1D Array with Negative Index Number:
```py
[10,  20,  30,  40,  50]
  ↑    ↑    ↑    ↑    ↑
 -5   -4   -3   -2   -1   ← Yeh Negative INDEX numbers hain jo -0 se start hota hai last se
```

# 2D Array:
1. 2D Array mein Rows aur Columns dono hote hain — bilkul Excel sheet ya table ki tarah.
2. 2D Array ko bhe Matrix kehte hain isme Data Table ki form mein show hota hai bilkul Vertical or Horizontal. 

## Example 01 - 2D Array
```py
arr = np.array([
#   C-0   C-1  C-2
    [85,  90,  78],   # Row - 0
    [92,  88,  95],   # Row - 1
    [70,  65,  80]    # Row - 2
])
```
# 3D Array:
1. 

## Example 01 - 3D Array
```py

```

# Array Attributes:
1. Array Attributes woh properties hain jo kisi bhi array ke baare mein Extra information batati hain.
2. jaise uski shape, size, dimension, datatype, etc.
3. yeah koi Functions nhe hote hai yeah Properties hoti hai.

## Example 01 - Array Attributes

---

# Array Operations:
1. Array operations wo actions hain jo NumPy arrays ke data par mathematical ya logical processing karte hain.

## Example 01 - Array Operations

```py
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Arithmetic Operators:

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a ** b) # Exponent

---

```

## Example 02 - Aggregation Operations

1. Aggregation operations woh mathematical functions hain jo array ke multiple values ko combine karke ek summary statistic produce karte hain, jaise sum, average, min, max, etc.

```py
import numpy as np
a = np.array([10, 20, 30, 40])

print(a.sum())  # Addition -> 100
print(a.mean()) # Average ->  25.0
print(a.min())  # Minimum ->  10
print(a.max())  # Maximum ->  40
print(a.std())  # Standard Deviation (STD) -> 
print(a.var())  # Variance ->  
print(a.prod()) # Product -> 
```

## Example 02 - Aggregation with Axis

1. Aggregation with Axis

```py
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.sum(axis=0)) # Column-wise sum -> [5 7 9]
print(a.sum(axis=1)) # Row-wise sum -> [6 15]

| Axis   | Direction |
| ------ | --------- |
| axis=0 | columns   |
| axis=1 | rows      |
```