| Type             | Use / Meaning                           |
| ---------------- | --------------------------------------- |
| **if**           | Jab ek hi condition check karni ho      |
| **if-else**      | Jab do possibilities ho (true ya false) |
| **if-elif-else** | Jab multiple conditions check karni ho  |
| **nested if**    | Jab ek if ke andar aur if ho            |

## `Example 01 - if`
```py
if condition:
    # agar condition true ho to ye chalega
else:
    # agar condition false ho to ye chalega

---

age = 20

if age >= 18:
    print("You are an adult.")     # ager true hua tu yeah run hoga
else:
    print("You are not an adult.") # ager false hua tu yeah run hoga 

```
## `Example 02 - if–elif–else statement`
```py
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

# Output : Grade C
```
## `Example 03 - Nested if statement`
```py

age = 20
citizen = "Pakistan"

if age >= 18:
    if citizen == "Pakistan":
        print("You can vote in Pakistan.")
    else:
        print("You are not a Pakistani citizen.")
else:
    print("You are underage.")

# Output : You can vote in Pakistan.
```