
| No.  | Data Structure | Example | Easy Meaning |
|------|----------------|----------|---------------|
| 7️⃣ | **Vector** | `c(10, 20, 30)` | Ye same **type** ke multiple values ko ek hi variable me store karta hai. |
| 8️⃣ | **List** | `list(10, "R", TRUE)` | Ek **mixed collection** — numbers, text, logical values sab ek sath store kar sakta hai. |
| 9️⃣ | **Matrix** | `matrix(1:6, nrow=2, ncol=3)` | Rows aur columns me arranged values — bilkul **table jaisa structure**. Sab values same type ke hone chahiye. |
| 🔟 | **Array** | `array(1:8, dim=c(2,2,2))` | Matrix ka advanced version — multiple (2D, 3D ya zyada) dimensions me data store kar sakta hai. |
| 11️⃣ | **Data Frame** | `data.frame(name=c("Ali","Sara"), age=c(21,22))` | Table jaisa structure jisme **har column alag data type** ka ho sakta hai (jaise name = text, age = number). |
| 12️⃣ | **Factor** | `factor(c("Male","Female","Male"))` | **Categorical data** store karta hai (jaise Gender, City, Grade). Ye labels ko internally numbers me convert karta hai. |
---

## 🔸 Types of Data Structures in R

# `Vector:`
1. Vector me sirf ek type ka data hota hai.
2. c() -> ka matlab hai combine / concatenate
3. R mein Vector ka `Index Number` 1 se start hota hai 0 se nahe.
  
## `Example 01:`
```r
mix <- c(10, "Ali", TRUE) # yeah galat hojayga mixed datatype aik Vector mein store nahe karte hai
name <- c("Ali" , "Ahmed" , "Shayan" , "Bilal")

print(name)    # "Ali" , "Ahmed" , "Shayan" , "Bilal"

print(length(name)) # 4

name[3]        # "Shayan"

name[1:3]      # "Ali" , "Ahmed" , "Shayan"

name[c(1,4)]      # "Ali" , "Bilal"

name[c(TRUE, FALSE, TRUE, FALSE)]  # "Ali" , "Shayan"

is.vector(name) # 
```

## `Example 02:`
1. yeah Name ka `Character` ko count karayga
2. jis naam mein Character 4 se Greater hue oisa yeah print karwa dyga

```r
name <- c("Ali" , "Ahmed" , "Shayan" , "Bilal")

greater <- name[nchar(name) > 4] 

print(greater) # "Ahmed" , "Shayan" , "Bilal"
```

## `sort()` & `rev()`
1. Values ko order mein lana

```r
name <- c("Ali" , "Ahmed" , "Shayan" , "Bilal")

a = sort(name)
name # "Ali" "Ahmed" "Shayan" "Bilal"

b = sort(name , decreasing = TRUE)
b # "Shayan" "Bilal"  "Ali" "Ahmed" 

c = rev(name)
c # "Bilal"  "Shayan" "Ahmed"  "Ali"
```

## `unique()` - Duplicate Values ko Remove Karna

```r
v <- c(1,2,2,3,3,4)
final = unique(v)

final # 1 2 3 4
```

## `rep()` - Values ko Repeat Karne ka liya
1. yeah Vector ki Sari Values ko 3 bar Repeat karayga

```r 
v <- c(1,2,3)
final = rep(v , time = 3)

final # 1,2,3  1,2,3  1,2,3
```

## `which()` - Index Find Karna
1. yeah batata hai kon si value ka Position (Index) Number kaha per hai. 

```r
10   20   30   40   50   
 ↑    ↑    ↑    ↑   ↑
 1    2    3    4   5   <--- Index number

num <- c(10 , 20, 30, 40, 50)

a = which(v > 30)

a # 4 5 --> yeah batayga ka 30 se Greater ki Value Index number 4 or 5 per hai

# ----
 
num <- c(10 , 20, 10, 20, 30)

a = which(v > 10)

a # 2 4 5 --> yeah check karayga 10 se Greater ki Values tu isne 2 4 5 diya
```

## `any()` - Index Find Karna
1. any() check karta hai ka Kya is list mein koi aik value bhi condition ko satisfy karti hai?
2. Ager List mein aik Value bhe mil jaati hai tu yeah `TRUE` return karayga

```r
num <- c(10 , 20 , 30)

a = any(num > 20)

a # TRUE ---> Vector mein ager aik bhe Value sahi hoti hai tu yeh TRUE return karta hai

# ----

num <- c(10 , 20 , 30)

a = any(num > 30)

a # FALSE ---> 30 se koi Value Greater nahe hai isliye FALSE aya
```

## `head()` aur `tail()`

```r
name <- c("Ali" , "Ahmed" , "Shayan" , "Bilal")

final = head(name) # "Ali" , "Ahmed" , "Shayan" , "Bilal"

print(final)
```

# `Data Frame:`
1. Data Frame ek table hoti hai jisme rows aur columns hote hain, bilkul Excel sheet ki tarah.
2. Isme hum her type ka data ko store karte hain — numbers, text, categories sab kuch.

## `Object`
1. Object ek `box` ya `container` jisme hum koi bhi cheez (data, list, result, ya function) store kar sakte hain.
2. aur is box ke andar `number`, `text`, `vector`, `matrix`, `data frame`, `function`... sab kuch aa sakta hai.

## `Example 01 (Data Frame):`
```r
df <- data.frame(
  name = c("Ali" , "Ahmed" , "Karlie" , "Smith" , "Shai1"),
  marks = c(480 , 300 , 259 , 400 , 360),
  age = c(20 , 24 , 29 , 19 , 18)
)

print(df)

1. # `df` - df yeah object hai iske andar hum ek data frame (table) store kar rahe ha.
2. # data.frame() - Ye function hai jo ek table (data frame) banata hai.
2. # `name` , `marks` , `age` - yeh humera columns hai jo object ka andar hai or inha hum Variables bolte hai.
```
# `	Matrix():`
1. Matrix ek aisi table hoti hai jisme sirf `Numbers` store hote hain koi dosre type ka data store nahe hota hai.
2. Matrix mein hum `Text` (jaise "Ali", "Ahmed" etc.) store nahi kar sakte.
3. aur data rows aur columns mein arrange hota hai Excel ki terha.
4. Matrix 2D hota hai means `2 Dimensional` jiska matlab hai Rows and Columns mein data store hota ha.

## `Purpose of Matrix()`
1. Mathematical operations karna like Matrix se hum addition, subtraction, multiplication jaise operations easily kar sakte hain.
2. Matrix ka use linear algebra, machine learning aur statistics mein hota hai.

## `Example 01:`
```r
mat <- matrix(
  c(1,2,3,4,5,6),   # or yeah Data hai
  nrow = 2,         # means 2 Rows create karayga
  ncol = 3          # means 3 Columns create karayga
)

mat
```
## `Example 02 Matrix():`
```r
mat <- matrix(
  c(1,2,3,4,5,6),   # or yeah Data hai
  nrow = 2,         # means 2 Rows create karayga
  ncol = 3,         # means 3 Columns create karayga
  byrow = TRUE      # ek line khatam hone ke baad agli line mein jao
)

mat

# 1. byrow = TRUE - Data ko row ke hisaab se fill karo (ek line khatam hone ke baad agli line mein jao)
# 2. Aur agar byrow = FALSE (ya default hota hai), means:
# 3. Data ko column ke hisaab se fill karo (ek column khatam hone ke baad agla column). 
```