# What is Middleware:
1. Middleware aik guard / filter hota hai jo request aur response ke beech mein kaam karta hai means.
2. Jab user browser se koi request bhejta hai (page open karne ke liye), controller tak pohanchne se pehle middleware us request ko check karta hai oiska bad wo Request Controller ka pass ati hai.
3. Middleware controller se pehle chalta hai.

> Agar request valid ho → aage jaane deta hai <br>
Agar request invalid ho → rok deta hai

```sql
Browser Request
      ↓
Middleware (Check)
      ↓
Controller
      ↓
View / Response
```
# Laravel mein 3 types ke middleware hote hain:

1. Global Middleware
2. Route Middleware
3. Middleware Groups

## GLobal Middleware:
1. Global Middleware har request par automatically chalta hai, chahe koi sa bhi route ho.
2. Har request is middleware se guzarti hai.

## Route Middleware:
1. Route middleware sirf un routes par chalta hai jahan tum usko manually lagate ho.

## Middleware Groups:
1. Middleware group ka matlab multiple middleware ko aik bundle mein use karna