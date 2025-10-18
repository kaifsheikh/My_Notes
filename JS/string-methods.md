# Properties

## 1. `lenght`
```js
let name = "Hello";
console.log(name.length) // Output : 5
```

# Methods

## 2. `toUpperCase()`
```js
let name = "Hello";
console.log(name.toUpperCase()) // Output : HELLO
```
## 2. `toLowerCase()`
```js
let name = "HELLO";
console.log(name.toLowerCase()) // Output : hello
```
## 2. `slice(start, end)`
1. JavaScript mein slice() ek method hai jo array ya string ka part (hissa) nikalne ke liye use hota hai — original array ya string ko change nahi karta, bas uska ek new copy (piece) return karta hai.
   
```js
let name = "JavaScript";
let part = name.slice(0, 4);
console.log(part); // Output : Java

// 0 se start kiya,
// 4 tak gaya (4 include nahi hota),
// matlab pehle 4 letters liye.

let name = "JavaScript";
let part = name.slice(0);
console.log(part); // Output : Javascript

// 0 se start kiya,
// or end tak gaya kue ka end index nahe tha
```
## 2. `replace('old_name' , 'naw_name')`

```js
let a = "Hello";
let b = a.replace("Hello" , "Hi");
console.log(b); // Output : Hi
```
## 2. `concat()`

```js
let a = "This is ";
let b = "Sample ";
let c = a.concat(b , "Text")
console.log(c); // Output : This is Sample Text
```
## 2. `trim()`

```js
let a = "        Hello World      ";
console.log(a.trim()) // Output : Hello World

// Ager trim karna ho starting se end se yeah phir center se tu regex use hote hai.
// ab yeah sirf 1 space add karay ga her words mein.

let a = "Hello          World      this    is sample    text";
let result = a.replace(/\s+/g , " ");
console.log(result);
```