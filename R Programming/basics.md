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

https://youtu.be/73vO2EAZKdE?si=sGvvPP_VlFWDyeY9&t=2523
E-Book : https://codanics.com/books/abc-of-statistics-for-data-science/