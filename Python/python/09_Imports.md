## **Step 1: Do Python files create karne hai**

1. `main.py`
2. `my_functions.py`

### **Step 2: `my_functions.py`**

1. isme actual function create karna hai.

```py
def greet(name):
    return f"Hello {name}!"
```

### **Step 3: `main.py`**

1. isme ois function ko use karna hai muje

```py
from my_functions import

greetresult = greet("Kaif")
print(result)
```

**Output:**

```
Hello Kaif!
```

---

### **Step 1: Do files create karo**

```
my_project/
│
├── subtraction.py
│
└── main.py
```

### **Step 2: `subtraction.py`**

Is file mein subtraction ka pura logic hoga.

```py
def subtract(num1, num2):
    result = num1 - num2
    return result
```

### **Step 3: `main.py`**

isme actual function ko import karke use karna hai.

```py
from subtraction import subtract

answer = subtract(20, 10)
print("Subtraction Answer:", answer)
```

---

## **1. Project structure**

```
ATM_Project/
│
├── func.py
│
└── index.py
```

## **2. func.py — Saare custom functions**

```py

# ATM SYSTEM FUNCTIONS

balance = 10000
pin = 1234


# Show ATM Menu
def show_menu():
    print("\n========== ATM SYSTEM ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("================================")


# Verify ATM PIN
def verify_pin(user_pin):
    if user_pin == pin:
        return True
    else:
        return False


# Check Balance
def check_balance():
    print("\nYour Current Balance:", balance)


# Deposit Money
def deposit(amount):
    global balance

    if amount > 0:
        balance += amount

        print("\nDeposit Successful!")
        print("Deposited Amount:", amount)
        print("Available Balance:", balance)

    else:
        print("\nInvalid Deposit Amount!")


# Withdraw Money
def withdraw(amount):
    global balance

    if amount <= 0:
        print("\nInvalid Withdrawal Amount!")

    elif amount > balance:
        print("\nInsufficient Balance!")

    else:
        balance -= amount

        print("\nWithdrawal Successful!")
        print("Withdrawn Amount:", amount)
        print("Remaining Balance:", balance)


# Exit ATM
def exit_atm():
    print("\nThank You For Using Our ATM!")
    print("Have A Nice Day!")

```

## **3. index.py — Functions import karke use karo**

```py

# IMPORT ATM FUNCTIONS

import func


print("================================")
print("     WELCOME TO ATM SYSTEM")
print("================================")


# PIN Verification
user_pin = int(input("\nEnter Your ATM PIN: "))


if func.verify_pin(user_pin):

    print("\nPIN Verified Successfully!")

    # Show Menu
    func.show_menu()

    # Get User Choice
    choice = int(input("\nSelect Your Option: "))


    # Check Balance
    if choice == 1:

        func.check_balance()


    # Deposit Money
    elif choice == 2:

        amount = float(input("\nEnter Deposit Amount: "))

        func.deposit(amount)


    # Withdraw Money
    elif choice == 3:

        amount = float(input("\nEnter Withdrawal Amount: "))

        func.withdraw(amount)


    # Exit ATM
    elif choice == 4:

        func.exit_atm()


    # Invalid Choice
    else:

        print("\nInvalid Option Selected!")


else:

    print("\nIncorrect PIN!")
    print("Access Denied!")

```

## **4. Program run kaise karna hai?**

Terminal mein ye command run karo:

```
python index.py
```
