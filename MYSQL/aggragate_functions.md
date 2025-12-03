# MySQL Aggregate Functions

Aggregate functions ka use multiple rows ke data ko **summarize** karne ke liye hota hai.

---

## 1. COUNT()

* **Purpose:** Rows ki **count** nikalne ke liye

```sql
SELECT COUNT(column_name) FROM table_name;
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
