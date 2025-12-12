
## 🔹 Joins

**JOIN ka matlab hai do ya do se zyada tables ko aapas mein jorna (connect karna) taake hum un tables ka data ek saath dekh sakein.**

## Foreign Key
1. **Foreign Key (FK) woh key hai jo do tables ko aapas mein jorti hai.
2. Yeh woh "bridge" hai jo JOINs mein istemaal hota hai.**    

```sql
CREATE TABLE departments (
    dep_id INT PRIMARY KEY AUTO_INCREMENT,
    dep_name VARCHAR(50)
);

INSERT INTO departments (dep_name) VALUES
('Computer Science'),
('Business'),
('Physics');

```
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    dep_id INT,
    FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
);

INSERT INTO students (student_name, dep_id) VALUES
('Ali', 1),
('Sara', 2),
('Usman', 3);
```

## AGAR TABLES PEHLE SE BANAYE HUWE HO TO FOREIGN KEY BAAD ME LAGANA
1. `fk_dep` → foreign key ka naam name kch bhe de sekhte hai.

```sql
ALTER TABLE students
ADD CONSTRAINT fk_dep
FOREIGN KEY (dep_id) REFERENCES departments(dep_id);
```
- `ALTER TABLE students` → Students table modify kar rahe hain.
- `ADD CONSTRAINT fk_dep` → Constraint ka naam fk_dep rakha.
- `FOREIGN KEY (dep_id) REFERENCES departments(dep_id)` → Dep_id ko Departments ke dep_id se link kar diya.

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
- INNER JOIN SQL ka ek join hai jo 2 sirf wohi data dikhata hai jo dono tables mein match hota ho.
- Agar koi record match nahi karta → wo result mein nahi aata.

```sql
SELECT Students.name, Classes.classes
FROM Students
INNER JOIN Classes
ON Students.student_class = Classes.id;
```

```sql
-- 1. Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

-- 2. Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- 3. Salaries table
CREATE TABLE salaries (
    emp_id INT PRIMARY KEY,
    salary DECIMAL(10,2),
);

--- Insert Queries

-- Employees
INSERT INTO employees VALUES 
(1, 'Ali', 101),
(2, 'Sara', 102),
(3, 'John', 101);

-- Departments
INSERT INTO departments VALUES
(101, 'IT'),
(102, 'HR');

-- Salaries
INSERT INTO salaries VALUES
(1, 50000),
(2, 60000),
(3, 55000);

--- Inner Join

SELECT e.emp_name, d.dept_name, s.salary
FROM employees e

INNER JOIN departments d
ON e.dept_id = d.dept_id

INNER JOIN salaries s
ON e.emp_id = s.emp_id;

```
