# Inheritance (Proper Definition)

> **Inheritance** ek OOP concept hai jismein ek **nayi class (child/subclass)** ek **pehle se maujood class (parent/superclass)** ki **properties aur methods ko inherit (apna)** kar leti hai — aur apni **nayi properties/methods bhi add** kar sakti hai.

### Definition (Simple Words Mein)

1. Inheritance means: Ek class dusri class ki saari cheezein (data + functions) ko apne class mein Inheri kar sekhti hai.

- **Parent class** = jo pehle se bani hui hai, usme common cheezein hain.
- **Child class** = jo parent ki cheezein **free mein** le leta hai + apni nayi cheezein add karta hai
- **Keyword** = `extends` (PHP mein)

**Ek line mein:** _"Ek class dusri class ko extend kare — parent ka sab kuch mile + apna kuch add kare."_

```php
<?php
// Parent class
class ParentClass {
    // properties + methods
}

// Child class — parent ko extend karo
class ChildClass extends ParentClass {
    // parent ka sab kuch automatically mil gaya
    // apni nayi cheezein add karo
}
?>
```

**Bas itna hi!** `ChildClass` ke paas ab `ParentClass` ka **saara public aur protected** data + methods hain.

## Example:

```php
<?php
// ============================================
// PARENT CLASS — Common for all payments
// ============================================
class Payment {
    protected $amount;
    protected $customerName;

    public function __construct($amount, $customerName) {
        $this->amount = $amount;
        $this->customerName = $customerName;
    }

    // Common method — har payment same tarah process hoti hai
    public function process() {
        echo "Processing payment of {$this->amount} for {$this->customerName}...<br>";
        $this->pay();   // Child apna pay() chalayega
        echo "✅ Payment successful!<br><br>";
    }

    // Child classes isko apne hisaab se badlengi
    public function pay() {
        echo "Generic payment<br>";
    }
}


// ============================================
// CHILD 1 — Credit Card (Stripe)
// ============================================
class CreditCardPayment extends Payment {
    private $cardNumber;

    public function __construct($amount, $customerName, $cardNumber) {
        parent::__construct($amount, $customerName);
        $this->cardNumber = $cardNumber;
    }

    public function pay() {
        $masked = "**** **** **** " . substr($this->cardNumber, -4);
        echo "💳 Charging card {$masked} via Stripe<br>";
    }
}


// ============================================
// CHILD 2 — PayPal
// ============================================
class PayPalPayment extends Payment {
    private $email;

    public function __construct($amount, $customerName, $email) {
        parent::__construct($amount, $customerName);
        $this->email = $email;
    }

    public function pay() {
        echo "🅿️ Sending money from PayPal account {$this->email}<br>";
    }
}


// ============================================
// CHILD 3 — JazzCash
// ============================================
class JazzCashPayment extends Payment {
    private $mobileNumber;

    public function __construct($amount, $customerName, $mobileNumber) {
        parent::__construct($amount, $customerName);
        $this->mobileNumber = $mobileNumber;
    }

    public function pay() {
        echo "📱 Sending OTP to {$this->mobileNumber} for JazzCash payment<br>";
    }
}


// ============================================
// REAL USE — Checkout page
// ============================================

// Customer ne Credit Card choose kiya
$payment1 = new CreditCardPayment(5000, "Ali", "4111111111111234");
$payment1->process();

// Customer ne PayPal choose kiya
$payment2 = new PayPalPayment(2500, "Sara", "sara@example.com");
$payment2->process();

// Customer ne JazzCash choose kiya
$payment3 = new JazzCashPayment(1200, "Bilal", "03001234567");
$payment3->process();
```
