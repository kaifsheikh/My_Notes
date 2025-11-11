# What is Model?
1. Model ek Python class hoti hai jime hum likhte hain kaunse fields (columns) honge aur unka data type kya hoga
   
2. Model decide karta hai ke database mein kya information store karne hai jaise (name, age, email) aur Data kis Type ka hoga jaise (text, number, email)
   
3. Model Django ka wo part hai jo database ke table ko represent/Describe karta hai ka oisme kitne Column hongay or Datatype kia hoge.

# What is Schema?
1. Jab tum ye model save (migrate) karte ho,
2. to Django database ke andar ek table bana deta hai.
3. Wo table ka structure (columns + Datatype) ko he Schema bolte hai.

# What is Migration?
1. Matlab, Model ne abhi tak sirf ye bataya hai ke humein ek table create karna hai jisme 3 columns honge aur unke data types alag honge. Jab hum is table ko database mein actual create karna chahte hain, to hum is Model ka Migration banate hain, jisse Django ko instructions milti hain ke table kaise create karna hai, aur phir Migrate command run karke ye table database mein actually create ho jata hai.

1. Migration Django ka ek system hai jo aapke Models (Python code) ko database ke tables mein convert karta hai.
2. Migration sirf instructions hai

# What is Migrate?

1. Migrate Django ka command hai jo actually database me changes apply karta hai.
2. Migrate ka use karke table database me create hota hai.

# `Commands for Migrate:`

```cmd
1. python manage.py migrate
2. python manage.py createsuperuser
```
