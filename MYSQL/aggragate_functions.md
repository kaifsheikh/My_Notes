# MySQL Aggregate Functions

Aggregate functions ka use multiple rows ke data ko **summarize** karne ke liye hota hai.

---

## 1. COUNT()

- Rows ko **count** karta hai 

```sql
SELECT COUNT(column_name) FROM table_name;
SELECT COUNT(*) AS Total_Rows FROM table_name;
```
---

## 2. SUM()

* **Purpose:** Numeric column ka **total sum** nikalta hai

```sql
SELECT SUM(column_name) FROM table_name;
```
---

## 3. AVG()

* **Purpose:** Numeric column ka **average** nikalta hai
  
```sql
SELECT AVG(column_name) FROM table_name;
```
---

## 4. MIN()

* **Purpose:** Column ka **minimum value** nikalta hai
  
```sql
SELECT MIN(column_name) FROM table_name;
```
---

## 5. MAX()

* **Purpose:** Column ka **maximum value** nikalta hai

```sql
SELECT MAX(column_name) FROM table_name;
```
---

## 5. GROUP BY()

* **Purpose:** GROUP BY clause ka Purpose hai table ki rows (data ki lines) ko chote groups mein jama (collect) karna hai, taake hum un groups par Aggregate Functions (jaise SUM(), AVG(), COUNT()) laga saken.

```sql
-- Sample table code (MySQL)

CREATE TABLE Sales_Data (
    Order_ID INT PRIMARY KEY,
    Product_Name VARCHAR(100),
    City VARCHAR(50),
    Sale_Amount DECIMAL(10, 2),
    Quantity INT
);

-- Sample Insert code

INSERT INTO Sales_Data (Order_ID, Product_Name, City, Sale_Amount, Quantity) VALUES
(1, 'Laptop', 'Karachi', 1200.00, 1),
(2, 'Mouse', 'Lahore', 25.00, 5),
(3, 'Laptop', 'Karachi', 1500.00, 1),
(4, 'Keyboard', 'Islamabad', 75.00, 3),
(5, 'Mouse', 'Karachi', 20.00, 4),
(6, 'Keyboard', 'Lahore', 80.00, 2),
(7, 'Monitor', 'Islamabad', 300.00, 1);
```

## Example:

```sql
SELECT City, SUM(Sale_Amount) AS Total_Revenue 
FROM  Sales_Data
GROUP BY City;
```
---


## 6. GROUP_CONCAT()

* **Purpose:** Multiple rows ko **single string** mein combine karta hai

```sql
SELECT GROUP_CONCAT(column_name) FROM table_name;
```
---

## 7. STD() / STDDEV()

* **Purpose:** Standard deviation calculate karne ke liye

```sql
SELECT STD(column_name) FROM table_name;
```
---

## 8. VARIANCE()

* **Purpose:** Column ka variance calculate karta hai

```sql
SELECT VARIANCE(column_name) FROM table_name;
```
---

### **Tips:**

* Aggregate functions ke saath `GROUP BY` clause ka use hota hai to summarize per group:

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```



1.	What is the total number of employees?
2.	What is the average salary of all employees?
3.	What is the maximum salary in the company?
4.	What is the minimum salary in the company?
5.	What is the total salary of IT depart employees?
6.	What is the total number of employees under the age of 35?
7.	What is the maximum age of employees?
8.	What is the minimum age of employees?
9.	How many employees were hired before the year 2020?
10.	What is the total salary of employees in the IT department? 
11.	What is the average salary of employees under the age of 30?
12.	What is the highest salary of employees over the age of 40?
13.	How many distinct departments are there?
14.	How many employees have a salary above the company average?
15.	Which employees are earning the highest salary?
16.	What is the total salary paid to employees hired in the year 2023?
17.	How many employees have the minimum age in the company?
18.	What is the average salary of employees in the HR department?
19.	Which department has the highest paid employee?
20.	Which employees were hired most recently?


```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    age INT NOT NULL,
    hire_date DATE NOT NULL
);


INSERT INTO employees (emp_name, department, salary, age, hire_date) VALUES
('Ali Khan', 'IT', 85000, 28, '2021-03-15'),
('Ahmed Raza', 'HR', 60000, 35, '2019-07-20'),
('Sara Malik', 'IT', 95000, 42, '2020-01-10'),
('Ayesha Noor', 'Finance', 78000, 30, '2023-05-01'),
('Usman Ali', 'HR', 50000, 25, '2023-08-12'),
('Bilal Hussain', 'IT', 72000, 32, '2018-11-25'),
('Hina Shah', 'Marketing', 65000, 29, '2022-06-18'),
('Kamran Akram', 'Finance', 88000, 45, '2017-02-09'),
('Zain Ahmed', 'IT', 100000, 40, '2016-09-30'),
('Nida Fatima', 'HR', 55000, 27, '2020-12-05'),
('Fahad Khan', 'Marketing', 70000, 34, '2019-04-22'),
('Maryam Iqbal', 'Finance', 82000, 31, '2021-10-14'),
('Imran Sheikh', 'IT', 92000, 38, '2022-01-19'),
('Sana Javed', 'HR', 58000, 26, '2023-02-11'),
('Omer Farooq', 'IT', 110000, 44, '2015-06-08');

```