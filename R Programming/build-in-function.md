# 🔢 R Programming: Built-in Numeric Functions

yeah (Numeric/Integer) par kaam karne waale (important) built-in functions hai.

---

## 1. 📐 Mathematical Aur Elementary Functions

| Function | Maqsad (Purpose) | Syntax |
| :--- | :--- | :--- |
| `abs()` | Kisi number ki **Absolute Value** nikalna (negative sign hata deta hai). | `abs(x)` |
| `sqrt()` | **Square Root** nikalna. | `sqrt(x)` |
| `log()` | **Logarithm** nikalna. Base define kar sakte hain. | `log(x, base = e)` |
| `exp()` | **Exponential** value nikalna ($e^x$). | `exp(x)` |
| `round()` | Number ko **qareebi whole number/decimal** tak round karna. | `round(x, digits = 0)` |
| `ceiling()` | Number ko usse **bade** nearest whole number tak round karna. | `ceiling(x)` |
| `floor()` | Number ko usse **chote** nearest whole number tak round karna. | `floor(x)` |
| `trunc()` | Decimal hissa **hata** kar sirf Integer part rakhna. | `trunc(x)` |

### 💡 Examples:

```R
# 1. Absolute Value
print(abs(-15.7)) 
# Output: 15.7

# 2. Square Root
print(sqrt(81))
# Output: 9

# 3. Logarithm (Base 10)
print(log(100, base = 10))
# Output: 2 (kyunki 10 ki power 2 = 100)

# 4. Rounding
print(round(5.678, digits = 1)) # Round to one decimal place
# Output: 5.7

# 5. Ceiling aur Floor
print(ceiling(8.1))  # 8.1 se bada nearest whole number
# Output: 9

print(floor(8.9))    # 8.9 se chota nearest whole number
# Output: 8