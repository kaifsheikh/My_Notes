# What is Class?

1. Class ek design / blueprint hota hai isme hum Rules ko set karte hai means.
2. Class khud real cheez nahi hoti, sirf batati hai cheez kaisi hogi. isko `Mobile` Example se samjte hai.
3. ager hum Mobile ki baat karta ho ka oiska design paper par bana hua (wo khud mobile nahi, sirf design hai)
4. Class ka andar hum 2 cheeza define karte hai sirf `Properties (Varaibles)` or `Function (Methods)`
5. ab mobile ka andar kia kia hota hai:

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

## What is Properties:

1. Property ek variable hai jo class ke andar declare hoti hai. Iska kaam hai object ki information (data) ko store karna. Har object ki apni alag properties hoti hain.

## What is Method:

1. Method ek function hai jo class ke andar likha jata hai. Iska kaam hai koi kaam/action perform karna — jaise data ko process karna, calculate karna, ya output dena.

2. Method Properties ke data par operations perform karta hai or Code ko reusable aur organized banana.

```pgsql
Class (Mobile)
 ├── Variables (color, brand, price)
 └── Functions (call, message, music)

Object ($myMobile)
 ├── color = Black
 ├── brand = Samsung
 └── price = 50000
```

## `->` - what is this arrow:

1. `->` ek operator hai jo PHP mein object ke andar jaa kar uski property ya method ko access karne ke liye use hota hai. Ye PHP ko batata hai ke 'is object ke andar jao aur ye cheez lo.

## What is `Public`

1. public ek access modifier hai jo batata hai ke koi property ya method kahan se access ho sakti hai. Jab kisi cheez ko public likha jaye, to usay har jagah se access kiya ja sakta hai — class ke andar bhi, bahar bhi, aur child class se bhi.

## What is `Private`

1. private ek access modifier hai jo sabse zyada restriction lagata hai. Jab kisi property ya method ko private likha jaye, to usay sirf usi class ke andar access kiya ja sakta hai — class ke bahar se nahi, aur child class se bhi nahi. Ye bilkul personal locker ki tarah hai.

## What is `$this`

1. $this ek special variable hai jo class ke andar current object ko refer karta hai. Jab kisi method ke andar $this likhte hain, to iska matlab hota hai 'ye wala object' — yani woh object jisne is method ko call kiya hai. Iski madad se hum usi object ki properties aur methods ko access karte hain.

## Example:

```php
<?php
// Class
class Car {
    public $brand;
    public $color;

    // Method
    public function start() {
        echo "Car started now... <br>";
    }

    // Method
    public function showInfo() {
        echo "Brand: " . $this->brand . "<br>";
        echo "Color: " . $this->color . "<br>";
    }
}

// Object
$car1 = new Car();
$car1->brand = "Toyota";
$car1->color = "White";

$car1->start();
$car1->showInfo();
?>
```

## Example:

```php
<?php
class ShoppingCart {
    // PROPERTIES
    public $customerName;
    private $items = [];
    private $total = 0;

    // METHOD — item add karna
    public function addItem($itemName, $price) {
        $this->items[] = $itemName;
        $this->total += $price;
        echo $itemName . " item added in card (" . $price . " Rs)<br>";
    }

    // METHOD — total karna
    public function showTotal() {
        echo $this->customerName . " total: " . $this->total . " Rs<br>";
        echo "Items: " . implode(", ", $this->items) . "<br>";
    }
}

// ===== Object 1 =====
$cart1 = new ShoppingCart();
$cart1->customerName = "Ali";
$cart1->addItem("Laptop", 50000);
$cart1->addItem("Mouse", 1500);
$cart1->showTotal();

echo "<br>";

// ===== Object 2 =====
$cart2 = new ShoppingCart();
$cart2->customerName = "Sara";
$cart2->addItem("Mobile", 25000);
$cart2->showTotal();
?>
```

## Example:

