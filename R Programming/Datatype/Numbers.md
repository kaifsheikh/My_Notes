# Numeric (Real Numbers)
1. eh woh numbers store karta hai jin mein decimal points (yaani fractions) ho sakte hain, jaise $3.14$, $10.5$, ya $-2.0$.
   
```r
x <- 10.12
typeof(x) # "double"
```

# Integer (Whole Number)
1. yeah Pure Whole Number store karta hai jisme Decimal Point nahe hote hai
2. Integer type hone ki nishani ke liye number ke aage L (capital L) lagana zaroori hai.

```r
x <- 10L
typeof(x) # "integer"
```

# 🔢 R Programming: Built-in Numeric Functions

yeah (Numeric/Integer) par kaam karne waale (important) built-in functions hai.

---

## 1. 📐 Mathematical Aur Elementary Functions

| Function | Maqsad (Purpose) | Syntax |
| :--- | :--- | :--- |
| `sqrt()` | **Square Root** nikalna. | `sqrt(x)` |
| `log()` | **Logarithm** nikalna. Base define kar sakte hain. | `log(x, base = e)` |
| `exp()` | **Exponential** value nikalna ($e^x$). | `exp(x)` |
| `round()` | Number ko **qareebi whole number/decimal** tak round karna. | `round(x, digits = 0)` |
| `ceiling()` | Number ko usse **bade** nearest whole number tak round karna. | `ceiling(x)` |
| `floor()` | Number ko usse **chote** nearest whole number tak round karna. | `floor(x)` |
| `trunc()` | Decimal hissa **hata** kar sirf Integer part rakhna. | `trunc(x)` |

## `abs()`
1. Kisi number ki Absolute Value nikalna (negative sign hata deta hai).
   
```r
a = 10
b = 20
c = abs(a - b)

print(c)
# Output: 10
```

## `is.numeric()`
   
```r
a = "100"
b = is.numeric(a)

print(b) # FALSE


a = 100
b = is.numeric(a)

print(b) # TRUE
```

## `as.numeric()`
1. yeah `Character` Datatype ko `Number` mein Convert karta hai.
   
```r
a = "100"
print(typeof(a)) # Character

b = as.numeric(a)
print(typeof(b)) # Double
```

## `sum()`
   
```r
a <- 10
b <- 20
c <- sum(a , b)

print(c) # 30


a <- c(10 , 20 , 30 , 40)
c <- sum(a)

print(c) # 100
```

## `mean()`
1. Avergae karne ka liye hai

```r
a <- 10
b <- 20
c <- mean(a , b)

print(c) # 10


a <- c(40 , 40)
c <- mean(a)

print(c) # 40
```

## `max()`

```r
a <- 10
b <- 20
c <- max(a , b)

print(c) # 20


a <- c(40 , 40 , 100 , 90)
c <- max(a)

print(c) # 100
```

### 💡 Examples:

```R

# 2. Square Root
print(sqrt(81))
# Output: 9

# 3. Logarithm (Base 10)
print(log(100, base = 10))
# Output: 2 (kyunki 10 ki power 2 = 100)

# 4. Rounding
print(round(5.678, digits = 1)) # Round to one decimal place
# Output: 5.7

# 5. Ceiling aur Floor
print(ceiling(8.1))  # 8.1 se bada nearest whole number
# Output: 9

print(floor(8.9))    # 8.9 se chota nearest whole number
# Output: 8