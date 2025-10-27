# Commands in R Language:
1. Comments wo lines hoti hain jo program me likhi jaati hain lekin R unhe execute (run) nahi karta.
2. Ye sirf explanation ya notes likhne ke liye hoti hain.
3. Jo bhi likha ho `#` ke baad, wo comment hota hai.
   
```r
# Arithmatic Operators:
# This is Comment

# isa Dropdown menu ajata hai
### Some other Operators----


```

# Variable in R Language:
1. Variable ek dabba (box) hota hai jisme hum kisi number, text, ya data ko rakhte hain, aur baad me usi value ko use kar sakte hain.
2. Variable ka main kaam hota hai — “value ko store karna.”
3. R me `=` aur `<-` dono value assign karte hain,
3. lekin `<-` R ka original style hai, aur zyada use hota hai.
```r
x = 10
y = 20

# x ek variable hai jisme 10 store hai
# y ek variable hai jisme 20 store hai

x + y # Output : 30
y - x # Output : 10

# Example 02

x <- 10
y <- 20

# Yeah bhe Same hai 10 x mein or 20 y mein store ho reha hai

x + y # Output : 30
y - x # Output : 10
```

## `print()` - Optional
1. print() variable ko print karta hai without print() bhe hum value ko run kar sekhta hai
```r
x <- 10
y <- 20

print(x + y) # Output : 30
```

## `BODMAS:`
1. BODMAS ek math rule hai jo batata hai ke kisi bhi expression (jaise 10 + 5 * 2) ko kis order me solve karna chahiye.
2. Jab koi expression ho, R language (ya math) usko BODMAS order me solve karta hai.
3. Matlab: Pehle `Bracket`, phir `Power`, phir `Divide`, phir `Multiply`, phir `Add`, phir `Subtract`.

```r
x = 100 + 50
y = 95

x + y + (23 - 5) * 10 / 3 # Output : 305
```
# `Datatypes` - R Language
1. R (programming language) mein, data ko store karne ke liye (6) (basic) data types hote hain.
# `Type of Datatypes:`
1. Logical
2. Numeric
3. Integer
4. Character
5. Complex
6. Raw

# Definition
**Data Type** batata hai ke kisi variable mein kis type ka data store hua hai —  
number, text, TRUE/FALSE, ya kuch aur.  
R language ko yeh jaanna zaroori hota hai taake wo data ko sahi tarike se process kar sake.

---

## `Basic Data Types (Single value types)`

| No. | Data Type | Example | Easy Meaning |
|-----|------------|----------|---------------|
| 1️⃣ | **Numeric** | `x <- 12.5` | Numbers (decimal ya simple number) |
| 2️⃣ | **Integer** | `y <- 10L` | Sirf poora number (L lagana zaroori hai) |
| 3️⃣ | **Character** | `name <- "R Studio"` | Text ya string data (quotes ke andar likha hota hai) |
| 4️⃣ | **Logical** | `a <- TRUE` or `b <- FALSE` | TRUE/FALSE (Yes/No type values) |
| 5️⃣ | **Complex** | `z <- 3 + 2i` | Real + imaginary number (maths ke complex numbers) |
| 6️⃣ | **Raw** | `charToRaw("R")` | Data ko binary (machine) form me store karta hai |

---

## `Example 01:`
```r
# 1. Numeric
x <- 12.5
print(x)       # Output: 12.5

# 2. Integer
y <- 10L
print(y)       # Output: 10

# 3. Character
name <- "Aptech"
print(name)    # Output: "Aptech"

# 4. Logical
is_passed <- TRUE
print(is_passed)  # Output: TRUE

# 5. Complex
z <- 3 + 2i
print(z)        # Output: 3+2i

# 6. Raw
r <- charToRaw("A")
print(r)        # Output: 41
```

# `Advanced Data Structures (Multiple values / group types)`
## `Definition`
R language me sirf single values (numbers, text, TRUE/FALSE) hi nahi balki **multiple values** ya **complex data** ko store karne ke liye kuch **data structures** bhi hote hain.  
Ye structures data ko **organize aur manage** karne me help karte hain — jaise list, table, matrix, etc.

---

## 🔸 Types of Data Structures in R

# `Data Frame:`
1. Data Frame ek table hoti hai jisme rows aur columns hote hain, bilkul Excel sheet ki tarah.
2. Isme hum data ko store karte hain — numbers, text, categories sab kuch.

## `Object`
1. Object ek `box` ya `container` jisme hum koi bhi cheez (data, list, result, ya function) store kar sakte hain.
2. aur is box ke andar `number`, `text`, `vector`, `matrix`, `data frame`, `function`... sab kuch aa sakta hai.

## `Example 01 (Data Frane):`
```r
df <- data.frame(
  name = c("Ali" , "Ahmed" , "Karlie" , "Smith" , "Shai1"),
  marks = c(480 , 300 , 259 , 400 , 360),
  age = c(20 , 24 , 29 , 19 , 18)
)

1. # `df` - df yeah object hai iske andar hum ek data frame (table) store kar rahe ha.
2. # data.frame() - Ye function hai jo ek table (data frame) banata hai.
2. # `name` , `marks` , `age` - yeh humera columns hai jo object ka andar hai or inha hum Variables bolte hai.
```

| No.  | Data Structure | Example | Easy Meaning |
|------|----------------|----------|---------------|
| 7️⃣ | **Vector** | `c(10, 20, 30)` | Ye same **type** ke multiple values ko ek hi variable me store karta hai. |
| 8️⃣ | **List** | `list(10, "R", TRUE)` | Ek **mixed collection** — numbers, text, logical values sab ek sath store kar sakta hai. |
| 9️⃣ | **Matrix** | `matrix(1:6, nrow=2, ncol=3)` | Rows aur columns me arranged values — bilkul **table jaisa structure**. Sab values same type ke hone chahiye. |
| 🔟 | **Array** | `array(1:8, dim=c(2,2,2))` | Matrix ka advanced version — multiple (2D, 3D ya zyada) dimensions me data store kar sakta hai. |
| 11️⃣ | **Data Frame** | `data.frame(name=c("Ali","Sara"), age=c(21,22))` | Table jaisa structure jisme **har column alag data type** ka ho sakta hai (jaise name = text, age = number). |
| 12️⃣ | **Factor** | `factor(c("Male","Female","Male"))` | **Categorical data** store karta hai (jaise Gender, City, Grade). Ye labels ko internally numbers me convert karta hai. |

---

## `Example 02:`
```r

```

https://youtu.be/73vO2EAZKdE?si=nm4YjPDXXs00974N&t=2240
E-Book : https://codanics.com/books/abc-of-statistics-for-data-science/