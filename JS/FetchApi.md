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

console.log(products[0].id) // Output : 0
console.log(products[1].name) // Output : Shoes
```

---

## 🔹 JSON (JavaScript Object Notation)

* JSON ek **data format** hai jo data ko store aur exchange karne ke liye use hota hai.
* Ye **object jaisa lagta hai**, lekin ye **string format** hota hai.
* 90% web APIs data JSON format mein bhejti/leti hain.

Example JSON:

```json
let person = {
    "name": "Kaif",
    "age": 22,
    "skills": ["HTML", "CSS", "JavaScript"], // yeah Array hai
    "address": {        // Yeah Object hai
      "city": "Lahore",
      "zip": "54000"
    }
}

console.log(person.name);           // Kaif
console.log(person.age);            // 22
console.log(person.skills[0]);      // HTML
console.log(person.skills[2]);      // JavaScript
console.log(person.address.city);   // Lahore
console.log(person.address.zip);    // 54000

```

---

## 🔹 API (Application Programming Interface)

1. API ek **bridge** hai jo do applications ke beech data exchange karata hai.
2. Tum directly server ke andar nahi ja sakte, isliye API middleman ki tarah kaam karta hai.
3. API ek messenger hai jo data ek jagah se doosri jagah le jaata hai —
taake different software aapas me baat kar sakein

## API Purpose:
1. Data Exchange - Website aur server ke beech data lena–dena
2. Communication - Different applications ek doosre se baat kar sakein

### Example (Restaurant Analogy):

1. Tum (Customer) menu se khana order karte ho.
2. Waiter (API) order ko Kitchen (Server) tak le jaata hai.
3. Kitchen order banata hai.
4. Waiter (API) khana wapas tum tak laata hai.
5. Tumhara kaam ho gaya bina kitchen mein ghuse.

---

# Fetch() Method:
1. fetch() JavaScript ka ek method (function) hai jo kisi server ya API se data lene (ya bhejne) ke kaam aata hai.
2. yeah Promise return karta hai.
3. ager data mil jata hai tu .then() method use hota hai
4. or ager nahe mila tu catch() method use hota hai

## Example 01:
```js
 let URL = fetch("https://jsonplaceholder.typicode.com/posts");

        URL.then(function(result){
            let a = result.json(); // Data ko Json() mein convert karta hai
            return a; // ois Json Data ko agauy return karta hai
        })

        .then(function(response){
            console.log(response) // yeah ois Data ko Display karta hai
        })

        .catch(function(error){
            console.log("Error: " , error); // ager koi Error ho tu oisa Handle karta hai
        })
```
## Example 02

```js
 <div id="dataUser"></div>

<script>
        let URL = fetch("https://jsonplaceholder.typicode.com/posts");

        URL.then(function(result){
            let a = result.json(); 
            return a;
        })

        .then(function(response){
            console.log(response);
            let container = document.getElementById('dataUser');

            response.forEach(function (user){
                container.innerHTML += `
                    <div>
                         <h3>${user.title}</h3>
                        <p>Email: ${user.body}</p>
                        <hr>
                    </div>
                `
            });
        })

        .catch(function(error){
            console.log("Error: " , error);
        })
</script>
```

## New Api Fetch Project:

```
1. https://newsapi.org/

2. https://newsapi.org/v2/everything?q=tesla&from=2025-09-06&sortBy=publishedAt&apiKey=b8d291e010374213b1c3d1e6ac920833

```
## Code

```html
 <div id="news"></div>

<script>
      let Api = fetch(
        "https://newsapi.org/v2/everything?q=tesla&from=2025-09-06&sortBy=publishedAt&apiKey=b8d291e010374213b1c3d1e6ac920833"
      );

      Api.then(function (result) {
        let a = result.json();
        return a;
      })
      .then(function (response) {
        // Actual data response mein hai json format mein
        console.log(response);

        let data = document.getElementById("news"); // Get id

        response.articles.forEach(function (news) {
          // forEach loop run kiya or articles mein wo sara data hai
          data.innerHTML += `
                <div>
                  <h3>${news.title}</h3>
                  <p>${news.description}</p>
                  <p>${news.author}</p>
                  <img src="${news.urlToImage}" width="300">
                  <hr>
              </div>`;
        });
      });
</script>
```
