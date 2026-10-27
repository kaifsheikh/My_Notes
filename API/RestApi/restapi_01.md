# What is Restapi:

1. REST = REpresentational State Transfer

| Word                 | Simple Meaning                                                        |
| -------------------- | --------------------------------------------------------------------- |
| **Representational** | Data ka representation (jaise JSON format mein data)                  |
| **State**            | Kisi cheez ki current situation (jaise user ka data, product ka data) |
| **Transfer**         | Ek jagah se doosri jagah bhejna                                       |

2. REST ek **design style** hai (rules ka set) jo batata hai ke **do systems ke beech data kaise exchange karna chahiye** — internet ke through.
   - **REST koi programming language nahi hai** (jaise Python ya Java)
   - **REST koi software nahi hai** (jaise Windows ya Chrome)
   - **REST koi protocol nahi hai** (jaise HTTP)

3. **REST API** woh API hai jo **REST ke rules (guidelines) ko follow karti hai** — taake do systems ke beech data exchange kiya ja sekhe ek standard or simple se. yehi iska main purpose hai 2 System ka beech Data ko Exchange karna like.
   - Do applications jo alag alag languages mein bani hain (ek Python mein, doosri JavaScript mein) — unko ek dusre se baat karwani hai. REST API translator ka kaam karti hai.

   - **Data Exchange**: Ek system ke paas data hai, doosre ko chahiye. REST API data ko safe aur organized tareeqe se transfer karti hai.
   - REST API mein data exchange ke liye koi ek fixed "language" nahi hoti — balke kuch data formats hote hain jinme se koi bhi use ho sakta hai. Lekin **JSON** sabse zyada common hai (95%+ cases mein) use hota hai.

   - **Standardization**: Har developer ko pata hai REST API kaise kaam karti hai. Isliye koi bhi nayi API use karna aasan hota hai.

4. REST API mein hum 4 buniyadi kaam karte hai sirf jisa **CRUD** kehte hain `Create`, `Read` , `Update` or `Delete`. REST API mein har CRUD operation ke liye **ek specific HTTP method** hota hai:

| CRUD Operation | HTTP Method         | Matlab           | Example            |
| -------------- | ------------------- | ---------------- | ------------------ |
| **C**reate     | **POST**            | Naya data banao  | Naya user banao    |
| **R**ead       | **GET**             | Data padho/lo    | User ki info dekho |
| **U**pdate     | **PUT** / **PATCH** | Data update karo | User ka naam badlo |
| **D**elete     | **DELETE**          | Data hatao       | User delete karo   |

### Example se samjho:

**REST ke saath (REST API style):**

```
GET    /books          → saari books lo
GET    /books/5        → book #5 lo
POST   /books          → nayi book banao
PUT    /books/5        → book #5 update karo
DELETE /books/5        → book #5 delete karo
```

5. Agar ek software Python mein bana hai aur dusra Java mein, to wo aapas mein direct baat nahi kar sakte. REST API unhe ek common rasta deti hai **HTTP Methods** aur ek common zubaan deti hai **JSON**.

# What is **Statelessness**:

**State = Kisi cheez ki current situation yeah yaad rakhi hui information.** means Yaad rakhi hui cheez — kisi system ko pata hona ke pehle kya hua tha.

**Stateless = "Yaad nahi rakhna"** — har request ko **fresh request** samjho, purani baaton ko bhool jao yeah hota stateless.

**REST API Stateless hoti hai** — means **server ko har request ke baad bhoolna padta hai** ke pehle kya hua tha. Server **kisi bhi client ki purani information yaad nahi rakhta**.

## Part 4: Stateful vs Stateless — Complete Comparison

| Point                      | Stateful                        | Stateless                |
| -------------------------- | ------------------------------- | ------------------------ |
| **Server yaad rakhta?**    | ✅ Haan                         | ❌ Nahi                  |
| **Har request mein info?** | Zaroori nahi                    | **Zaroori hai**          |
| **Example**                | Purani websites (session-based) | REST API (token-based)   |
| **Scalability**            | Mushkil                         | Aasan                    |
| **Server load**            | Zyada (memory mein sessions)    | Kam                      |
| **Failure handling**       | Mushkil (session gayab)         | Aasan (koi session nahi) |

# What is Token:

1. **Token** = Ek "digital ID card" jo server aapko deta hai jab aap login karte ho. tu har request mein yeh Token dikhana padta hai — taake server jaane ke aap kaun ho.

