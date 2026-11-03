# 1. Encapsulation:

**Encapsulation** ka matlab hai: **"Data ko chhupana (hide karna) aur us tak pahunchne ka ek control/system banwana."**

means aap apne class ke andar jo data (properties/variables) hain, unko **directly bahar se access hone se rokna** aur unko access karne ka ek **sirf ek hi tareeqa (method)** dena.

# 2. why it's important:

Agar aap properties ko `public` chhod denge, toh koi bhi bahar se aake unko **kuch bhi** kar sakta hai — galat value daal sakta hai, delete kar sakta hai, modify kar sakta hai. Ye **data corruption** hai.

| Purpose                    | Meaning                                                                   |
| -------------------------- | ------------------------------------------------------------------------- |
| **Data Protection**        | Bahar se koi directly data change nahi kar sakta                          |
| **Validation**             | Galat value aane se pehle check kar sakte ho (e.g., age -5 nahi ho sakti) |
| **Controlled Access**      | Data ko sirf define kiye gaye methods se hi access kar sakte ho           |
| **Easy Maintenance**       | Andar ka code badal do, bahar wala code nahi tootega                      |
| **Security**               | Sensitive info (password, balance) safe rehti hai                         |
| **Read-only / Write-only** | Aap decide kar sakte ho — sirf read karo ya sirf write karo               |

---

# 1. Getter & Setter:

- **Getter** = Ek method jo property ki **value padhne (get)** ke liye use hota hai. Naam aksar `getXXX()` hota hai naam kch rekh sekhte hai.
- **Setter** = Ek method jo property ki **value set/change** karne ke liye use hota hai. Naam aksar `setXXX()` hota hai naam kch rekh sekhte hai.

- Property ko `private` banao (taake bahar se direct access na ho)
- Getter/Setter ko `public` banao (taake bahar se inhi ke through access ho)

## 📖 Getter & Setter — Complete Combined Table

| #   | Purpose (Maqsad)                                  | Getter Ka Kaam (Read)                                                   | Setter Ka Kaam (Write)                                                          | Simple Words Mein Matlab                                                                                                 |
| --- | ------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1   | **Data Access** (Data tak pahunchna)              | Private property ki value bahar nikal kar dena                          | Private property mein value daalna                                              | Data chhupa hua hai — getter se padho, setter se likho. Direct haath nahi daal sakte.                                    |
| 2   | **Data Protection** (Data bachana)                | Value sirf dikhana, change nahi karne dena                              | Change karne se pehle check karna ke allowed hai ya nahi                        | Bahar wala data ko **bigaad na sake** — sirf sahi tareeqe se change ho.                                                  |
| 3   | **Validation** (Ghalat value rokna)               | Usually nahi — value already valid hoti hai                             | **Haan** — galat value aane se pehle check karna (e.g., age `-5` nahi ho sakti) | Setter **darwaza** hai — andar aane se pehle check karta hai ke value sahi hai ya nahi. Getter sirf sahi value deta hai. |
| 4   | **Data Cleaning** (Data saaf karna)               | Nahi                                                                    | Value ko trim/sanitize karke store karna (extra spaces hatao)                   | Setter value ko **saaf karke** rakhta hai — jaise naam ke aage-peeche spaces hata dena.                                  |
| 5   | **Transformation** (Value badal kar rakhna)       | Formatted value dena (e.g., `getFullName()` = first + last)             | Value badal kar store karna (e.g., password ko **hash** karna)                  | Setter andar value ko **badal** deta hai (plain password → hash). Getter bahar **ready format** mein deta hai.           |
| 6   | **Security — Masking** (Sensitive cheez chhupana) | Sensitive data **hide/mask** karke dikhana (e.g., PIN ka last 4 digit)  | Sensitive data ko **hash/encrypt** karke store karna                            | Getter sensitive cheez **adhoori** dikhata hai. Setter usko **encrypt** karke rakhta hai — taake leak na ho.             |
| 7   | **Read-Only Access** (Sirf padhna)                | ✅ Sirf padhne ki permission dena                                       | ❌ Setter nahi — value change nahi ho sakti                                     | Jaise **balance** ya **order ID** — sirf dekh sakte ho, badal nahi sakte.                                                |
| 8   | **Write-Only Access** (Sirf likhna)               | ❌ Getter nahi — value padhi nahi ja sakti                              | ✅ Sirf likhne ki permission dena (e.g., password)                              | Jaise **password** — daal sakte ho, padh nahi sakte. Ek taraf ka rasta.                                                  |
| 9   | **Computed Value** (Calculate karke dena)         | Property se calculate karke value dena (e.g., `getAge()` birth date se) | —                                                                               | Getter andar calculate karke **taiyar value** deta hai — jaise date of birth se age nikaalna.                            |
| 10  | **Business Rule Enforce** (Rule follow karwana)   | —                                                                       | Rules follow karwana (e.g., price negative nahi ho sakti)                       | Setter **company ke rules** lagata hai — jaise price kabhi minus nahi hogi.                                              |
| 11  | **Encapsulation** (Data ko band karna)            | Data `private` rakhna, sirf getter se bahar jaane dena                  | Data `private` rakhna, sirf setter se andar aane dena                           | Data **dibbe mein band** hai — bahar jaane ka rasta getter, andar aane ka rasta setter.                                  |
| 12  | **Easy Maintenance** (Future mein aasan badlav)   | Andar ka code badlo, bahar wala nahi tootega                            | Andar ka code badlo, bahar wala nahi tootega                                    | Andar ka **system badal do** — bahar wala code waise hi chalta rahega.                                                   |
| 13  | **Safe Access** (Safe value dena/lena)            | Null/empty check karke safe value return karna                          | Default value ya extra logic chalana value set karte waqt                       | Getter kabhi **crash nahi** karta — null ho toh safe value deta hai. Setter **default** bhi set kar sakta hai.           |

