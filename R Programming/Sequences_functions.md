# What is Sequences functions?
1. Sequence functions wo functions hain jo R mein automatic number ki series banate hain — ek ordered pattern mein.

# Purpose kia hai isko use karne ka:
1. Sequence ka main Purpose hai Data ko automatically generate karna Manual writing se bachne ke liye.
1. Number ki line banana Order wise
2. ek number se start, ek number par end, aur beech ke sare numbers automatic generate ho jayein.
- 1 se 10 tak -> `counting`
- 2, 4, 6, 8, 10 -> `(even numbers)`
- 5, 10, 15, 20 -> `(constant gap wale numbers)`

## Examples:
```r
a <- seq(1 , 100)
print(a)
# 1 se 100 tak Number Generate hongay

a <- seq(from = 1 , to = 100)
print(a)
# yeah bhe same hai 1 se 100 tak Number Generate hongay

a <- seq(1 , 100 , by = 2)
print(a)
# iska matlab hai ka 1 se 100 tak chalayga lakin 1 ka bad 2 add karo or oisa print karo menas 1 , 3 , 5 , 7 , 9 , 11 , 13 , etc is terha se yeah gap hum by = 2 se karte hai 2 kia huga kch bhe number dy sekhte hai

a <- seq(1 , 100 , by = 2.5)
print(a)
# 1.0 , 3.5 , 6.0 , 8.5 , 11.0 , 13.5 , 16.0 , etc
```
## Examples (Length out Arugemt):
```r
a <- seq(1 , 100 , length.out = 5)
# 1 se 100 tak number generate hongay lakin wo sirf 5 values mein he Equally Divided honge Values like: 1.00  25.75  50.50  75.25 100.00
```

## along.with
1. `along.with` yeah vector ka elements ki total length nikal kar dyta hai ka oisme kitni number of values hai 
3. Matlab: agar aapke paas pehle se vector hai aur sequence chahiye uske size ke hisaab se tu `along.with`  use karte hai
4. `along.with` ka use sirf vector ke saath hota hai.

```r
a <- c(10 , 20 , 30 , 40)
seq(along.with = a)
# 1 , 2 , 3 , 4 -> kue ka a variable mein 4 values hai tu along.with ne vector a ki lenght batai hai 4 or yeah 1 se count hota hai.

x <- c(10, 20, 30, 40)
seq_along(x)
# 1 , 2 , 3 , 4 

y <- c("a" , "b" , "c" , "d" , "e")
seq(from = 100, along.with = y)
# means ka 100 se start hoga number or y ki length count karayga -> 100 101 102 103 104 -> isko hum kisi bhe number se start kar sekhte hai
```

# What is X-Axis or Y-Axis
1. Jab aap graph dekhte ho (charts), to 2 lines hoti hain.

## Type of Lines
## **Horizontal line → X-axis -> (left to right)**
- Agar hum “1 se 10 tak numbers” graph mein dikhna chahte hain, to hum unko X-axis pe rakhte hain.
- R language ko X-axis ke liye numbers chahiye hote hain. Wo numbers hum sequence se bana lete hain:

```r
seq(1 : 10)
```

## **Vertical line → Y-axis -> (bottom to top)**
1. Y-axis wo hoti hai jahan values dikhayi jaati hain means.
2. ager humera pass 10 din ka temperature Data hai like:
- Day 1 → 20°C
- Day 2 → 22°C
- Day 3 → 24°C

> Day 1, 2, 3...10 = X-axis <br>
> 20, 22, 24... = Y-axis values <br>
> Graph banane ke liye dono chahiye.

