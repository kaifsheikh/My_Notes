# MySQL Important Datatypes (Easy Words)

## TEXT / STRING TYPES

| Datatype      | Min | Max        | Easy Meaning              | Practical Example                     |
|---------------|-----|------------|---------------------------|---------------------------------------|
| CHAR(n)       | 1   | 255        | Fixed length text         | country_code CHAR(3)                  |
| VARCHAR(n)    | 1   | 65535      | Short variable text       | name VARCHAR(100)                     |
| TEXT          | -   | 65535      | Paragraph text            | description TEXT                      |
| MEDIUMTEXT    | -   | 16,777,215 | Long article text         | content MEDIUMTEXT                    |
| LONGTEXT      | -   | 4 Billion  | Very long text (book)     | full_book LONGTEXT                    |


## NUMBER TYPES

| Datatype      | Range / Limit                     | Easy Meaning          | Practical Example           |
|---------------|-----------------------------------|------------------------|-----------------------------|
| INT           | -2B to +2B                        | Normal number         | id INT                      |
| BIGINT        | Very very large number            | Huge number           | views BIGINT                |
| DECIMAL(M,N)  | Depends on M,N                    | Exact decimal number  | price DECIMAL(10,2)         |
| FLOAT         | Approx decimal                    | Decimal (not exact)   | rating FLOAT                |
| DOUBLE        | Bigger approx decimal             | More precise float    | weight DOUBLE               |


## DATE / TIME TYPES

| Datatype  | Easy Meaning               | Practical Example                         |
|-----------|-----------------------------|---------------------------------------------|
| DATE      | Only date                   | birth_date DATE                             |
| TIME      | Only time                   | login_time TIME                             |
| DATETIME  | Date + time                 | created_at DATETIME                         |
| TIMESTAMP | Auto date + time            | updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP |


## LOGICAL & SPECIAL TYPES

| Datatype        | Easy Meaning         | Practical Example                         |
|-----------------|-----------------------|-------------------------------------------|
| BOOLEAN         | True/False (0/1)      | is_active BOOLEAN                          |
| ENUM            | Fixed choices         | status ENUM('Active', 'Pending', 'Banned') |
| JSON            | Store JSON data       | settings JSON                              |
| BLOB            | Binary data (files)   | image BLOB                                 |


# Example Table (Using These Datatypes)

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_code CHAR(3)
    bio TEXT,
    content MEDIUMTEXT,
    full_book LONGTEXT,
    views BIGINT,
    price DECIMAL(10,2),
    rating FLOAT,
    name VARCHAR(100),
    birth_date DATE,
    login_time TIME,
    created_at DATETIME,
    email VARCHAR(255),
    price DECIMAL(10,2),
    is_active BOOLEAN,
    status ENUM('Active', 'Pending', 'Banned'),
    created_at DATETIME,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
