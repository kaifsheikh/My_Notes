# What is Synchronous?

1. Aap ek line mein khade hain. Jab tak aapke aage wala banda apna kaam poora nahi kar leta, aap aage nahi badh sakte. <br>
2. Matlab (Programming Mein): Jab ek function call hota hai, toh code us function ke khatam hone ka intezaar karta hai, tabhi agle line par jata hai. Isse "Blocking" kehte hain. <br> 
3. Matlab: Ek kaam khatam hoga, tabhi doosra shuru hoga. <br>
3. Purpose: Jab kaam bahut chote hote hain ya jab ek step doosre step par poori tarah se nirbhar (depend) karta hai, toh hum synchronous use karte hain. <br>

# What is Asynchronous?

1. Matlab: Kaam shuru karke, uske khatam hone ka intezaar kiye bina, agla kaam shuru kar dena.<br>
2. Fayda: Aap ek hi samay mein kai kaam kar sakte hain. Aapka system freez nahi hoga.<br>
3. Purpose: Asynchronous ka main purpose hai time bachana aur system ko non-stop chalana (Non-Blocking). <br>
4. Isko samajhne ke liye, jab koi kaam zyada time leta hai, toh hum use background mein bhej dete hain aur khud doosra kaam karne lagte hain.

## Async / Await:
1. async function hamesha ek Promise return karta hai. <br>
2. Chahe tum usme normal string, number ya object return karo → woh automatically ek Promise ban jayega. <br>
3. await ka kaam hai: promise ka result ka wait karna.<br>
4. await sirf async function ke andar use ho sakta hai. <br>
5. Tum async function likh sakte ho bina await ke. <br>
6. Lekin tum await tabhi likh sakte ho jab function async ho.

# Example 01 (Without Async and Await)
```js
 let a = 10;
 let b = 20;
 let result = a + b;

function getData(){
    let data = fetch("https://jsonplaceholder.typicode.com/users");
    console.log(data)
}

getData();
console.log(result);

// Promise {<pending>} -> (phela muje Promise return hoga) 
// 30 -> (oiska bad muje result variable ka data milayga)
```
# Example 02 (With Async and Await)
```js
 let a = 10;
 let b = 20;
 let result = a + b;

async function getData(){
    let response = await fetch("https://jsonplaceholder.typicode.com/users");
    let data = await response.json();
    console.log(data);
}

getData();
console.log(result);

// 30 -> (phela muje result variable ka data milayga)
// Promise {<pending>} -> (oiska bad muje Promise return hoga)
```
## Example 03
```js
 function getData(){
        return new Promise(function(resolve , reject){
          
          setTimeout(function(){
            resolve("Data Received");
          }, 2000)

        })
      }

      // Async Function
      async function showData(){
        console.log("Data is Processsing...");

        let result = await getData();
        console.log(result);

        console.log("Work is Done Now !");

      }

      showData();
```

# Promise
Promise ek JavaScript ka object hota hai jo future mein kisi kaam ke complete hone ka wada (commitment) karta hai.<br>
1. API se data lana <br>
2. File read karna <br>
3. Time delay ke baad kuch karna

## Promise ke 3 states hoti hain:
1. Pending → kaam chal raha hai (not done yet)
2. Fulfilled → kaam successful ho gaya.
3. Rejected → kaam fail ho gaya.

Promise ya to tumhe Fulfilled ka result dyta hai✅<br>
ya phir Rejected ki result dyta hai ❌<br>
lakin empty result nahe dyta

## Example:
```js
  let a = new Promise(function(resolve , reject){
          let result = false;

          if(result){
            resolve("Work in Resolve.")
          
          }else{
            resolve("Work in Reject.")

          }          
       });

       a.then(function(finalResult){
        console.log("Success: " , finalResult)
       })

       a.catch(function(finalResult){
        console.log("Reject: " , finalResult)
})

// Jab tum new Promise(...) likhte ho, JavaScript tumhare function ko do helper functions bhejta hai
// 1. resolve (success ke liye)
// 2. reject (fail ke liye).
// Tum unhe parameters ki tarah use karte ho, aur jab kaam complete ho jaye, unko call karte ho.
```
# Promise Methods:
## .then()
Jab Promise successfully complete ho jaye (resolve ho) to .then() uska result ko handle karta hai.<br>
means ka ab Promise successfully complete ho jaye (tu resolve() call hoga) oisko handle karta hai .then() <br>
Tab .then() ke andar jo function likha hota hai, wo chalta hai. jaisa ka finalResult()<br>
Matlab .then() success handler hai.

## .catch()
Jab Promise fail ho jaye (reject ho) to .catch() uska error ko handle karta hai. <br>
means ka jab Promise fail ho jaye (tu reject() call hoga), <br>
Tab .catch() ke andar jo function likha hota hai, wo chalta hai. jaise ka finalResult()<br>
Matlab .catch() error handler hai. <br>

## Example 2:
```js
    function placeOrder(orderDetails){
      return new Promise((resolve, reject) => {
        document.getElementById("message").innerText = "⏳ Placing your order... Please wait";

        setTimeout(function(){
          if(orderDetails.pizza && orderDetails.address){
            resolve(`Your order for ${orderDetails.pizza} is Placed! Price: Rs: ${orderDetails.price}`)
          }else{
            reject('Order Failed: Missing details.');
          }
        }, 2000)

      });
    }

    // Handle form submit
  document.getElementById('orderForm').addEventListener('submit' , function(e){
      e.preventDefault();

      // Object
      let order = {
        pizza: document.getElementById("pizza").value,
        price: document.getElementById("price").value,
        address: document.getElementById("address").value
      };

      placeOrder(order)
        .then(function(msg){
          document.getElementById('message').innerHTML = msg;
        
        })
        .catch(function(error){
          document.getElementById('message').innerHTML = error;
        })

  });
```