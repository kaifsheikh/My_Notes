
## 🔹 Joins

**JOIN ka matlab hai do ya do se zyada tables ko aapas mein jorna (connect karna) taake hum un tables ka data ek saath dekh sakein.**

## Foreign Key
1. **Foreign Key (FK) woh key hai jo do tables ko aapas mein jorti hai.
2. Yeh woh "bridge" hai jo JOINs mein istemaal hota hai.**    

## Example:
- Table Name - `Classes`
- Yeh asal list hai, jisme bataya gaya ke kon kon si classes exist karti hain:

| id | classes    |
| -- | ---------- |
| 1  | Class 6    |
| 2  | Class 7    |


- Table Name - `Students`
- Yeh students ki list hai

| name  | student_class |                                                      
| ----- | --------      | 
| Ali   | 1             |
| Sara  | 2             |
| Hamza | 5             |

***Note***<br>
- `Students` table mein jo column hai `student_class` isme sirf wahi number ho sakta hai
- jo `Classes` table ke `id` wala column me already Exist karta ho.
- tu isme Hamza ki class show nahe hoge kue ka wo classes table mein exist he nahe karti hai
## Types:

1. `INNER JOIN` → Sirf matching data dikhata hai
2. `LEFT JOIN` → Left table ka sara data + matching right table ka data
3. `RIGHT JOIN` → Right table ka sara data + matching left table ka data
4. `CROSS JOIN` → Har record ko dusre table ke har record se milata hai

---

# Inner Join:
- 

## 🔹 Primary Key (PK)

1. Har table mein sirf **1 Primary Key** hoti hai
2. NULL values allowed nahi hoti
3. Values unique hoti hain
4. FOREIGN KEY, PK ke sath connect hoti hai
5. Usually AUTO_INCREMENT hota hai

---
