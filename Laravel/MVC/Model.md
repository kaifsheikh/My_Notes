1. Model ka kam sirf `Database` ki `table` mein Store `Data` ko Manage karne ka hai.
2. Model ke zariye hum table mein mojod Data ka saath `CRUD` Operations perform karwa sekhte hai without writing SQL Model ka kam sirf `Create` `Read` `Update` or `Delete` karne ka hai bs.
5. Har table ke liye usually ek `Model` banta hai
3. Model aik Normal PHP Class hoti hai iski files `app/Models/` folder mein hoti hai.
4. Laravel ka Model [Eloquent](../orm.md) ORM ka part hai

## Difference Between:
| Language & Framework | Table | Each Rows | Each Columns | SQL & ORM |
| :--- | :--- | :--- | :--- | :--- |
| **MYSQL** | user | Rows | Columns | SQL Query `SELECT * FROM users` | 
| **Laravel** | Users `Model` | Objects | Properties | ORM `User::all()` |

# What is ORM?
1. `ORM` = Object-Relational Mapping
2. ORM aik translator ki terha kam karta hai jo `PHP` ka code ko `Database` ki (SQL) Language mein badal deta hai means.
3. ORM mein hum PHP code likhte hain aur ORM usay background mein SQL query bana kar database ko bhej deta hai
3. **Purpose:** SQL query manually likhne ki zarurat nahe hoti

## Example:
1. hum `PHP` code likhte hai kch is terha se.

```php
User::where('age', '>', 18)->get();
```

2. ORM Background mein oisa `SQL` ki Query bana dyta hai kch is terha sa.

```sql
SELECT * FROM users WHERE age > 18;
```