
## 🔹 Joins

**JOIN ka matlab hai do ya do se zyada tables ko aapas mein jorna (connect karna) taake hum un tables ka data ek saath dekh sakein.**

## Foreign Key

**Foreign Key (FK) woh key hai jo do tables ko aapas mein jorti hai. Yeh woh "bridge" hai jo JOINs mein istemaal hota hai.**    

## Types:

1. INNER JOIN → Sirf matching data dikhata hai
2. LEFT JOIN → Left table ka sara data + matching right table ka data
3. RIGHT JOIN → Right table ka sara data + matching left table ka data
4. CROSS JOIN → Har record ko dusre table ke har record se milata hai

Example:

```sql
SELECT students.student_id, students.name, classes.class_name
FROM students
INNER JOIN classes
ON students.class_id = classes.class_id;
```

---

## 🔹 Primary Key (PK)

1. Har table mein sirf **1 Primary Key** hoti hai
2. NULL values allowed nahi hoti
3. Values unique hoti hain
4. FOREIGN KEY, PK ke sath connect hoti hai
5. Usually AUTO_INCREMENT hota hai

---
