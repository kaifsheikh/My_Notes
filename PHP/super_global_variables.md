## Superglobal Variables Kya Hain?
PHP mein **Superglobal Variables** woh built-in (pehle se bane hue) variables hote hain, jo script ke **kisi bhi hissay** (chahe woh function ho, class ho, ya main file) mein hamesha access kiye ja sakte hain. Inhein access karne ke liye `global $variable;` likhne ki zaroorat nahi padti. Yeh "Super" isliye hain kyunki ye hamesha "Global scope" mein rehte hain.

### Purpose (Yeh Kyun Zaruri Hain?)
Inka main maqsad web application mein **user se data lena**, **server ki information handle karna**, aur **user ka session (login status) maintain rakhna** hai. Bina in superglobals ke, aap ek dynamic website nahi bana sakte jo user ke input par respond kare.

---

## HTTP Methods Kya Hain?
HTTP Methods browser (client) aur server ke beech mein communicate karne ka tareeka hain. Jab aap browser mein kuch type karte hain ya click karte hain, browser server ko ek request bhejta hai. HTTP Method server ko batata hai ki aap **kya action** perform karna chahte hain.

1. **GET**: "Server, mujhe yeh data **dikhao**." (Sirf view karne ke liye)
2. **POST**: "Server, yeh naya data **save kar lo**." (Naya record banane ke liye)

---

## Complete List of Superglobals
1. `$_GET`
2. `$_POST`
3. `$_REQUEST`
4. `$_SERVER`
5. `$_SESSION`
6. `$_COOKIE`
7. `$_FILES`
8. `$_ENV`
9. `$GLOBALS`

---

## 1. `$_GET` Superglobal (Deep Dive)

### **Definition & Purpose**
`$_GET` PHP ka woh superglobal variable hai jo URL ke zariye bheje gaye data ko collect karne ke liye use hota hai. Jab bhi aap kisi link par click karte hain ya HTML form mein `method="GET"` use karte hain, toh woh data URL mein `?key=value` ki shakal mein jata hai aur `$_GET` ke zariye server par pohanchta hai.

**Iska main purpose data ko fetch (retrieve) karna hai.**

**HTML Form:**
```html
<form action="search.php" method="GET">
    <label>Search:</label>
    <input type="text" name="keyword">
    <button type="submit">Search</button>
</form>
```
*Jab user "PHP" likh kar submit karega, toh URL ban jayega: `search.php?keyword=PHP`*

**PHP (`search.php`):**
```php
<?php
if (isset($_GET['keyword'])) {
    $search = htmlspecialchars($_GET['keyword']);
    echo "Aap ne search kiya: " . $search;
}
?>
```

### **Important Limitations & Security (Must Read)**
1. **Visible Data:** URL mein data nazar aata hai, isliye **Kabhi Bhi Password ya Credit Card number `$_GET` se na bhejein**.
2. **Length Limit:** URL ki ek limit hoti hai, isliye bahut bada data `$_GET` se nahi bheja ja sakta.
3. **XSS Security Risk:** `$_GET` se aaya hua data hamesha insecure hota hai. Hamesha `htmlspecialchars()` use karein taake XSS attacks se bacha ja sake.

---

## 2. `$_POST` Superglobal

### **Definition & Purpose**
`$_POST` PHP ka woh superglobal variable hai jo HTML form se bheje gaye data ko secure tareeqay se collect karne ke liye use hota hai. Jab aap form mein `method="POST"` use karte hain, toh data URL mein nazar nahi aata, balkay HTTP request ki "body" mein chupa hua jata hai.

**Iska main Purpose data ko submit karna (ya save) karwana horta hai, specially sensitive data.**

```html
<form action="" method="POST">
    <label>Email:</label>
    <input type="email" name="email" required>
    
    <label>Password:</label>
    <input type="password" name="password" required>
    
    <button type="submit" name="submit">Login</button>
</form>
```

```php
<?php
if (isset($_POST["submit"])) {
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'];

    echo "<pre>";
        print_r($_POST);
    echo "</pre>";
}
?>
```

### **Features:**
- **Security:** Data URL mein visible nahi hota, isliye yeh passwords aur private info ke liye best hai.
- **Capacity:** Iski koi strict limit nahi hoti, aap bari files ya bahut zyada data bhej sakte hain.
- **Action:** Form resubmission ka warning aata hai agar user page refresh kare (jo double form submission rokne mein madad karta hai).

---

## 3. Comparison Table: `$_GET` vs `$_POST`

Yeh table in dono methods ke farq ko saaf samajhne mein madad karegi:

| Feature | `$_GET` | `$_POST` |
| :--- | :--- | :--- |
| **Data Visibility** | Data URL mein query string ki tarah nazar aata hai. | Data HTTP request body mein hota hai, URL mein nahi dikhta. |
| **Security** | Insecure (Sensitive info ke liye nahi). | Secure (Passwords aur private data ke liye best). |
| **Data Capacity** | Limited (2000 characters tak). | Large / Unlimited (Server config par depend karta hai). |
| **Bookmarkable** | Yes (URL save aur share ho sakta hai). | No (POST data bookmark nahi ho sakta). |
| **Main Purpose** | Data mangna (Retrieving/Fetching data). | Data bhejna (Submitting/Saving data). |
| **Form Method** | `method="GET"` | `method="POST"` |

---

## 4. `$_REQUEST` Superglobal

### **Definition & Purpose**
`$_REQUEST` ek combined associative array hai jo `$_GET`, `$_POST`, aur `$_COOKIE` teeno mein maujood data ko ek jagah collect karti hai.

**Iska main maqsad yeh hai ke jab aapko confirm na ho ke data GET se aa raha hai ya POST se, tab aap sirf `$_REQUEST` use karke dono ka data access kar sakte hain.**

### **Example**
```php
<?php
// Chahe data GET se aaye ya POST se, $_REQUEST dono mein kaam karega
if (isset($_REQUEST['username'])) {
    echo "Welcome: " . htmlspecialchars($_REQUEST['username']);
}
?>
```
*Note: Safety ke liye aksar developers `$_GET` ya `$_POST` ko alag-alag use karna prefer karte hain.*

---

## 5. `$_SERVER` Superglobal

### **Definition & Purpose**
`$_SERVER` ek superglobal array hai jo server ke environment, script ki location, headers, aur client ki request ki tafseelat (details) hold karta hai. Is array mein data **web server** khud bharta hai.

**Iska main maqsad server aur request ki technical details janna hai.**

### **Useful Keys & Examples**
```php
<?php
// 1. Current script ka path janna
echo "Script Path: " . $_SERVER['PHP_SELF'];

// 2. Request method check karna (GET ya POST?)
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    echo "Form was submitted via POST method!";
}

// 3. User ka IP address janna
echo "User IP: " . $_SERVER['REMOTE_ADDR'];

// 4. Server ka naam janna
echo "Server Name: " . $_SERVER['SERVER_NAME'];
?>
```
