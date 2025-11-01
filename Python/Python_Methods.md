# Python Methods:

```py
name = "python"
print(name.upper()) # PYTHON

# -------------------

word = "HELLO"
print(word.lower()) # hello

# -------------------

msg = "hello world"
print(msg.title()) # har word ka first letter capital

# -------------------

text = "   Hello Python   "
print(text.strip()) # extra spaces hata deta hai

# -------------------

sentence = "I love Java"
print(sentence.replace("Java", "Python")) # words replace karta hai

# -------------------

data = "apple,banana,mango"
print(data.split(",")) # text ko todta hai list mein

# Output : ['apple', 'banana', 'mango']

# -------------------

Name = "Harry"   =>  Length = 5

Indexes:
Forward Index  →   0   1   2   3   4
Characters     →   H   a   r   r   y
Backward Index →  -5  -4  -3  -2  -1

print(Name) # Harry
print(Name[0]) # H
print(Name[-1]) # y
print(len(Name)) # 5
print(Name[0:3]) # Har
print(Name[0:5]) # Harry
print(Name[-4 : -1]) # arr

# -------------------

numbers = [3,4,5,6,7,8,1]
numbers.sort()
print(numbers) # [1, 3, 4, 5, 6, 7, 8]

# -------------------

numbers = [3,4,5,6,7,8,1]
numbers.reverse()
print(numbers) # [1, 8, 7, 6, 5, 4, 3]
```

# `Object Methods:`
```py
# -------------------

student = {
    "name": "Ali",
    "age": 20
}
print(student.keys()) # dict_keys(['name', 'age'])

# -------------------

student = {
    "name": "Ali",
    "age": 20
}
print(student.values()) # dict_values(['Ali', 20])

# -------------------

student = {
    "name": "Ali",
    "age": 20
}
print(student.items()) # dict_items([('name', 'Ali'), ('age', 20)])

# -------------------

student = {
    "name": "Ali",
    "age": 20
}
print(student.get("name")) # Ali
```


https://youtu.be/UrsmFxEIp5k?si=ozZ6gIK6mhjt1wvX&t=5695