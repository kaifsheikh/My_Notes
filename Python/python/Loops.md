# What is Loop?

1. Programming language mein **loop** ka matlab hota jo kisi specific code ko (block of code) ko baar baar execute (run) karta hai jab tak aik khaas condition **true** rehti hai.

2. Loop ka basic rule hi yeh hai ke jab tak condition **True** rahegi, loop chalta rahega. Jaise hi woh condition **False** hogi, loop forn ruk jayega. Agar hum condition ko False nahi karenge, toh computer ko pata hi nahi chalega ke kab rukna hai, aur woh chalta hi chala jayega (jise infinite loop kehte hain).

3. **purpose**: loop ka purpose Code **ko baar-baar repeat karna without writing same code again and again**.

    - **Initialization**: Kaam kahan se shuru karna hai (e.g., ginti 1 se shuru karni hai).

    - **Condition**: Kaam kab tak chalana hai (e.g., jab tak ginti 10 tak na pahunch jaye).

    - **Increment/Decrement**: Har chakkar ke baad agay kaise barhna hai (e.g., 1 ke baad 2, phir 3 karna).

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