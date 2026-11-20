### 1. Billing & E-Commerce (Discount & Tax Calculation)

```py
def calculate_final_price(price, discount_percent, tax_percent):
  discount_amount = price * (discount_percent / 100)
  after_discount = price - discount_amount
  tax_amount = after_discount * (tax_percent / 100)
  final_total = after_discount + tax_amount
  return round(final_total, 2)


# Students ke liye simple input
price = float(input("Item actual price: "))
discount = float(input("Enter Discount % : "))
tax = float(input("Enter Tax % : "))

# Function ko call karna
total = calculate_final_price(price, discount, tax)

print("Final Bill:", total)
```

---

### 2. User Input Validation (Email ya Password Check Karna)

```py
def is_strong_password(password):
  has_length = len(password) >= 8
  has_upper = not password.islower()
  has_not_only_letters = not password.isalpha()
  return has_length and has_upper and has_not_only_letters


# User se password input lena
user_pass = input("Apna password likhein: ")

if is_strong_password(user_pass):
  print("Password strong hai!")
else:
  print(
      "Password must be at least 8 characters long, include a capital letter, and not contain only letters."
  )
```

---

### 3. Data Cleaning & Formatting (Text ya Strings Saaf Karna)

```python
def format_phone_number(phone):
  # Extra spaces, dashes (-) aur spaces hatana
  cleaned = phone.strip().replace("-", "").replace(" ", "")

  # Error handling: sirf digits hon, 0 se start ho, aur 11 digits ka ho
  if not cleaned.isdigit():
    return "Error: Phone number must contain only digits."
  elif not cleaned.startswith("0"):
    return "Error: Phone number must start with 0."
  elif len(cleaned) > 11:
    return "Error: Phone number must not be more than 11 digits."
  elif len(cleaned) < 11:
    return "Error: Phone number must not be less than 11 digits."

  # Sab theek ho to +92 mein badalna
  return "+92" + cleaned[1:]


# User se phone number input lena
user_phone = input("Enter your phone number (e.g. 0300-1234567): ")

result = format_phone_number(user_phone)

if result.startswith("Error:"):
  print(result)
else:
  print("Formatted Number:", result)
```

---
