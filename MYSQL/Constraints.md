# What is Constraints?
1. Constraints rules hote hain jo database table ke columns par lagaye jate hain, taki data correct aur consistent rahe.

## Type of Constraints (Rules for Data)

* **PRIMARY KEY** → Har row ki unique pehchan
* **AUTO_INCREMENT** → ID **apne aap 1,2,3…** badhe
* **NOT NULL** → Value empty nahi ho sakti
* **UNIQUE** → Har value alag honi chahiye
* **DEFAULT** → Agar value na di jaye to default value set ho jaaye
* **CHECK** → Condition lagane ke liye
* **FOREIGN KEY** → Do tables ko connect karne ke liye                                               |

# Example 01:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID automatically
    name VARCHAR(100) NOT NULL,             -- Name required
    email VARCHAR(255) UNIQUE NOT NULL,     -- Email unique & required
    status ENUM('Active','Pending') DEFAULT 'Pending', -- Default value
    age INT CHECK(age >= 18)                -- Age must be 18 or more
);
```
