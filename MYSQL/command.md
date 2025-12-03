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

3. **Table Delete karne ka liye**

   ```sql
   DROP TABLE users;
   ```
---

🔹 **Multiple rows ek sath insert karne ke liye.**

```sql
INSERT INTO users (name, age, city)
VALUES 
('Sara Ahmed', 25, 'Lahore'),
('Usman Raza', 22, 'Islamabad'),
('Hina Sheikh', 24, 'Multan');
```

---

## 🔹 Alter Table (Modify Columns)

1. **Single Column Add karne ka liye**

   ```sql
   ALTER TABLE users ADD email VARCHAR(100);
   ```
   
1. **Multiple New Columns add karne ke liye.**

   ```sql
   ALTER TABLE users ADD (email VARCHAR(100) , age INT);
   ```

2. **Add Column After Specific Column**

   ```sql
   ALTER TABLE users ADD gender VARCHAR(10) AFTER name;
   ```

3. **Modify Column Datatype Only**

   ```sql
   ALTER TABLE users MODIFY age BIGINT;
   ```

4. **Change Column Name + Datatype**

   ```sql
   ALTER TABLE users CHANGE old_name new_name VARCHAR(50);
   ```

5. **Sirf Column Name Change Karna**

   ```sql
   ALTER TABLE users CHANGE old_column_name new_column_name VARCHAR(100);
   ```

6. **Table ke Columns ko Delete karne ka liye**

   ```sql
   ALTER TABLE users DROP COLUMN age;
   ```

7. **Table ke Naam change karne ka liya.**

   ```sql
   ALTER TABLE Old_table_Name RENAME TO New_table_Name;
   ```

8. **Column mein Default Value Set karne ka liya.**

   ```sql
   ALTER TABLE table_name
   ALTER COLUMN column_name SET DEFAULT default_value;
   
   ALTER TABLE users
   ALTER COLUMN city SET DEFAULT "Hyd";

   ```
   **Existing Default Value ko Remove karne ka liya**
   ```sql
   ALTER TABLE users
   ALTER COLUMN city DROP DEFAULT;
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

3. **WHERE Clause Sirf 20 se Greater Age Show Hoge**

   ```sql
   SELECT * FROM users WHERE age > 20;
   SELECT * FROM users WHERE city > "Hyd";
   ```

5. **IS NULL (Ye check karne ke liye hota hai ki column empty hai ya nahi)**

   ```sql
   SELECT * FROM table_name WHERE Gender is NULL;
   SELECT Column_Name FROM tabl_name WHERE Gender is NULL;
   ```
   
   **Jo students ka address empty hai, wo show honge.**
   ```sql
   SELECT * FROM Table_Name WHERE address IS NOT NULL;
   ```
   
4. **AND / OR / IN**

   ```sql
   SELECT * FROM users WHERE city = 'Lahore' OR Age >= 20;
   
   SELECT * FROM users
   WHERE age < 25 OR age > 28;

   SELECT * FROM users
   WHERE age < 25 OR age = 28 OR city = 'Islamabad' OR name = 'Sara';

   SELECT * FROM users
   WHERE age > 24 AND city = 'Karachi';

   SELECT * FROM users WHERE city IN ('Lahore','Karachi','Multan');

   SELECT * FROM users WHERE Age IN (20 , 25 , 26);
   ```

5. **BETWEEN**

   ```sql
   SELECT * FROM users WHERE age BETWEEN 20 AND 30;

   SELECT * FROM users WHERE age BETWEEN 20 AND 30 AND City = "Hyderabad";

   SELECT * FROM users WHERE age BETWEEN 20 AND 30 OR City = "Hyderabad";
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

9. **Ye duplicate data remove kar deta hai, sirf unique values show karta hai.**

   ```sql
   1. SELECT DISTINCT column_name FROM table_name;
   2. SELECT DISTINCT column_name , column_name FROM table_name;
   3. SELECT DISTINCT * FROM table_name;
   4. SELECT DISTINCT * FROM table_name ORDER BY Name ASC
   5. SELECT COUNT(DISTINCT city) FROM users;
   6. SELECT COUNT(DISTINCT c_name) FROM table_name
   7. SELECT COUNT(DISTINCT c_name , c_name) FROM users;

   ```

9. **Column Alias means Column ko temporary naam dena**

   ```sql
   1. SELECT First_Name AS Name FROM users
   2. SELECT First_Name Name FROM users
   3. SELECT First_Name AS fname , Phone_Number AS Contact FROM users
   ```

---
