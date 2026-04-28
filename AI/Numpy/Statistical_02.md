# What is Statistic:
1. Statistic ka matlab hai ka Numbers ko analysics karke oiska kch matlab find karna jaise ka:
2. Class ka Students ka Marks Count karna Average, Max, and Min jaise or bhe kam karna wo sub Statistic mein ata hai

# Min()
1. Array mein sabse chhoti value return karta hai.

```py
import numpy as np

arr = np.array([5, 2, 9, 1, 7])
print(np.min(arr))   # Output: 1
```

# Max()
1. Array mein sabse badi value return karta hai.

```py
import numpy as np

arr = np.array([5, 2, 9, 1, 7])
print(np.max(arr))   # Output: 9
```

# median() - Median value
1. yeah Numbers ko chote se bade mein Arrange / Sort karta hai oiska bad center ki value (middle value) find karke return karta hai.

```py
import numpy as np

arr = np.array([1, 2, 3, 100, 200])
print(np.median(arr))   # Output: 3.0 (Middle Value)
```

# mean() - Average
1. yeah sari values ka sum karta hai or Number of Values se Divide kar deta hai.

```py
import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.mean(arr))   # Output: 2.5
```

# std() - Standard Deviation
1. 

```py
import numpy as np

arr = np.array([10, 12, 11, 13, 14])
print(np.std(arr))   # Output: ~1.41
```