```php
<?php
class RestaurantOrder
{
    // 🟢 PUBLIC
    public $customerName;
    public $tableNumber;

    // 🔒 PRIVATE — Menu
    private $menu = [
        1 => ["Biryani", 350],
        2 => ["Burger", 500],
        3 => ["Pizza", 800],
        4 => ["Raita", 50],
        5 => ["Cold Drink", 100],
    ];

    // 🔒 PRIVATE — Order data
    private $items = [];
    private $prices = [];
    private $quantities = [];
    private $isCancelled = false;

    // 🔵 METHOD — Menu dikhana
    public function showMenu()
    {
        echo "\n===== MENU =====\n";
        foreach ($this->menu as $num => $item) {
            echo $num . ". " . $item[0] . " — " . $item[1] . " Rs\n";
        }
        echo "================\n";
    }

    // 🔵 METHOD — Menu number + quantity se order
    public function orderItem($menuNumber, $quantity)
    {
        if ($this->isCancelled) {
            echo "❌ Order cancel\n";
            return false;
        }
        if (!isset($this->menu[$menuNumber])) {
            echo "❌ Wrong Menu!\n";
            return false;
        }
        if ($quantity <= 0) {
            echo "❌ Quantity must bhe greater than 0\n";
            return false;
        }

        $itemName  = $this->menu[$menuNumber][0];
        $itemPrice = $this->menu[$menuNumber][1];
        $lineTotal = $itemPrice * $quantity;

        $this->items[]      = $itemName;
        $this->prices[]     = $itemPrice;
        $this->quantities[] = $quantity;

        echo "✅ " . $quantity . "x " . $itemName . " = " . $lineTotal . " Rs\n";
        return true;
    }

    // 🔵 METHOD — Bill print
    public function printBill()
    {
        if ($this->isCancelled) {
            echo "Order cancelled\n";
            return;
        }
        if (count($this->items) == 0) {
            echo "⚠️ Nothing order!\n";
            return;
        }

        $grandTotal = 0;
        echo "\n========= BILL =========\n";
        echo "Customer: " . $this->customerName . " | Table: " . $this->tableNumber . "\n";
        echo "------------------------\n";

        for ($i = 0; $i < count($this->items); $i++) {
            $lineTotal = $this->prices[$i] * $this->quantities[$i];
            echo "- " . $this->items[$i] . " x" . $this->quantities[$i]
                . " = " . $lineTotal . " Rs\n";
            $grandTotal += $lineTotal;
        }

        echo "------------------------\n";
        echo "GRAND TOTAL: " . $grandTotal . " Rs\n";
        echo "========================\n";
    }

    // 🔵 METHOD — Cancel
    public function cancelOrder()
    {
        $this->isCancelled = true;
        echo "Order cancel ho gaya!\n";
    }
}

// ===================== USER INPUT LOOP =====================

$order = new RestaurantOrder();

echo "===== RESTAURANT ORDER SYSTEM =====\n";

// Customer naam lo
echo "Enter your Name: ";
$order->customerName = trim(fgets(STDIN));

// Table number lo
echo "Enter Table Number: ";
$order->tableNumber = trim(fgets(STDIN));

// Menu dikhao
$order->showMenu();

// Loop — jab tak user 'done' na likhe
while (true) {
    echo "\nMenu Number (0 = bill / 'c' = cancel): ";
    $input = trim(fgets(STDIN));

    // Bill chahiye?
    if ($input === "0") {
        break;
    }

    // Cancel?
    if (strtolower($input) === "c") {
        $order->cancelOrder();
        break;
    }

    // Quantity lo
    echo "Quantity: ";
    $quantity = trim(fgets(STDIN));

    // Order lagao (casting int)
    $order->orderItem((int)$input, (int)$quantity);
}

// Bill dikhao
$order->printBill();
```

# What is Constructor?

1. `Constructor` ko hum `def __init__():` function bhe bolte hai.
2. **init** ek aisa function hai jo APNE AAP chal jaata hai, jab aap koi naya object banate ho. Iska kaam hai uss naye object ki basic settings set karna.
