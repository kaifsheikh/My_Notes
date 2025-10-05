# 📦 Package Manager, Package aur Dependencies Cheat Sheet

Yeh document Node.js aur npm ke concepts ko simple **Roman Urdu** mein explain karta hai.

---

## 🔹 Package Manager Kya Hota Hai?

* **Package Manager** ek tool hota hai jo aapke liye ready-made code libraries download, install, update aur remove karta hai.
* Node.js ke liye sabse zyada use hone wala package manager hai **npm (Node Package Manager)**.

---

## 🔹 Package aur Library

1. **Library**
   → Library ek collection hoti hai ready-made functions/code ki, jo ek specific kaam asaan banati hai.

2. **Package**
   → Package ek complete bundle hota hai jisme:

   * Code (Library)
   * Metadata (naam, version, author, license)
   * Dependencies ka record hota hai.

3. **Example**

   * Aap `express` package install karte ho (npm se).
   * Ye aapko ek **server banane ki library** provide karta hai.

---

## 🔹 Dependencies vs DevDependencies

1. **Dependencies**

   * Ye woh packages hote hain jo project ko **chalane ke liye zaroori** hote hain.
   * Example:

     * `express` (server ke liye)
     * `mongoose` (database ke liye)
     * `axios` (API calls ke liye)

2. **DevDependencies**

   * Ye sirf **development ke time** use hote hain, production (live server) pe zaroori nahi hote.
   * Ye mainly developer ki madad karte hain.
   * Example:

     * Testing tools (jest, mocha)
     * Code linting (eslint)
     * Auto-reload tools (nodemon)

---

## 🔹 node_modules aur package.json

1. **node_modules/**

   * Is folder mein sari installed libraries ka real code store hota hai.
   * Ye folder bahut bada ho sakta hai.

2. **package.json**

   * Project ki ek info file hoti hai.
   * Isme project ke dependencies aur devDependencies dono list hote hain.
   * Example:

   ```json
   {
     "dependencies": {
       "express": "^4.19.0"
     },
     "devDependencies": {
       "nodemon": "^3.0.0"
     }
   }
   ```

---

## 🔹 npm Commands

1. **Install Package**

   ```bash
   npm install package_name
   ```

   → Ek package download karein aur dependencies mein add ho jaata hai.

2. **Install DevDependency**

   ```bash
   npm install package_name --save-dev
   ```

   → Package sirf devDependencies mein add hota hai.

3. **Uninstall Package**

   ```bash
   npm uninstall package_name
   ```

   → Package remove karne ke liye.

---

## 🔹 Scripts aur npm run

`package.json` file mein ek `scripts` section hota hai jisme aap custom commands likh sakte ho.

Example:

```json
"scripts": {
  "start": "node server.js",
  "chacha": "node index.js",
  "test": "test"
}
```

1. **npm start**

   * Default script run karne ke liye.
   * Yaha pe `server.js` run hoga.

2. **npm run chacha**

   * Custom script run karne ke liye.
   * Yaha pe `index.js` run hoga.

3. **npm test**

   * Code test karne ke liye.
   * Ye developer ke liye bugs dhundhne ka shortcut hai.

---