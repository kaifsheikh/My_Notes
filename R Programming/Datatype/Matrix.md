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