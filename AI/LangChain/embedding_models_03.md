# What is Embedding Models:
1. `Embedding models` wo models hote hai jo kisi bhi data ko jaise ka (text, image, audio) ko ek numerical vector mein convert karna jo uska “meaning” represent kare.

2. `Semantic Encoding` Semantic encoding ka matlab hai text ko numbers (vector) mein convert karna, aise ke similar meaning wali cheezein numbers ki form mein ek doosre ke paas ho jayein aur different meaning wali door ho jayein.

## Example:
```py
"I love cats" → [0.91, 0.12, 0.77]
"I like kittens" → [0.89, 0.10, 0.80]

"I bought a car" → [-0.40, 0.60, 0.10]
"Vehicle price is high" → [-0.45, 0.58, 0.12]

---

# yeh numbers random nahi hain
# yeh meaning represent karte hain

```