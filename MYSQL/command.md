# 📘 MySQL Commands Cheat Sheet
---

## 🔹 Database Commands

1. **Create Database**

   ```sql
   CREATE DATABASE db_name;
   ```

   → Naya database banane ke liye.

2. **Drop Database**

   ```sql
   DROP DATABASE db_name;
   ```

   → Database delete karne ke liye.

---

## 🔹 Table Commands

1. **Create Table**

   ```sql
   CREATE TABLE users(
       id INT,
       name VARCHAR(100),
       age INT,
       city VARCHAR(50)
   );
   ```

   → Ek nayi table banata hai jisme columns define hote hain.

2. **Describe Table**

   ```sql
   DESCRIBE users;
   ```

   → Table ke columns aur unke datatypes dikhata hai.

3. **Drop Table**

   ```sql
   DROP TABLE users;
   ```

   → Table poori ki poori delete ho jaati hai.

---

## 🔹 Insert Data

```sql
INSERT INTO users (name, age, city)
VALUES 
('Sara Ahmed', 25, 'Lahore'),
('Usman Raza', 22, 'Islamabad'),
('Hina Sheikh', 24, 'Multan');
```

→ Multiple rows ek sath insert karne ke liye.

---

## 🔹 Alter Table (Modify Columns)

1. **Add New Column**

   ```sql
   ALTER TABLE users ADD email VARCHAR(100);
   ```

   → Naya column add karne ke liye.

2. **Add Column After Specific Column**

   ```sql
   ALTER TABLE users ADD gender VARCHAR(10) AFTER name;
   ```

3. **Modify Column Datatype**

   ```sql
   ALTER TABLE users MODIFY age BIGINT;
   ```

4. **Change Column Name + Datatype**

   ```sql
   ALTER TABLE users CHANGE old_name new_name VARCHAR(50);
   ```

5. **Sirf Column Name Change Karna**

   ```sql
   ALTER TABLE users CHANGE old_name new_name VARCHAR(100);
   ```

6. **Drop Column**

   ```sql
   ALTER TABLE users DROP COLUMN age;
   ```

   → Table ke andar se ek column hataane ke liye.

---

## 🔹 Constraints (Rules for Data)

* **NOT NULL** → Value empty nahi ho sakti
* **UNIQUE** → Har value alag honi chahiye
* **DEFAULT** → Agar value na di jaye to default value set ho jaaye
* **CHECK** → Condition lagane ke liye
* **PRIMARY KEY** → Har row ki unique pehchan
* **FOREIGN KEY** → Do tables ko connect karne ke liye

Example:

```sql
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(100) DEFAULT 'Hyderabad',
    gender ENUM('Male','Female')
);
```

---

## 🔹 Update Data

1. **Single Update**

   ```sql
   UPDATE users
   SET name = 'Ali Raza'
   WHERE id = 2;
   ```

2. **Update Multiple Rows with CASE**

   ```sql
   UPDATE users
   SET city = CASE id
       WHEN 1 THEN 'Karachi'
       WHEN 2 THEN 'Lahore'
       WHEN 3 THEN 'Islamabad'
       WHEN 4 THEN 'Faisalabad'
       WHEN 5 THEN 'Rawalpindi'
       WHEN 6 THEN 'Peshawar'
       WHEN 7 THEN 'Quetta'
       WHEN 8 THEN 'Multan'
       WHEN 9 THEN 'Sialkot'
       WHEN 10 THEN 'Hyderabad'
   END
   WHERE id IN (1,2,3,4,5,6,7,8,9,10);
   ```

   → Multiple records ek hi query mein update karne ke liye.

---

## 🔹 Delete Data

1. **Delete Record**

   ```sql
   DELETE FROM users WHERE id = 1;
   ```

2. **Delete Rows by Condition**

   ```sql
   DELETE FROM users WHERE city = 'Lahore';
   ```

---

## 🔹 Select Data

1. **All Data**

   ```sql
   SELECT * FROM users;
   ```

2. **Specific Column**

   ```sql
   SELECT name, city FROM users;
   ```

3. **WHERE Clause**

   ```sql
   SELECT * FROM users WHERE age > 20;
   ```

4. **AND / OR / IN**

   ```sql
   SELECT * FROM users WHERE city = 'Lahore' OR city = 'Karachi';
   SELECT * FROM users WHERE city IN ('Lahore','Karachi','Multan');
   ```

5. **BETWEEN**

   ```sql
   SELECT * FROM users WHERE age BETWEEN 20 AND 30;
   ```

6. **NOT BETWEEN**

   ```sql
   SELECT * FROM users WHERE id NOT BETWEEN 5 AND 10;
   ```

7. **LIKE (Pattern Matching)**

   ```sql
   SELECT * FROM users WHERE name LIKE 'A%';   -- Start A se
   SELECT * FROM users WHERE name LIKE '%a';   -- End a se
   SELECT * FROM users WHERE name LIKE '%am%'; -- Beech mein "am"
   SELECT * FROM users WHERE name LIKE 'a%i';  -- Start a, end i
   ```

8. **Sorting**

   ```sql
   SELECT * FROM users ORDER BY name ASC;
   SELECT * FROM users ORDER BY age DESC;
   ```

9. **DISTINCT (Unique Values)**

   ```sql
   SELECT DISTINCT city FROM users;
   ```

---

## 🔹 Joins

**JOIN ka matlab hota hai tables ko jorna.**

Types:

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
