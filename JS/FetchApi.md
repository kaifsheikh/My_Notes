# 🗂️ Objects, Arrays, JSON aur APIs Cheat Sheet

Yeh document basic JavaScript aur Web concepts ko simple **Roman Urdu** mein explain karta hai.

---

## 🔹 Object

Object ek aisi cheez hai jisme data **key-value pairs** ki form mein store hota hai.

```js
let person = {
  name: "Kaif",
  age: 22,
  city: "Lahore"
};
```

---

## 🔹 Nested Object

Object ke andar ek aur object ho, to usko **nested object** kehte hain.

```js
let user = {
  name: "Kaif",
  address: {
    city: "Lahore",
    zip: "54000"
  }
};
```

---

## 🔹 Array

Array ek list hoti hai jisme multiple values ek sath rakhi jaati hain.

```js
let fruits = ["apple", "banana", "mango"];
```

---

## 🔹 Nested Array

Array ke andar ek aur array ho, to usko **nested array** kehte hain.

```js
let numbers = [1, 2, [3, 4], 5];
```

---

## 🔹 Array inside Object

Object ke andar ek array rakha jaa sakta hai.

```js
let products = [
  { id: 1, name: "Shirt" },
  { id: 2, name: "Shoes" }
];
```

---

## 🔹 JSON (JavaScript Object Notation)

* JSON ek **data format** hai jo data ko store aur exchange karne ke liye use hota hai.
* Ye **object jaisa lagta hai**, lekin ye **string format** hota hai.
* 90% web APIs data JSON format mein bhejti/leti hain.

Example JSON:

```json
{
  "name": "Kaif",
  "age": 22,
  "skills": ["HTML", "CSS", "JavaScript"],
  "address": {
    "city": "Lahore",
    "zip": "54000"
  }
}
```

---

## 🔹 API (Application Programming Interface)

* API ek **bridge** hai jo do applications ke beech data exchange karata hai.
* Tum directly server ke andar nahi ja sakte, isliye API middleman ki tarah kaam karta hai.

### Example (Restaurant Analogy):

1. Tum (Customer) menu se khana order karte ho.
2. Waiter (API) order ko Kitchen (Server) tak le jaata hai.
3. Kitchen order banata hai.
4. Waiter (API) khana wapas tum tak laata hai.
5. Tumhara kaam ho gaya bina kitchen mein ghuse.

---

✅ Ab tumhe Objects, Arrays, JSON aur APIs ekdum easy tareeke se samajh aa gaya hoga.