| Office ka ID Card                             | REST API ka Token                        |
| --------------------------------------------- | ---------------------------------------- |
| Reception se milta hai (login ke baad)        | Server se milta hai (login ke baad)      |
| Aapka naam, photo, designation likha hota hai | Aapka userId, name, role likha hota hai  |
| Har baar entry pe dikhana padta hai           | Har request mein bhejna padta hai        |
| Agar kho jaye, naya banwana padta hai         | Agar expire ho jaye, naya lena padta hai |
| Bina ID card ke andar nahi aa sakte           | Bina token ke API access nahi kar sakte  |

2. Token Humesha Login successfull hone ka bad milta hai without login apko token nhe milta hai.

## Token kab NAHI milta?

| Situation                  | Token milta?     | Kyun?                    |
| -------------------------- | ---------------- | ------------------------ |
| **Galat password**         | ❌ Nahi          | Verification fail        |
| **Galat OTP**              | ❌ Nahi          | Verification fail        |
| **Account banned**         | ❌ Nahi          | Server mana kar deta hai |
| **Email verify nahi hua**  | ❌ Nahi (mostly) | Pehle email verify karo  |
| **Bina login ke API call** | ❌ Nahi          | 401 Unauthorized         |

## Summary — Token kab milta hai?

| #   | Situation                      | Token milta?         |
| --- | ------------------------------ | -------------------- |
| 1   | Login (email/password)         | ✅ Haan              |
| 2   | Signup ke baad                 | ✅ Haan (mostly)     |
| 3   | OTP verify ke baad             | ✅ Haan              |
| 4   | Refresh token se               | ✅ Naya access token |
| 5   | Social login (Google/Facebook) | ✅ Haan              |
| 6   | API Key (server-to-server)     | ✅ Manually generate |
| 7   | Galat password/OTP             | ❌ Nahi              |
| 8   | Bina login ke                  | ❌ Nahi              |

## Token Purpose:

Token ka **3 main purpose** hai:

#### **Identity Batana**

Server ko pata chalna chahiye ke request **kaun bhej raha hai** — Ali, Sara, ya koi hacker.

#### **Authorization**

Sirf identity nahi — yeh bhi pata chalna chahiye ke aap **kaunsa kaam kar sakte ho**.

- **Admin** — user delete kar sakta hai
- **Normal user** — sirf apna profile dekh sakta hai
- **Guest** — sirf public data dekh sakta hai

#### **Statelessness**

Token ke andar hi saari info hoti hai — server ko **session yaad rakhne ki zaroorat nahi**.

# What Inside the Token?

1. Token ke andar **3 parts** hote hain — **Header**, **Payload** or **Signature**.
2. inhe dot (`.`) se alag kiya jata hai.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsIm5hbWUiOiJBbGkifQ.abc123signature
│                                      │                          │
│            HEADER                    │        PAYLOAD           │    SIGNATURE
```

```
HEADER.PAYLOAD.SIGNATURE
```

## `HEADER` — Token ka "Meta Data"

1. Header dekhne mein kch aysa hota yeah aik url ka format mein hota hai like this.
2. yeh **Base64Url** **encoded** hai. means yeah asli text ko machine-readable form mein badal diya gaya hai yeah human readable nhe hota hai.

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

3. jo asli text hota hai oisa hum decoded bolte hai or wo kch is terha ja dekhta hai like this

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

## typ:

1. **typ** batata hai ke "yeh token kis type ka hai".

## alg:

1. **alg** batata hai ke token ki SIGNATURE (security seal) kaunse "formula" se bani hai — matlab "signature ko verify kaise karna hai?"

### Example:

1. **Decoded HEADER** = `{"alg":"HS256","typ":"JWT"}` (insaan padh sakta hai)

2. **Encoded HEADER** = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (token mein yahi dikhta hai)

3. Header Token ka Meta data provide karta hai means yeah batata hai ka token kis type ka hai aur uski signature (security seal) kaunse hai or kis algorithm se bani hai.
   - **typ**:

## `PAYLOAD` — Token ka "Asli Data"

Yahan **user ki information** hoti hai. Payload mein **claims** hote hain — matlab "statements" ya "facts" user ke baare mein.

## Payload ke 3 Types of Claims:

1. `Registered Claims` (Standard Fields)
2. `Public Claims` (Custom Fields — Common)
3. `Private Claims` (App-Specific)

## SIGNATURE — Token ka "Security Guard"

Signature **koi data nahi** hoti — yeh ek **cryptographic hash** hai jo batata hai ke token **fake nahi hai**.
