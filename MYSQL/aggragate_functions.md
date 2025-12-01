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
