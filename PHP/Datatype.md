# What is Array?
1. Array ek aisa datatype hota hai jo multiple values ko ek hi variable mein store karta hai.
2. Array ke andar different types ka data store ho sakta hai.
3. Array ka andar hum Nested Array or Function bhe Create kar sekhte hai mein
4. jab hum array banate ho, to har value ka ek number hota hai jise hum index kehte hain.

## Examples:
```php 
$fruits = ["Apple", "Banana", "Mango"];
echo $fruits[0]; // Apple
echo $fruits[2]; // Mango
```

# What is Associative Array?
1. Associative array wo array hota hai jisme har value ko ek unique naam (key) ke zariye store kiya jata hai, jise hum key-value pair kehte hain.

## Examples:
``` php
$student = [
  "name" => "Ali",
  "age" => 20,
  "class" => "10th"
];

echo $student["name"];  // Output: Ali
echo $student["age"];   // Output: 20
echo $student["class"]; // Output: 10th
```

# What is Multidimensional Array `(Array ke andar array)`?
1. Array ke andar ek ya zyada arrays ho sakte hain.
2. Complex data ko store karne ke liye use hota hai, jaise tables, products etc.

## Examples:
``` php
$students = [
    ["Ali", 21, "Male"],
    ["Sara", 20, "Female"],
    ["Ahmed", 22, "Male"]
];

echo $students[1][0]; // Sara
```

# What is `Associative` + `Multidimensional` Array?

## Examples:
``` php
$students = [
    "student1" => ["name" => "Ali", "age" => 21],
    "student2" => ["name" => "Sara", "age" => 20]
];

echo $students["student2"]["name"]; // Sara
```

# Methods of Array?

```php
print_r(array_keys($person)); 
print_r(array_values($person));
sort($fruits);
rsort($fruits); 
```


