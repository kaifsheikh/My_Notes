
## `Array` (Linear Data Structure)
> 1. ### **Array**: mein hum Same type ka Data store karta hai isme Multi type ka data aik Array mein store nhe kar sekhte hai.

> 2. ### aik Array numbers ke liye bana hai, to usmein sirf numbers hoge yeah agar text ke liye bana hai, to oisme sirf text hoga.

> 3. ### Array ka size fixed hota hai means, array bante time usmein kitne values rekhne hai , woh pehle se decide karni padti hai bad mein oisme add nahe kar sekhte hai lakin old values ko update kar sekhte ha.

> 4. ### Array ki values ko hum Index Number se access kar sekhte hai or index number 0 se start hota hai.

> 5. ### List ke mutabiq array **zyada fast** hai kyunki values memory mein ek saath hain.

> 6. ### Pandas ka pure kaam arrays par hi based hai (DataFrame andar se array hai).

## `Array Examples` - (Linear Data Structure)

1. array mein se **None** value remove ki oisa list bnaya or print kardiya.

```py
import pandas as pd

arr = [10, 20, None, 40, None, 60]

clean_arr = pd.array(arr).dropna().tolist()

print(clean_arr)
```

---

1. array ko oiske index number se print karwaya.
```py
import pandas as pd

arr = [10, 20, 40, 60]

a = pd.array(arr)[0]

print(a) 
```

---

1. full array ko print karwana.
```py
import pandas as pd

country = ["Pak", "India", "USA", "UK"]
final_data = pd.array(country)

print(final_data)
```

---

1. list ko array mein convert karna.
```python
import numpy as np

marks_list = [45, 72, 68, 91]

marks = np.array(marks_list)

print(type(marks))  # <class 'numpy.ndarray'>
print(marks)        # [45 72 68 91]
```

---

1. 
```py
import numpy as np

result = np.array(
    [
        [78, 85, 90],
        [62, 71, 88],
        [91, 55, 74]
    ]
)   

print(result)
```

---

1. last mein jo datatype hoga pura result oisi ka according ayga.

```py
import numpy as np

salary = np.array([50000, 55000, 60000])
print(salary.dtype)

salary = np.array([50000, 55000, 60000.50])
print(salary.dtype)

units = np.array([120, 145, 98], dtype=float)
print(units.dtype)           # float64
```

---

1. data structure ka **Dimension check** karne ka liya.
```py
import numpy as np

overs = np.array([12, 8, 15, 22, 9])
print(overs.ndim)   # 1

# ---

innings = np.array(
    [
        [12, 8, 15],
        [22, 9, 18]
    ]
)
print(innings.ndim) # 2
```

---

1. 2 dimension data hai yeah.

```py
import numpy as np

bill = np.array(
    [
        [120, 95, 60, 30],
        [140, 110, 75, 28],
        [105, 88, 52, 35]
    ]
)

print(bill.shape) # 3 rows , 4 columns

print(bill[0].shape) # [120, 95, 60, 30]
```

---

# Array with Conditions: 

1. array mein conditions apply karna ho.

```py
import numpy as np

sales = np.array([2500, 3200, 1800, 4100, 2900])

print(sales[sales > 3000])
```

---

```python
import numpy as np

marks = np.array([45, 78, 92, 61, 35, 88])

print(marks[marks >= 60])
```

---

```python
numbers = np.array([50, 100, 75, 100, 25])

print(numbers[numbers == 100])
```

---

```python
numbers = np.array([50, 100, 75, 100, 25])

print(numbers[numbers != 100])
```

---

```python
marks = np.array([35, 50, 65, 80, 90, 45])

print(marks[(marks >= 50) & (marks <= 80)])
```
---

```python
marks = np.array([35, 50, 65, 80, 90, 45])

print(marks[(marks < 50) | (marks > 80)])
```
---

```python
numbers = np.array([10, 15, 22, 31, 40, 55])

print(numbers[numbers % 2 == 0])
```

---

```python
price = np.array([100, 250, 500, 750, 1000, 1500])

print(price[(price >= 500) & (price <= 1000)])
```

---

```python
import numpy as np

rates = np.array([[185, 140, 290]])

print(rates[0, 0])   # 185 
print(rates[0, 2])   # 290 
```

---

```python
import numpy as np

prices = np.array([4200, 4250, 4180, 4300, 4290, 4350, 4400])

print(prices[:3])     # [4200 4250 4180]  → pehle 3 din
print(prices[2:5])    # [4180 4300 4290]  → 3rd se 5th din
print(prices[::2])    # [4200 4180 4290 4400] → har 2nd din
```

---

```python
import numpy as np

prices = np.array([1500, 850, 2200, 300])

discounted = prices * 0.90

with_gst = discounted * 1.15

print(with_gst)
```

---