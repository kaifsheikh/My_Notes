## What is Context Processor?
1. Context processor ek function hota hai jo har request par automatically run hota hai aur jo data return karta hai, wo har template ke liye available hota hai.

# What is `superuser` , `is_staff` & `is_active`:
## is_staff
1. Yeh field hume permission dyte hai ke user Django ka Default Admin Panel mein enter ho sakta hai ya nahi.
2. Agar `True` hai User admin site mein login kar sakta hai.
3. Agar `False` hai tu user sirf website ke front-end ko use kar sakega, admin panel ko nahi dekh sakta.

## is_superuser
1. Yeh field `PermissionsMixin` Class se aati hai aur yeh sab se zyada powerful hai.
2. Jis user ka `is_superuser = True` ho, usay kisi alag permission ki zaroorat nahi hoti. Woh database mein kuch bhi dekh sakta hai, badal sakta hai ya delete kar sakta hai.

## is_active
1. Yeh field aik Boolean (True/False) hoti hai jo batati hai ke user ka account filhal chalu hai ya nahi.
