# Examples of Custom Functions:

```py
name = "kaif shaikh"

name.upper()                 # KAIF SHAIKH
name.lower()                 # kaif shaikh
name.title()                 # Kaif Shaikh
name.capitalize()            # Kaif shaikh
name.strip()                 # Extra spaces remove
name.replace("kaif", "Ali")  # Ali shaikh
name.split()                 # ['kaif', 'shaikh']
name.find("shaikh")          # 5

# ---------------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.append("Orange")     # Item add
fruits.insert(1, "Grapes")  # Position par add
fruits.remove("Apple")      # Item delete
fruits.pop()                # Last item remove
fruits.sort()               # Alphabetical sort
fruits.reverse()            # Reverse list
fruits.count("Mango")       # Item count
fruits.index("Mango")       # Item position

# ---------------------------------------------------------

student = {"name": "Kaif", "age": 20}

student.keys()                # dict_keys(['name', 'age'])
student.values()              # dict_values(['Kaif', 20])
student.items()               # Key aur value dono
student.get("name")           # Kaif
student.update({"age": 21})   # Value update
student.pop("age")            # Key delete
student.copy()                # Dictionary copy
student.clear()               # Dictionary empty

```

# Example 2:

```py
name = "kaif shaikh"

# Case checking
name.isupper()             # False
name.islower()             # True
name.istitle()             # False
name.isspace()             # False
name.isalpha()             # False (space ki wajah se)
name.isalnum()             # False

# Searching
name.startswith("kaif")   # True
name.endswith("shaikh")   # True
name.count("a")           # 2
name.rfind("a")           # Last occurrence index
```

# Example 3:

```py
numbers = [10, 20, 30, 40, 50]

# Adding
numbers.extend([60, 70, 80])

# Copying
new_numbers = numbers.copy()

# Sorting
numbers.sort(reverse=True)
numbers.sort(key=None)

# Removing
numbers.pop()   # Last item removed
numbers.clear() # All items removed

# Searching
numbers.index(30)
numbers.count(20)
```

# Example 4:

```py
numbers = [10, 20, 30, 40, 50]

len(numbers)       # Total items
max(numbers)       # Largest value
min(numbers)       # Smallest value
sum(numbers)       # Total sum
sorted(numbers)    # New sorted list
reversed(numbers)  # Reverse iterator
any(numbers)       # Kya koi value True hai?
all(numbers)       # Kya sab values True hain?
```

# Example 5:

```py
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:4]       # [20, 30, 40]
numbers[:3]        # [10, 20, 30]
numbers[2:]        # [30, 40, 50, 60]
numbers[-1]        # 60
numbers[-3:]       # [40, 50, 60]
numbers[::-1]      # Reverse list
numbers[::2]       # Every second item
```
