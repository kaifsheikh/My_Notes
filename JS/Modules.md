# What is Modules in JS:
1. JavaScript modules ka matlab hota hai code ko alag files mein tod dena — taake har file ka apna kaam ho aur code clean aur reusable ban jaye. <br>
2. “Modules code ko organize karne ka ek system hai.”

## Export (code ko bahar bhejna):
1. “Is file se kuch cheez (function, variable, class, etc.) dusri file ko dena.”
2. Jaise tum ek file mein kuch functions likhte ho, aur chahte ho ke wo functions dusri file bhi use kar sake, to tum export karte ho.

## Example 01
```js
// main.js

// Export Varialbe
export let message = "This is the Sample Txt here.";

// Export Function
export function sum(a , b){
    let total = a + b;
    return total;
}

// export { message , sum }
```

```js
// libaray.js

// Import message or sum
import { message , sum } from './main.js';

// 2 Method Import
// import * as sample from './main.js'

document.body.innerHTML = message;
console.log(sum(10 , 10))
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type="module" src="./libaray.js"></script>
</head>
<body></body> 
</html>
```



