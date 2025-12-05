# Raw (Data)
1. `Raw Data` = Wo data jo tum dekh saktay ho aur samajh saktay ha like.
2. (`Number` , `Names` , `Excel Files`, `Students marks`)
3. lakin ho sekhta hai ka wo `Raw Data` abhi `process` mein ho means.
4. Data clean na ho
5. ya analyze nahi hua ho
6. yeah kch values galat ho in sub ko sub `Raw Data` bolte hai

| Name  | Age | Marks |
| ----- | --- | ----- |
| Ali   | 20  | 85    |
| Sara  |     | 90    |
| Ahmed | 21  | abc   |

- Sara ka `Age` missing hai
- Ahmed ke Marks mein `“abc”` galat value hai
- Jab tak yeh data saaf (clean) nahi hota, tab tak yeh `Raw data` hi kehlata hai.

## Binary Data or Bytes:
1. Raw Data = jo hum dekh sekhte hai means `Human Readable` (Name , Age , City , Excel Files).
2. Binary Data = Jo computer dekhta hai or samajta hai (`01000001` , `01101100` , `01101001`)

## Bytes:
1. Byte data Measure kane ka ka aik chhota sa (unit) hai.
2. Tumhara mobile, laptop, video, image, Excel file — sab ka size BYTES mein measure hoti hai.
3. Computer sirf `0 - 1` samajta hai
4. `8 Bits` = `1 Byte`

## Example:
- Ager mein koi `Single Charater` be type karta ho like (`A` , 1 , `Z`) tu wo Usually `1 Byte` ka hota hai:

| Tum Kya Likhte Ho | Kitne Characters | Kitne Bytes | Kitne Bits |
| ----------------- | ---------------- | ----------- | ---------- |
| A                 | 1                | 1 Byte      | 8 Bits     |
| 1                 | 1                | 1 Byte      | 8 Bits     |
| AB                | 2                | 2 Bytes     | 16 Bits    |
| 12                | 2                | 2 Bytes     | 16 Bits    |
| Ali               | 3                | 3 Bytes     | 24 Bits    |
| 1234              | 4                | 4 Bytes     | 32 Bits    |
| abc               | 3                | 3 Bytes     | 24 Bits    |
| 1234abcd          | 8                | 8 Bytes     | 64 Bits    |
| Hello             | 5                | 5 Bytes     | 40 Bits    |

## Formula:
### **Bytes * 8 = Bits** 

## Examples of Working Raw Data in R

## nchar()
```r
x2 <- "1234abcd"

nchar(x2 , type = "chars") # 8 Character -> yeah Charaters ko count karta hai
nchar(x2 , type = "bytes") # 8 Bytes  -> yeah Bytes ko count karta hai

```
## charToRaw()
1. `charToRaw()` function use hota hai HEX output dekhne ke liye
1. HEX ya Hexadecimal ek number system hai jisme 16 digits ka use hota hai
2. Digits = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
3. Hexadecimal = Short form hai Binary ka `0/1`

```r
x1 <- "A"
charToRaw("x1") # 41 -> yah Hexadecimal (1 byte)


x1 <- "Hii"
charToRaw("x1") # 31 32 33 -> yah Hexadecimal (3 bytes)


x <- charToRaw("Hi")
text <- rawToChar(x)
print(text) # output: Hi


x <- charToRaw("A") # Hexadecimal
bits <- rawToBits(x) # Hexadecimal se Bits mein convert kardiya
print(bits) # 10000010

```

## as.raw()
1. `as.raw()` kisi bhi number ko 0 se 255 ke beech wale raw byte mein badal deta hai.
2. Ye hexadecimal format hota hai

```r
y <- as.raw(100)
print(y) # Output: 64
```

## object.size()
1. R object (vector, dataframe, list etc.) RAM me kitni memory le raha hai ye batata hai

```r
v <- c("A", "B", "C")
object.size(v) # 160 bytes


a <- "H"
b <- object.size(x)
print(b) # 112 Bytes

```

## is.na()
1. Check karta hai missing values (NA) ko
2. jo Value Missing hoge waha per `TRUE` likha ayga
   
```r
x1 <- c("A", "B", NA, "C")
is.na(x1) # FALSE FALSE TRUE FALSE
```

## na.omit()
1. Check karta hai missing values (NA) ko or oisa `Remove` kar dyta hai

```r
raw_data <- c(12, 45, NA, 30)
clean_data <- na.omit(raw_data)

clean_data # 12 45 30 -> NA ko remove kardiya
```

## as.numeric()
1. Raw data ko numeric type me convert karne ke liye
2. String numbers ko actual numbers me badal do
3. Jo convert na ho sake oisa → NA

```r
raw_data <- c("12", "45", "N/A", "30")
numeric_data <- as.numeric(raw_data)

numeric_data # 12 45 NA 30
```

## gsub(pattern, replacement, x)
```r
raw_data <- c("12", "45", "N/A", "error", "30")
cleaned <- gsub("N/A|error", NA, raw_data)
cleaned # "12" "45" NA NA "30"
```





# Task:

```r
# Raw Data (unprocessed)
raw <- c("23", "45", "N/A", "32", "-1")

# Step 1: Convert to numeric, replace "N/A" & negative with NA
clean <- as.numeric(raw)
clean[clean < 0] <- NA

# Step 2: Summary
summary(clean)
```