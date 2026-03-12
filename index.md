Main tumhare text ko **same concept ke saath**, lekin **zyada clear order, thodi extra detail aur easy wording** ke saath clean kar raha hoon. Tum ise notes ki tarah bhi use kar sakte ho.

---

# Python Program Run Hone Ka Complete Process (Easy Explanation)

Example program:

```python
print("Hello")
```

Tum terminal ya VS Code mein run karte ho:

```bash
python app.py
```

Ab dekho **computer ke andar kya kya hota hai**.

---

# Step 1 — Python Interpreter Start Hota Hai

Jab tum command run karte ho:

```
python app.py
```

to **Python interpreter start hota hai**.

Interpreter ka kaam hota hai:

* Python code ko read karna
* usko samajhna
* aur execute karna

Simple idea:

```
User command
↓
Python Interpreter start
```

---

# Step 2 — Python File Open Aur Read Hoti Hai

Python interpreter tumhari file open karta hai.

Example:

```
app.py
```

Uske andar jo code likha hai Python **line by line read karta hai**.

Example:

```python
print("Hello")
```

Ab Python ko pata hai ke program mein kya likha hai.

---

# Step 3 — Syntax Check (Code Sahi Hai Ya Nahi)

Ab Python check karta hai:

* code correct hai ya nahi
* koi syntax error to nahi

Example mistake:

```python
print("Hello
```

Yahan bracket close nahi hai.

Python turant error dega:

```
SyntaxError
```

Agar code sahi hai to Python next step par jata hai.

---

# Step 4 — Code Ko Chote Pieces Mein Todna (Tokens)

Ab Python code ko **chote chote pieces mein tod deta hai**.

In pieces ko bolte hain:

```
Tokens
```

Example code:

```python
x = 5 + 3
```

Python internally isko tod deta hai:

```
x
=
5
+
3
```

Yeh sab alag alag **tokens** hain.

Is process ko bolte hain:

```
Tokenization
```

---

# Step 5 — Code Ka Structure Samajhna (AST)

Ab Python check karta hai:

* code ka structure kya hai
* kaunsi cheez assignment hai
* kaunsi calculation hai
* kaunsa loop hai
* kaunsa if statement hai

Is structure ko bolte hain:

```
AST (Abstract Syntax Tree)
```

Example:

```python
x = 5 + 3
```

Python internally samajhta hai:

```
Assignment
   |
   x
   |
Addition
 /   \
5     3
```

Yeh Python ko batata hai ke **program ka logic kya hai**.

---

# Step 6 — Bytecode Banana

Ab Python tumhare code ko **apni internal language mein convert karta hai**.

Is language ko bolte hain:

```
Bytecode
```

Example:

Tum likhte ho:

```python
print("Hello")
```

Python internally kuch aisa banata hai (concept):

```
LOAD "Hello"
CALL PRINT
```

Important baat:

* yeh **machine language nahi hoti**
* yeh **Python ki internal language hoti hai**

Kabhi kabhi yeh file mein store bhi hoti hai:

```
__pycache__
```

---

# Step 7 — Python Virtual Machine (PVM) Code Run Karti Hai

Python ke andar ek engine hota hai jise bolte hain:

```
Python Virtual Machine (PVM)
```

Ye engine **bytecode ko execute karta hai**.

Flow:

```
Python Code
↓
Bytecode
↓
Python Virtual Machine
↓
Execution
```

Yeh step actual **program run hone ka stage** hota hai.

---

# Step 8 — Variables Memory Mein Store Hote Hain

Agar program mein variables hain:

```python
x = 5
y = 10
```

to Python:

1. value ka object banata hai
2. usko **RAM (heap memory)** mein store karta hai
3. variable us object ko reference karta hai

Concept:

```
x → 5
y → 10
```

Matlab:

* `5` aur `10` memory mein objects hain
* `x` aur `y` un objects ke references hain

---

# Step 9 — Calculations Aur Operations Hoti Hain

Ab Python program mein jo operations likhe hain wo perform karta hai.

Example:

```python
print(x + y)
```

Python karta hai:

```
5 + 10 = 15
```

---

# Step 10 — Output Screen Par Aata Hai

Ab Python result ko **output stream** mein bhejta hai.

Terminal par output show hota hai.

Output:

```
15
```

---

# Step 11 — Program Finish Ho Jata Hai

Jab code finish ho jata hai:

Python:

* program stop karta hai
* unused memory free karta hai
* process close ho jata hai

---

# Complete Flow (Simple Diagram)

Python program run hone ka complete flow:

```
1 Python interpreter start hota hai
2 Python file open hoti hai
3 Syntax check hota hai
4 Code tokens mein tod diya jata hai
5 AST (structure) banaya jata hai
6 Bytecode generate hota hai
7 Python Virtual Machine bytecode run karti hai
8 Variables memory mein store hote hain
9 Calculations aur operations perform hoti hain
10 Output screen par aata hai
11 Program finish ho jata hai
```

---

# Short Simple Definition

Jab Python program run hota hai:

```
Python code read karta hai
↓
code check karta hai
↓
tokens banata hai
↓
structure (AST) samajhta hai
↓
bytecode banata hai
↓
Python Virtual Machine run karti hai
↓
memory use hoti hai
↓
output milta hai
```

---
