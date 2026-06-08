# Grid

> 1. ### X or Y Axis dono mein Grid Lines aynge

```py
import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6]
sales = [5000, 7000, 6000, 9000, 11000, 8000]

plt.plot(month, sales, marker='o')

# Grid ON for Lines
plt.grid(True)

# Heading
plt.title("Sales Report Dashboard")
plt.xlabel("Month")
plt.ylabel("Monthly Sales")

plt.show()
```

# Grid only X or Y

```py
import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6]
sales = [5000, 7000, 6000, 9000, 11000, 8000]

plt.plot(month, sales, marker='o')

# Grid apply only Y Axis
plt.grid(axis='y')

# Grid apply only X Axis
plt.grid(axis='x')  

# Heading
plt.title("Sales Report Dashboard")
plt.xlabel("Month")
plt.ylabel("Monthly Sales")

plt.show()
```

# Grid Designing

```py
import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6]
sales = [5000, 7000, 6000, 9000, 11000, 8000]

plt.plot(month, sales, marker='o')

# Grid Combine Properties
plt.grid(color='red', linestyle='--', linewidth=5, alpha=0.3)

# Heading
plt.title("Sales Report Dashboard")
plt.xlabel("Month")
plt.ylabel("Monthly Sales")

plt.show()
```

