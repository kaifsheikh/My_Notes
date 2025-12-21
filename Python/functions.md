# What is Function?

# Local Variables in Function:
1. Jo variable function ke andar create hai usay `local variable` kehte hain.
2. **Local** means sirf us function tak limited
2. `x` or `y` yeah Local Variables hai inha Function ka bahir access nahi kar sakta hai.

```py
def add():
    x = 10        # local variable
    y = 20        # local variable
    print(x + y) 

add()
```

### `Local variable` function ke bahar access nahi hota.

```py
def add():
    x = 10        # local variable
    print(x) 

add() # 10

print(x) # NameError: name 'x' is not defined
```
### `Local variable` ko return karna.
1. is terha `Local Variable` ko bahir Access kar sekhte hai
```py
def add():
    x = 5
    y = 3
    return x + y

result = add()
print(result)
```

# Global Variables in Function:
1. Jo variable function ke bahar banaya jaye, wo `global variable` hota hai.
2. `num` yeah Global Variable hai isa Funtion ka andar Access kar sekhte hai lakin sirf Read kar sekhte hai.

```py
num = 50   # global variable

def show():
    print(num) 

show() # 50
```

### Global variable ko function ke andar Modify karna ho tu:
1. Agar hume `global variable` ko `modify` karna ho, function ka inside tu `global` keywoard use karna hota hai Function ka Inside.

```py
count = 5   # global variable

def increase():
    global count
    count = count + 1

increase()

print(count) # 6
```
# Same naam ka variable (local vs global):
1. Local variable global ko override nahi karta, sirf function ke andar use hota hai.

```py
x = 100       # global

def demo():
    x = 50    # local
    print(x)

demo()   # 50
print(x) # 100
```

# Function with Parameter:
1. Parameter wo variable hota hai jo function banate waqt brackets ke andar likhte hain.
2. **Purpose** Jab function ko call karega, to value `Parameter` ka pass ayge.

```py
def greet(name):
    print("Hello", name)

greet("Ali") # Ali
```
1. `Ali` -> Value ko `Argument` bhe bolte hai.
2. Function call karte waqt hum Argument pass karte hai jo Parameter ka pass jata hai. 

```py
def make_juice(fruit):
    print(fruit, "juice ready")

make_juice("Apple") # Apple juice ready
make_juice("Mango") # Mango juice ready
```

### Default Parameter:
1. Agar argument na mile to default use hota hai.

```py
def greet(name="Guest"):
    print("Hello", name)

greet()        # Hello Guest
greet("Kaif")  # Hello Kaif
```
# Return Statement:
