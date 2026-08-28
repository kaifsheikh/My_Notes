# JWT Definition:

> **JWT (JSON Web Token)** ek aisa **secure digital token** hai jo do systems (jaise aapka Browser aur Server) ke darmiyan kisi user ki **pechan (Identity)** ko safely verify karne ke liye istemal hota hai.

Simple Words: **JWT** yeh ek **digital token** ya **security pass** ki tarah hota hai jo check karta hai ke user kaun hai aur usko access milna chahiye ya nahi.

---

# 🎯 JWT ka Purpose:

Iska sab se bada maqsad **Authentication (Pehchan)** aur **Authorization (Ijazat)** ko asaan aur secure banana hai.

1. **Baar Baar Login Se Bachana:** Ek baar login hone ke baad server aapko **JWT (JSON Web Token)** de deta hai. Iske baad aap jab bhi app mein aage peeche jayenge, JWT hi aapki pehchan ban kar kaam karega.
2. **Server ka Bojh Kam Karna (Stateless):** Server ko apne paas yaad rakhne ki zaroorat nahi parti ke kaun kaun login hai. Sab info token ke andar hi hoti hai.

---

# 💡 Real-Life Example:

Maan lijiye aap ek Hotel mein stay karne jaate hain:

1. **Login Process:** Aap reception par jaate hain, apni ID aur Booking dikhate hain.
2. **JWT Issuance:** Receptionist aapko ek **Digital Key Card** de deta hai. Is card mein likha hota hai ke aap kis room number ke mehman hain aur aap kab tak ruk sakte hain.
3. **Using JWT:** Ab jab bhi aap apne room ka darwaza kholte hain ya Hotel ki Gym/Pool mein jaate hain, aapko reception par dobara ID nahi dikhani parti. Aap bas apna **Key Card** scanner par lagate hain aur darwaza khul jata hai.

**Web App mein:**

* Reception = **Login Page**
* Key Card = **JWT Token**
* Hotel Door/Gym = **App ke pages ya photos/videos**

---

JWT ke in sabhi components aur terms ko bilkul asaan aur step-by-step tareeqe se samajhte hain, taake aapko restaurant app banate waqt har cheez ki crystal-clear samajh ho.

---

## 1. Token Generation (Token Ka Banna)

**Token Generation** woh process hai jahan Server user ke successful login hone par ek naya JWT Token tayyar karta hai.

### Yeh Kaise Hota Hai?

1. Jab Waiter ya Admin apna correct email aur password daalta hai, toh Server kehne ko ek **"Digital Seal Machine"** chalta hai.
2. Server 3 cheezon ko milata hai:
* **Payload** (User ka Data)
* **Secret Key** (Server ki apni aik confidential chabi jo kisi ko nahi pata hoti)
* **Algorithm** (Security formula, e.g., HS256)


3. Is combination se ek lambi unique string banti hai jo kuch aise dikhti hai:
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMjMiLCJyb2xlIjoid2FpdGVyIn0...`

> **Real-Life Example:** Jaise Govt office aapki ID card details verify karke ek **Stamp & Signature** laga kar aapko Offical Pass issue kar deti hai.

---

## 2. Payload (Token Ke Andar Ka Data)

**Payload** JWT Token ka wo darmiyani hissa hota hai jisme **User ki Information** rakhi jaati hai. Is information ko JWT ki zaban mein **"Claims"** kehte hain.

### Payload Mein Kya Kya Hota Hai?

* **User Identity:** `userId`, `username`
* **Role:** `role: "waiter"` ya `role: "admin"`
* **Issue Date (`iat`):** Token kis waqt bana.
* **Expiry Date (`exp`):** Token kab khatam (expire) hoga.

```json
{
  "userId": "usr_9981",
  "name": "Kashif",
  "role": "waiter",
  "iat": 1723330000,
  "exp": 1723333600
}

```

> ⚠️ **Bohot Zaroori Baat:** Payload ko **Base64** se encode kiya jata hai, encrypt nahi! Iska matlab hai ke koi bhi banda `jwt.io` website par ja kar aapka payload **parh (read)** sakta hai. Isliye ismein **Password, Credit Card Details, ya Secret Keys** kabhi mat daalein.

---

## 3. Token Storage (Token Ko Kahan Save Karein?)

Jab Server JWT frontend (Browser ya Mobile App) ko bhej deta hai, toh frontend ko isey **apne paas safe rakhna** hota hai taake har agli API request ke sath yeh token bhej sake.

Browser mein Token save karne ke 2 main raste hain:

| Storage Type | Yeh Kya Hai? | Security Level | Pros & Cons |
| --- | --- | --- | --- |
| **`localStorage` / `sessionStorage**` | Browser ki simple memory jahan JavaScript data save karti hai. | ⚠️ Low (XSS Attack ka khatra) | **Fayda:** Code likhna bohot asaan hai.<br>

<br>**Nuksan:** Agar kisi hacker ne aapki site par malicious JS script chala di, toh wo token chura sakta hai. |
| **`HttpOnly Cookie`** *(Professional Way)* | Browser ki special Cookie jo Server khud set karta hai. | 🛡️ High (Secure) | **Fayda:** JavaScript is cookie ko read nahi kar sakti, isliye hackers token nahi chura sakte.<br>

<br>**Nuksan:** Set up karne ke liye thoda extra backend code likhna parta hai. |

---

## 4. Token Validation (Token Ki Checking)

Jab user app mein koi button dabata hai (jaise *“Order Status Change Karo”*), toh browser JWT Token ko request ke **Header** mein daal kar Server ko bhejta hai. Server is token ko check karta hai — isey **Token Validation** kehte hain.

### Server Validation Mein 3 Main Checks Lagata Hai:

1. **Signature Verification (Seal Check):**
Server apne paas rakhi **Secret Key** ka use karke JWT ka signature dubara calculate karta hai. Agar token mein kisi ne 1 character bhi badla ho (jaise role ko `waiter` se `admin` kiya ho), toh signature match nahi hoga aur request **Reject** ho jayegi.
2. **Expiration Check (`exp` Check):**
Server check karta hai ke kya token ki Expiry Date nikal toh nahi gayi? Agar token expire ho chuka hai, toh server `401 Unauthorized` error bhej deta hai aur app user ko logout kar deti hai.
3. **Role Authorization Check:**
Token se role nikal kar check kiya jata hai ke kya yeh user yeh kaam karne ke qabil hai? (e.g., Agar Chef *Bill Print* karne ki koshish kare, toh Middleware usey block kar dega).

---

### 💡 Summary (Ek Nazar Mein)

* **Generation:** Server par Secret Key se JWT Token banna.
* **Payload:** Token ke andar rakha hua user ka data (UserId, Role, Expiry).
* **Storage:** Token ko frontend par save karna (`HttpOnly Cookie` ya `localStorage`).
* **Validation:** Server par har request ke sath aane wale token ka Signature aur Expiry check karna.