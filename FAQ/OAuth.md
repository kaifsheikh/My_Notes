# Authorization means:

1. **Authorization** ka matlab hai: **“Ijazat dena”** ya **“Permission dena”**.
2. Yeh batata hai ke koi cheez **kya kar sakti hai** aur **kya nahi kar sakti**.

---

# 🔑 OAuth:

> OAuth ek `open standard authorization protocol` hai. jo applications ko password share kiye baghair kisi doosre application ke resources tak limited access dene ki sahulat deta hai. Yeh token-based system hai jismein user apna password kisi third-party app ko nahi deta, balki ek authorization server se access token hasil karta hai jo specific permissions ke saath aata hai aur expire ho jata hai.

**Isko simple karte hain:**

> **OAuth ek safe tareeqa hai jisme aap kisi app ko apna password diye baghair sirf kuch cheezein karne ki ijazat dete hain. Woh ijazat ek chhoti si key (token) ki soorat mein hoti hai, jo limited hoti hai aur thodi der baad khud khatam ho jati hai.**

---

## 🏨 Sab Se Aasan Misal: Hotel Ka Key Card

Sochiye aap hotel mein gaye.

- **Password = Master Key**  
  Yeh poore hotel ke saare kamre khol sakti hai. Agar kho jaye to bohat khatra.

- **OAuth Token = Key Card**  
  Yeh sirf **aapka kamra** kholta hai, **2 din** tak kaam karta hai, aur reception se **cancel** ho sakta hai.

Bas! OAuth yahi karta hai — **master key ke bajaye limited key card** deta hai.