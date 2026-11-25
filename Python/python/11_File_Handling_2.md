## 1. File Modes Kya Hain?

1. **mode** batata hai ke aap file ke saath kya kaam karne wale hain (sirf parhna hai, naya likhna hai, ya purane mein aage jorna hai).

### Sab Se Zaroori Modes

| Mode                 | Kaam Kya Hai?         | File **Pehle Se Hai** to kya hoga?                        | File **Nahi Hai** to kya hoga?           |
| -------------------- | --------------------- | --------------------------------------------------------- | ---------------------------------------- |
| **`"r"`** _(Read)_   | Sirf parhna           | File khul jati hai aur shuru se parhti hai                | **Error** (`FileNotFoundError`) aata hai |
| **`"w"`** _(Write)_  | Naya likhna           | Purana sab data **mitt** jata hai, phir naya likhta hai   | **Nayi file** ban jati hai               |
| **`"a"`** _(Append)_ | Akhir mein jorna      | Purana data **safe** rehta hai, uske aage naya likhta hai | **Nayi file** ban jati hai               |
| **`"x"`** _(Create)_ | Sirf nayi file banana | **Error** (`FileExistsError`) aata hai                    | **Nayi file** ban jati hai               |

### Extra Modes (`+` aur `b`)

- **`"r+"`** _(Read + Write)_: File parhne aur likhne dono ke liye (file pehle se honi chahiye).
- **`"w+"`** _(Write + Read)_: Purana data mitta kar naya likhne aur parhne ke liye.
- **`"a+"`** _(Append + Read)_: Akhir mein jorne aur parhne ke liye.
- **`"b"`** _(Binary mode)_: Jaise `"rb"` ya `"wb"` — images, audio, PDF ya binary files ke liye.

---

## 2. Har Mode Ki Simple Example

### Example 1: `"w"` Mode (Nayi file banana ya purana data mitta kar likhna)

```python
with open("student.txt", "w") as f:
    f.write("Naam: Ali\n")
    f.write("Class: 10\n")

```

- Agar `student.txt` nahi thi, to ban gayi.
- Agar pehle se thi aur usmein kuch likha tha, to woh **mitt** gaya aur sirf yeh 2 lines reh gayin.

---

### Example 2: `"a"` Mode (Purane data ke akhir mein naya likhna)

```python
with open("student.txt", "a") as f:
    f.write("City: Hyderabad\n")

```

- `Ali` aur `Class: 10` **wese hi rahenge**, aur unke neeche `City: Hyderabad` add ho jayega.
- Agar dobara chalayenge, to `City: Hyderabad` ek aur baar neeche add ho jayega.

---

### Example 3: `"r"` Mode (File ka data parhna)

```python
with open("student.txt", "r") as f:
    data = f.read()
    print(data)

```

- Output mein poori file ka text nazar aayega.
- **Dhyan:** Agar file ka naam ghalat likha ya file mojood na ho, to `FileNotFoundError` aayega.

---

### Example 4: `"x"` Mode (Sirf nayi file banane ke liye)

```python
try:
    with open("new_file.txt", "x") as f:
        f.write("Yeh bilkul nayi file hai.\n")
    print("File ban gayi!")
except FileExistsError:
    print("Yeh file pehle se mojood hai!")

```

- Pehli baar chalane par `new_file.txt` ban jayegi.
- Doosri baar chalane par error ke bajaye `"Yeh file pehle se mojood hai!"` print hoga, taake purani file overwrite na ho.

---

### Example 5: `"r+"` Mode (Parhna aur likhna ek saath)

```python
with open("student.txt", "r+") as f:
    purana = f.read()
    print("Pehle yeh tha:\n", purana)
    f.write("Status: Active\n")

```

- Pehle file ka data parh kar `purana` mein aaya, phir `f.write()` ne akhir mein `Status: Active` likh diya.

---

# Real life Example:

## 1. Login / Activity Log File

```python
from datetime import datetime

def log_activity(username, action="logged in"):
    waqt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    with open("login_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"[{waqt}] User '{username}' {action}.\n")

# Naye logs append honge (purane safe rahenge)
log_activity("ali_raza", "logged out")
```

### 1. Daily Expense Tracker:

```py
from datetime import datetime

file_name = "expenses.txt"

# 1. Get user input
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
today_date = datetime.now().strftime("%Y-%m-%d")

# 2. Append data to the file (old data is kept)
with open(file_name, "a", encoding="utf-8") as file:
    file.write(f"{today_date} | {product_name} | {price}\n")

print("Saved successfully!\n")

# 3. Read the file and show a simple summary
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Count products by counting lines (each entry is one line)
lines = content.strip().split("\n")
total_products = len(lines)

# Calculate total price without using a loop
prices = [float(line.split("|")[2].strip()) for line in lines]
total_price = sum(prices)

print("--- Final Summary ---")
print(f"Total Products: {total_products}")
print(f"Total Price: {total_price:.2f}")
```
