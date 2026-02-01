# What is Datatypes in Python?

## 1. `String (str) — Text store karne ke liye`
1. String wo data type hai jisme `text` ya `characters` hote hain.
2. Ye quotes `" "` ya `' '` ke andar likha jaata hai.

## `Example 01`
```py
name = "Ali"
city = 'Lahore'

print(name) # Ali
print(city) # Lahore
```
## 2. `Integer (int) — Whole Numbers (poore number)`
1. Integer wo numbers hote hain jinke andar `decimal (.)` nahi hota.
2. Numbers Datatype Without quotation `" "` ya `' '` mein store nahe hota hai.

## `Example 01`
```py
age = 20
students = 45

print(age)      # 20
print(students) # 45
```
## 3. `Float (float) — Decimal Numbers`
1. Float me decimal point wale numbers hote hain.

## `Example 01`
```py
pi = 3.14
price = 19.99

print(pi)      # 3.14
print(price)   # 19.99
```
## 4. `Boolean (bool) — True or False`
1. Boolean me sirf do values hoti hain:

- `True`
- `False`

## `Example 01`
```py
age = 18
print(age >= 18) # True

age = 18
print(age >= 20) # False
```
## 5. `None  — empty value`
1. Jab kisi variable, function, ya expression ke paas koi actual value nahi hoti,
2. tab Python uske liye None use karta hai.
3. None use hota hai jab aap chahte ho ke
4. “abhi ke liye ye khaali rahe, baad mein value dunga.”

## `Example 01`
```py
x = None
print(x)
```
## 4. `List [list] — Multiple Items ek sath`
1. List ek box jesi hoti hai jisme hum multiple values ek sath rakh sakte hain.
2. List ke items index (0 se start) hote hain.
3. List changeable hai means ka iska data change ho sekhta hai
4. or isa `[] brackets` se Represent karte hai.

## `Example 01`
```py
fruits = ["apple", "banana", "mango"]

print(fruits) # ['apple', 'banana', 'mango']
print(fruits[0]) # apple 
```
## 5. `Tuple (tuple) — List jesa but unchangeable`
1. Tuple bhi list jesa hi hota hai,
2. bas farq ye hai ke tuple ke data ko change nahi kar sakte.
3. Tuple Not changeable means ka iska data change nahe ho sekhta hai
4. or isa `() brackets` se Represent karte hai.

## `Example 01`
```py
colors = ("red", "green", "blue")

print(colors) # ('red', 'green', 'blue')
```
## 6. `Dictionary {dict} — Key-Value = Pair`
1. Dictionary ek datatype hai jisme data `key : value ke pair` me store hota hai means.
2. Dictionary mein jis Order se hum Key Value define karte hai, oisi Order mein output ata hai.
3. Dictionary mein har key unique hoti hai.
3. Key sirf string nahi hoti, balke `string`, `number`, `float`, `tuple`, `boolean` or `frozenset` bhe ho sakti hai.
5. Dictionary `MUTABLE` hoti hai kue ka Dictionary ko Create karne ka bad hum oisa Change kar sekhte hai means (Update) jo cheez change ho sekhti hai oisa hum Mutable bolte hai Ager `key` already exist karti hai Dictionary mein tu, oisa change nahi kar sakte hai lakin koi New Key bad mein Add kar sekhte hai means ka Key `immutable` hoti hai lakin `Value` Mutable hoti hai kue ka hum Exist value ko Change kar sekhte hai or bad mein kisi new value ko add bhe kar sekhte hai
3. or isa `['key'] brackets` se Represent karte hai.

```py

```

## 7. `Set (set) — Unique Items ka Group`
1. Set me duplicate values allowed nahi hoti or.
2. Order fix nahi hota (random hota hai).

## `Example 01`
```py
numbers = {1, 2, 3, 3, 2, 1, 10, 8}

print(numbers) # {1, 2, 3, 8, 10}
```