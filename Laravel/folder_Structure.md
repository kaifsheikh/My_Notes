# What is Package , Libaray , Dependency  oor DevDependency:
1. Package aik tayyar shuda code ka "dibba" hota hai jo kisi makhsoos kaam (specific task) ke liye banaya gaya ho. Aapko wo code khud likhne ki zaroorat nahi parti.

2. Library functions ya classes ka aik `Collection` hota hai jise aap apni marzi se call karte hain. Har package aik library ho sakta hai, lekin har library package ho ye zaroorat nahi (kuch libraries built-in bhi hoti hain).

3. Jab aapka project kisi bahar ke code (Package) par depend karta hai, toh usay "Dependency" kehte hain. Matlab agar wo package nahi hoga, toh aapka project sahi se kaam nahi karega.

4. Ye wo packages hain jo aapko sirf code likhte waqt, testing karte waqt, ya design banate waqt chahiye hote hain. Jab aapki website live (Production) ho jati hai, toh inki zaroorat nahi rehti.

# app:
1. Ye sab se zaroori folder hai. Aapki application ka Core folder hota hai yeah per `Logics` hoti hai

## `Http/Controllers:`
1. Ye wo "Managers" hain jo decide karte hain ke request kahan jayegi aur kya response dena hai.

## `Models:`
1. Ye database ke saath baat karne ke liye hote hain.

# config:
1. Pore project ki settings yahan hoti hain.

# Resource:
1. Aapki website ka jo bhi "Front-end" ka part hota hai wo yahan rakha jata hai taake browser unhein utha sake:

## CSS:
1. Website ka design/style.

## JS:
1. Interactivity ke liye scripts.

## Images:
1. Logos, banners, aur icons.

# Storage:
1. Is folder ke andar mazeed 3 ahem folders hote hain:

## storage/app
1. Ye wo jagah hai jahan aapki application ki uploaded files rakhi jati hain. Maslan:
2. Users ki upload ki hui Profile Pictures.
3. Invoice ki PDF files.
4. Excel sheets ya koi bhi document jo user upload kare.

## storage/framework
1. Is folder ko Laravel khud use karta hai apni speed aur performance ke liye. Is mein:
2. Cache: Taake website jaldi load ho.
3. Sessions: Ye yaad rakhne ke liye ke kaunsa user login hai.
4. Views: Blade files ko process kar ke jo temporary files banti hain wo yahan hoti hain.
4. Note: Aapko is folder ke andar kabhi kuch manually change nahi karna chahiye.

## storage/logs
1. 

# Package.json:
1. package.json ek configuration file hai jo JavaScript dependencies aur scripts ko manage karti hai
2. Laravel project mein yeh file mostly front-end (JavaScript, CSS, NodeJS, Vue, React, Tailwind) ke liye hoti hai.
3. Ye backend PHP (Laravel) ke liye nahi hoti

# composer.json:
1. Ye file aapki application ki "Requirement List" ya "Fahrist" hai. Is mein aap batate hain ke aapko kaunse packages chahiye aur unka konsa version (version number) hona chahiye.

# composer.lock:
1. Ye file zyada ahem aur "Strict" hoti hai. Is mein un tamam packages ki exact details aur exact version numbers hote hain jo is waqt install ho chuke hain.