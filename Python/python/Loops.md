# What is Loop?
1. Loops ka purpose: Code ko baar-baar repeat karna without writing same code again and again.

## Types of Loops in Python:

1. For loop
2. While loop

## Example:
```py
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) # appple banana cherry

# ----

for i in range(5):
    print(i) # 0 1 2 3 4

# ----

word = "Python"
for char in word:
    print(char) # P t t h o n

```

```py
matrix = [1,2,3,4,5,6,7,8,9,10] #
even_numbers = []

for num in matrix:
    if num % 2 == 0:
        even_numbers.append(num)
    
print(even_numbers) # [2, 4, 6, 8, 10]

# ----

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] # Nested List

for row in matrix:
    for col in row:
        print(col , end=" ") # end=" " -> means print ke baad new line ki jagah space add karo
    print()

#  1 2 3
#  4 5 6
#  7 8 9
```