# What is API:
1. API ka full form hai Application Programming Interface.

2. API ek bridge hai jo do applications ya systems ko ek dusre se baat karne aur data exchange karne ki permission deta hai.

3. API ek set of rules aur protocols hai jo different software applications ko ek doosre se communicate karne ki permission deta hai.

# API 2 Level per Depend karti hai:
1. API by Access Level
2. API by Protocol

---

# API by Access Level:
1. Yeh is baat par focus karta hai ke API kaun use kar sakta hai aur uska security scope kya hai.

# Type of API by Access:
1. Public (Open) APIs
2. Partner APIs
3. Private (Internal) APIs

## Public API:
1. Public API woh API hai jo internet par sabke liye open hoti hai. Koi bhi use kar sakta hai, chahe woh developer ho ya koi organization or koi public user bhi use kar sakta hai.
2. Iska istemal koi bhi kar sakta hai (learning ke liye best)
3. Documentation available hoti hai
4. Community support milti hai

## Partner API:
1. Partner APIs woh APIs hai jo specific partners ke liye open hoti hain.
2. Jo APIs kisi company ke sath collaboration ke baad milti hai
3. in main authentication zaroori hai.

## Private APIs:
1. Private API woh API hai jo sirf company ke andar use hoti hai. External public ko access nahi hai.
2. Yeh APIs public nahi hoti.
3. Sirf authorized log access kar sakte hain
4. Internal use ke liye best

---

# Api by Protocol:
1. Architecture Based API types ka matlab hai ki API kis design pattern ya structure ke according bani hai.

# Type of API by Protocol:
1. REST APIs
2. SOAP APIs
3. GraphQL APIs

# REST API:
1. REST koi software ya architectural design style (tarz) hai jo web services banane ke liye use hota hai.

2. Iska asal maqsad Resources (data jaisa ke Users, Photos, ya Products) ko access karna aur un par action lena hota hai.

3. REST API hamesha HTTP Protocols par kaam karti hai. Is mein 4 buniyadi kaam hote hain jinhein hum CRUD kehte hain `Create`, `Read` , `Update` or `Delete`.

4. Agar ek software Python mein bana hai aur dusra Java mein, to wo aapas mein direct baat nahi kar sakte. REST API unhe ek common rasta deti hai (HTTP) aur ek common zubaan deti hai (JSON).

5. REST ka ek barha rule hai `Statelessness`. Iska matlab hai ke server ko ye yaad rakhne ki zaroorat nahi ke aapne 2 minute pehle kya kiya tha.

6. Har request apne sath apni puri pehchan (Token/ID) lekar aati hai.

# SOAP API:
1. SOAP (Simple Object Access Protocol) ek structured protocol hai jo web services mein data exchange ke liye istemal hota hai.

2. SOAP APIs ka istemal ziyada tar enterprise-level applications aur high-security transactions ke liye hota hai, jahan data consistency aur security sab se zaroori ho.

# GraphQL API:
1. GraphQL ek modern API query language hai jo developers ko exact data fetch karne ki permission deta hai jo unhe chahiye hoti hai.

2. GraphQL ek protocol hai aur yeh REST APIs ke mukable ziyada efficient hai. kue ka is mein ek hi Request mein multiple Resources (data jaisa ke Users, Photos, ya Products) se data fetch kar sakte hain,jabke REST APIs mein multiple requests ki zarurat hoti hai.

3. GraphQL APIs developers ko flexibility deti hai ke woh sirf wahi data request karein jiski unhe zaroorat hai.

