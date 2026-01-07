# What is Class?
1. Class ek design / blueprint hota hai isme hum Rules ko set karte hai sirf means.
2. Class khud real cheez nahi hoti, sirf batati hai cheez kaisi hogi. isko `Mobile` Example se samjte hai.
3. ager hum Mobile ki baat kare ka oiska design paper par bana hua (wo khud mobile nahi, sirf design hai)
4. Class ka andar hum 2 cheeza define karte hai sirf:
5. > `Properties (Varaibles)` <br>
6. > `Function (Methods)` <br>
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

# What is Public?
1. public aik `access modifier` hai jo `Class` ka andar use hota hai.
1. jo bhe `Property` yeah `Function` Public ho oisa hum kahe se bhe `Access` kar sekhte hai means.
3. `property` ya `function` ko hum class ke andar se bhi access karte sekhte hai or Class ka bahir se bhe.

### class ka bahir value ko Get or Set kaise karte hai `Without` Function:
```php
class Mobile {
    
    public $brand;
    public $color;
    public $price;

}

$myMobile = new Mobile(); // Object

// Option: 01 (Property ko Set or Get yehi per karwa diya)
echo $myMobile->brand = "Sumsung" . "<br>";
echo $myMobile->color = "Black" . "<br>";
echo $myMobile->price = 500000;

// Option: 02 (Properties ko Set kiya)
$myMobile->brand = "Samsung";
$myMobile->color = "Black";

// Option: 02 (Properties ko Get kiya)
echo "Brand: " . $myMobile->brand . "<br>";
echo "Color: " . $myMobile->color;

// yeah humne Class ka bahir se Properties ko Access kiya hai Object ka Through or Public ki waja se
```
### Class ka andar Properties ko Values kaise Set karte hai or bahir kaise Access karte hai Properties ko `without function`:
```php
class Mobile {
    public $brand = "Toyota";
    public $color = "Red";

    // Class ka andar he Properties ko Values Assign karde hai
}

$mobile = new Mobile(); // Object

// yeah per Properies ko Get karliya hai.
echo $mobile->brand . "<br>";
echo $mobile->color;
```

### Function ka andar Properties ko Access karwana or Clasa ka bahir Access karna:

```php
class Mobile{

    public $brand;
    public $color;

    function mobileInfo(){
        echo "Brand Inside Function: " . $this->brand;
        echo "<br> Color Inside Function: " . $this->color;
    }
}

$myMobile = new Mobile();

$myMobile->brand = "Sumsung";
$myMobile->color = "Black";

$myMobile->mobileInfo();
```

# What is $this in OOP?
1. Basic Rule: $this sirf class ke andar use hota hai class ka bahir kaabe bhe use nahe hoga.
2. $this = yeah Current Object ka liya use hota hai means.
3. 