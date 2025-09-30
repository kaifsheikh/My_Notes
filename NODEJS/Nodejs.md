# What is Schema?
Schema = Data ka blueprint
jab hum database ko batate ha ke ek document kaisa dikhna chahiye.
Kaunse fields honge aur unka type kya hoga.
Jaise ghar banane se pehle map banta hai, waise hi schema hota hai.

jis terha se MYSQL mein hum Tabkle bolte hai oisa hum MonogDB mein Collection bolte hai.

## Kia har Collection ka alag Schema banana pherta hai?
Haan, har collection ke liye alag schema banana padta hai.
Har collection ka data alag hoga.

## kia yeah zarori hai ka her Schema ko alag file mein create karna chaiya 

Nahi! Yeh zaroori nahi hai ke har schema ko alag file me banao.
Tum chaho to saare schemas ek hi file me bana sakte ho.

## Example:

users collection → name, email, password
products collection → title, price, description
orders collection → orderId, userId, total
In teeno collections ka structure different hai, isliye har ek ka alag schema banana padta hai.

```js
const mongoose = require('mongoose'); // Require Mongoose 

// User schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String
});
const User = mongoose.model('User', userSchema);

// Product schema
const productSchema = new mongoose.Schema({
  title: String,
  price: Number
});
const Product = mongoose.model('Product', productSchema);

// Export sabko
module.exports = { User, Product };
```
# What is Model?

Model = ek class jo database collection ke saath kaam karti hai. <br>
Ye Schema ke base par banta hai.<br>
Har model ek collection ko represent karta hai (users, products, orders, etc.).<br>
Model ke through hi tum database me CRUD (Create, Read, Update, Delete) karte ho.<br>
Model ek "tool" hai jo tumhe DB ke saath interact karne deta hai.<br>

## Example:
```js
// Step 1: Schema banao
const userSchema = new mongoose.Schema({ // Schema name -> userSchema
  name: String,
  email: String,
  age: Number
});

// Step 2: Model banao
const User = mongoose.model("User", userSchema);

// Ab User ek model hai jo users collection ko represent karega.
```