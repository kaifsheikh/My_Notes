# `Datatypes` - R Language
1. R (programming language) mein, data ko store karne ke liye (6) (basic) data types hote hain.
   
2. **DataType** batata hai ke kisi variable mein kis type ka data store hua hai —  
number, text, TRUE/FALSE, ya kuch aur.  
R language ko yeh jaanna zaroori hota hai taake wo data ko sahi tarike se process kar sake.

# `Type of Datatypes:`
1. [Character](Character.md)
2. [Numeric](Numbers.md)
3. [Integer](Numbers.md)
4. Logical
5. Complex
6. [Raw](Raw_data.md)
---

# `Advanced Data Structures (Multiple values / group types)`
## `Definition`
R language me sirf single values (numbers, text, TRUE/FALSE) hi nahi balki **multiple values** ya **complex data** ko store karne ke liye kuch **data structures** bhi hote hain.  
Ye structures data ko **organize aur manage** karne me help karte hain — jaise list, table, matrix, etc.

---

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
numbers <- c(10, 20, 30, 40)
names <- c("Ali", "Ahmed", "Karlie")
logical_vec <- c(TRUE, FALSE, TRUE)
mix <- c(10, "Ali", TRUE) # yeah galat hojayga mixed datatype aik Vector mein store nahe karte hai

print(numbers) # Output: 10, 20, 30, 40
numbers[3]     # Output: 30
numbers[2:4]   # Output: 2 se 4 tak ki values ayge sirf
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