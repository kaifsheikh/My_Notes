# What is Mongo DB?
MongoDB ek database hai — jisme hum apna data store karte hain. Lekin ye NoSQL Database hai.

# What is NoSQL?
"NoSQL" ka matlab hota hai: Not Only SQL.
Yani aise database jo tables, rows, columns ki form mein data store karte hai oisa hum Relation Database bolte hai.
or jo Document or JSON ki format mein store karte hai oisa hum NoSQL bolte hai.
MongoDB mein data JSON (JavaScript Object Notation) jaisa format mein store hota hai jisa BSON bolte hai.
```js
{
  "name": "Kaif",
  "age": 22,
  "city": "Karachi"
}
```
Isko hum document bolte hain.
Or yeah JSON data jis file mein save hota hai oisa hum Collection bolte hai.
Tu collection ka andar humera pass Document yeah phir Multiple Document ho sekhte hai

## Example:
 
1. MYSQL -> Database , Table , Rows
2. Mongo DB -> Database . Collection , Document

Commands	Describe
Use Database_Name	Yeah database create karti hai or create karne ka bad oisme switch bhe kar jaati hai or ager database already exists hoga tu oisme switch kar jayge
Show dbs	Yeah saray database show karti hai
Db.createCollection("collection_name")	
    
