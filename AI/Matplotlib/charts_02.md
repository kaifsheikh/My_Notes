## Matplotlib charts:

# 1. Line Chart

> 1. ### Time ke saath data ka (up/down) dikhana.

> 2. ### Stock price, temperature, sales trend.

```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.plot(x, y) # Line Chart

plt.title("Line Graph")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.show()
```

---

# 2. Bar Chart (Comparison ke liye)

1. > ### Bar Chart ek aisa graph hai jo different categories ke values ko compare karne ke liye use hota hai..

2. > ### Fruits ki price, students ke number.

# Vertical or Horizontal bar Charts

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Smith", "Bilal"]
marks = [70, 85, 90, 65]

# Vertical Bar Chart
plt.bar(students, marks)

# Horizontal Bar Chart
plt.barh(students, marks) 

# Headings
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

# Coloring in Bar Chart

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Smith", "Bilal"]
marks = [70, 85, 90, 65]

# Single Color
plt.bar(students, marks, color="red")

# Headings
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

```py
import matplotlib.pyplot as plt

students = ["Ali", "Ahmed", "Smith", "Bilal"]
marks = [70, 85, 90, 65]

# Multiple Colors
colors = [
    "red",
    "blue",
    "green",
    "orange"
]

# bar Chart with Multi Colors
plt.bar(students, marks, color=colors)

# Headings
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Smith", "Bilal"]
marks = [70, 85, 90, 65]

# Custom Design
plt.bar(students, marks, width=0.1, edgecolor='red', linewidth=3, alpha=0.1)

# Headings
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

# Show Bar Info According to the Real Values

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Smith", "Bilal"]
marks = [70, 85, 90, 65]

# Bar Chart
bars = plt.bar(students, marks)

# Show all Values
for bar in bars:
    print(bar)              # Show All Bar values
    print(bar.get_height()) # Show Bar Values

# Headings
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Kaif"]
marks = [70, 85, 90]

# Bar Chart
bars = plt.bar(students, marks)

# Show Bar Values in Graph
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2, 
        bar.get_height(),
        str(bar.get_height()),
        ha="center"
    )

plt.show()
```

# Bar Chart with Figure

- ### 8 = width
- ### 5 = height

```py
import matplotlib.pyplot as plt

# Data
students = ["Ali", "Ahmed", "Kaif", "Bilal"]
marks = [70, 85, 90, 65]

# Canvas size set
plt.figure(figsize=(8,5))

# Bar chart
plt.bar(students, marks, color="skyblue")

# Labels
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

---

# 3. Pie Chart
> 1. ### Kisi mukammal cheez mein alag hisson ka percentage batana.

> 1. ### Budget ka kharcha, votes ka distribution.

```py
import matplotlib.pyplot as plt

# Data
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
usage = [40, 25, 18, 12, 5]

plt.pie(usage, labels=languages)
plt.title("Programming Languages Usage")
plt.show()
```

> 1. ### `autopct=''` iska use number ko percentage or percentage ko decimal mein karne ka liya hota hai

> 2. ### `autopct='%.0f%%'` - yeah sirf percentage mein karayga decimal mein nhe.

```py
import matplotlib.pyplot as plt

# Data
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
usage = [40, 25, 18, 12, 5]

# autopct number ko decimal mein or percentage mein convert karayga
plt.pie(usage, labels=languages, autopct='%1.1f%%')
plt.title("Programming Languages Usage")
plt.show()
```

```py
import matplotlib.pyplot as plt

# Data
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
usage = [40, 25, 18, 12, 5]

plt.pie(usage)
plt.legend(['Python', 'Java', 'C++'], title="Languages")
plt.show()
```

```py
import matplotlib.pyplot as plt

# Data
data = [40, 30, 20, 10]
categories = ['Python', 'Java', 'C++', 'Ruby']

plt.pie(data, autopct='%1.1f%%')

plt.legend(categories, title="Language", loc="lower right")

plt.title("Programming Languages")
plt.show()
```

---

### 4. Histogram (Frequency dikhane ke liye)
- **Kaam:** Data ka spread aur frequency batana (kitna baar koi value aayi).
- **Use:** Students ke number ka distribution, age groups.

```py
import matplotlib.pyplot as plt
import numpy as np
marks = np.random.randint(30, 100, 200)

plt.hist(marks, bins=10, color='skyblue', edgecolor='black')
plt.title("Students Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()
```

### 5. Scatter Plot (Relationship dekhne ke liye)
- **Kaam:** Do variables ke beech correlation (positive/negative) dikhana.
- **Use:** Padhai ka time vs exam number.

### 6. Box Plot (Outliers aur spread ke liye)
- **Kaam:** Median, range aur abnormal values (outliers) dikhana.
- **Use:** Salaries ka distribution.

### 7. Area Chart (Stacked comparison ke liye)
- **Kaam:** Total value mein har part ka contribution dikhana.
- **Use:** Website visitors ke sources (search, social, direct).

```py
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan','Feb','Mar','Apr','May']
sales = [200, 250, 270, 300, 350]

plt.fill_between(range(len(months)), sales, color='skyblue', alpha=0.4)
plt.plot(range(len(months)), sales, color='Slateblue', alpha=0.6, linewidth=2)
plt.xticks(range(len(months)), months)
plt.title("Monthly Sales (Area Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

### 8. Heatmap (Matrix data ke liye)
- **Kaam:** Colors se values ki intensity dikhana.
- **Use:** Correlation matrix, temperature map.

## Chart choose karne ka quick rule:

| Aapko kya dikhana hai? | Best chart |
|------------------------|------------|
| Trend over time | Line Chart |
| Comparison | Bar Chart |
| Percentage / share | Pie Chart |
| Distribution | Histogram / Box Plot |
| Relationship | Scatter Plot |
| Contribution in total | Stacked Bar / Area |