---

## Example — Bina Encapsulation

```php
<?php
class User {
    public $name;
    public $age;
    public $balance;
}

$user = new User();

$user->name = "Ali";
$user->age = -50;
$user->balance = 99999999;

echo $user->age;
?>
```

## Example Encapsulation + Getter/Setter

```php
<?php
class User {
    // Properties private — bahar se direct access nahi
    private $name;
    private $age;
    private $balance;

    // Setter for name
    public function setName($name) {
        $name = trim($name);
        if (strlen($name) < 2) {
            throw new Exception("Name must be greater then 2 characters");
        }
        $this->name = $name;
    }

    // Getter for name
    public function getName() {
        return $this->name;
    }

    // Setter for age — yahan validation
    public function setAge($age) {
        if (!is_numeric($age)) {
            throw new Exception("Age must bhe a number");
        }
        if ($age < 0 || $age > 120) {
            throw new Exception("Age must bhe under 100");
        }
        $this->age = $age;
    }

    // Getter for age
    public function getAge() {
        return $this->age;
    }

    // Balance ke liye sirf getter (read-only) — koi direct set nahi
    public function getBalance() {
        return $this->balance;
    }

    // Balance change karne ka tarika (business logic ke saath)
    public function deposit($amount) {
        if ($amount <= 0) {
            throw new Exception("Deposit amount positive hona chahiye");
        }
        $this->balance += $amount;
    }

    public function withdraw($amount) {
        if ($amount > $this->balance) {
            throw new Exception("Insufficient balance");
        }
        $this->balance -= $amount;
    }
}
?>
```

```php
<?php
class Product {
    private $name;
    private $price;
    private $stock;

    public function setName($name) {
        if (trim($name) === '') {
            throw new Exception("Product name khali nahi ho sakta");
        }
        $this->name = trim($name);
    }

    public function getName() {
        return $this->name;
    }

    public function setPrice($price) {
        if (!is_numeric($price) || $price < 0) {
            throw new Exception("Price positive number hona chahiye");
        }
        $this->price = $price;
    }

    public function getPrice() {
        return $this->price;
    }

    public function setStock($stock) {
        if (!is_int($stock) || $stock < 0) {
            throw new Exception("Stock 0 ya usse zyada integer hona chahiye");
        }
        $this->stock = $stock;
    }

    public function getStock() {
        return $this->stock;
    }

    // Business method — kuch rule ke saath
    public function sell($qty) {
        if ($qty <= 0) throw new Exception("Quantity positive honi chahiye");
        if ($qty > $this->stock) throw new Exception("Stock kam hai");
        $this->stock -= $qty;
    }
}

// Usage
$p = new Product();
$p->setName("Laptop");
$p->setPrice(85000);
$p->setStock(10);

$p->sell(3);   // ✅ 3 laptop sold
echo "Remaining stock: " . $p->getStock();  // 7

$p->sell(50);  // ❌ Exception: Stock kam hai
$p->setPrice(-100); // ❌ Exception: Price positive hona chahiye
?>
```
