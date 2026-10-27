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

## Public (Open) APIs:

1. Public API woh API hai jo internet par sabke liye open hoti hai. Koi bhi use kar sakta hai, chahe woh developer ho ya koi organization ho developer ho, student ho, ya koi company ho.
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

# How does work API:

## API call mein 5 important things:

| Term           | Simple meaning                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| Endpoint / URL | Server ka address jahan request bhejni hai kisi specific address per yeah simple bolo tu kisi specific route per |
| Request        | Server se ki gayi demand                                                                                         |
| Method         | Request kis tarah bhejni hai                                                                                     |
| Response       | Server se wapas aane wala jawab                                                                                  |
| JSON           | Data bhejne aur receive karne ka common format                                                                   |

### Example endpoint:

`https://jsonplaceholder.typicode.com/users/1`

Is URL par request bhejne se ek sample user ki information mil sakti hai.

## API ke common methods:

- **GET**: data lena.
- **POST**: data bhejna ya naya record banana.
- **PUT/PATCH**: existing data update karna.
- **DELETE**: data delete karna.

Har API in methods ko apne rules ke mutabiq use karti hai.
