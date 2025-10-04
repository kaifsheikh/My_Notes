# What is Modules in JS:
1. JavaScript modules ka matlab hota hai code ko alag files mein tod dena — taake har file ka apna kaam ho aur code clean aur reusable ban jaye. <br>
2. “Modules code ko organize karne ka ek system hai.”

## Export (code ko bahar bhejna):
1. “Is file se kuch cheez (function, variable, class, etc.) dusri file ko dena.”
2. Jaise tum ek file mein kuch functions likhte ho, aur chahte ho ke wo functions dusri file bhi use kar sake, to tum export karte ho.

## Example 01
```js
// math.js

export function add(a, b) {
  return a + b;
}

export function sub(a, b) {
  return a - b;
}

// Yahaan humne 2 functions banaye
// aur unhe export kiya taake dusri file use kar sake.
```

```js
// main.js

import { add, sub } from './math.js';

console.log(add(5, 3)); // 8
console.log(sub(5, 3)); // 2

// Yahaan humne math.js se add aur sub import kiye,
// aur apni file main.js mein unhe use kar liya.
```



