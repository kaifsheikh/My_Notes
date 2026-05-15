# What is Class?
1. Class ek design / blueprint hota hai isme hum Rules ko set karte hai means.
2. Class khud real cheez nahi hoti, sirf batati hai cheez kaisi hogi. isko `Mobile` Example se samjte hai.
3. ager hum Mobile ki baat karta ho ka oiska design paper par bana hua (wo khud mobile nahi, sirf design hai)
4. Class ka andar hum 2 cheeza define karte hai sirf `Properties (Varaibles)` or `Function (Methods)`
4. ab mobile ka andar kia kia hota hai:

| **Real Life Example**        | **Programming (PHP OOP)** |
| ---------------------------- | ------------------------- |
| Mobile ka **design / model** | **Class**                 |
| Color                        | **Variable (Property)**   |
| Brand                        | **Variable (Property)**   |
| Price                        | **Variable (Property)**   |
| Call karna                   | **Function (Method)**     |
| Message bhejna               | **Function (Method)**     |
| Music sunna                  | **Function (Method)**     |
| Asal mobile (haath mein)     | **Object**                |


# What is Object?
1. `Object` class ka real form hota hai means `Object` = asal cheez jo hum use karte hain.
2. Object banaya hi is liye jata hai taake hum class ke andar wali cheezon ko use kar saken.
3. Class ke andar hum jo `properties` aur `functions` ko define karte hain, oihne actual mein `Object` ki madad se `access` karke use karte hain. Access humesha Object ke through hota hai.
4. Without Object hum kabe bhe Class ka andar ki Properties ko or Function ko Access nahe kar sekhte hai.

```pgsql
Class (Mobile)
 ├── Variables (color, brand, price)
 └── Functions (call, message, music) 

Object ($myMobile)
 ├── color = Black
 ├── brand = Samsung
 └── price = 50000
```

# What is Constructor?
1. `Constructor` ko hum `def __init__():` function bhe bolte hai.
2. __init__ ek aisa function hai jo APNE AAP chal jaata hai, jab aap koi naya object banate ho. Iska kaam hai uss naye object ki basic settings set karna.