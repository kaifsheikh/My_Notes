## `Example 01`
```js
function checkAge(name, age) {
  if (age >= 18) {
    console.log(name + ", you are an adult.");
  } else {
    console.log(name + ", you are still a minor.");
  }
}

checkAge("Ali", 20);
checkAge("Sara", 15);
```
## `Example 02`
```js
function greet(name = "Guest") {
  console.log("Hello " + name);
}

greet("Ali");   // Output: Hello Ali
greet();        // Output: Hello Guest
```

## `Example 03`
```js
  function userInfo(name, age) {
            return {
                name: name,
                age: age,
                status: age >= 18 ? "Adult" : "Minor"
            };
        }

        const user = userInfo("Ali", 16);
        console.log(user.name);    // Ali
        console.log(user.status);  // Adult
```

## `Example 04`
```js
function checkEven(num) {
  return num % 2 === 0 ? "Even" : "Odd";
}

console.log(checkEven(10)); // Even
console.log(checkEven(7));  // Odd
```
## `Example 05`
```js
function countdown(num) {
  if (num <= 0) {
    console.log("Done!");
    return;
  }
  console.log(num);
  countdown(num - 1);  // function apne aap ko call kar raha hai
}

countdown(5);
```