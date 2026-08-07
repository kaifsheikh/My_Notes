# What is FastAPI:
1. FastAPI ek modern, high-performance Python ASGI **Asynchronous Server Gateway Interface** based framework hai jo APIs banane ke liye use hota hai.
    
    - ASGI ek rulebook (protocol) hai jo batati hai ki server aur Python application ke beech mein baat kaise hogi.

2. FastAPI Starlette framework par build hai aur Pydantic library ka use karta hai data validation ke liye.
    
    - **Starlette** ek lightweight, fast web framework hai. FastAPI isi ke upar bana hai.
    - Pydantic ek data checking machine hai jo Python ke type hints use karke data ko validate karta hai.

2. Ye Python 3.7+ ke saath kaam karta hai aur **asynchronous programming** ko support karta hai.

# Purpose of FastAPI:

# Installation of FastAPI:
1. Customer ki request sunta hai
2. Aapke code tak pahunchata hai
3. Jo jawab aata hai woh customer ko lauta deta hai
```py
pip install uvicorn
```

# How to Start Server:
1. **uvicorn main:app --reload**
    - *main* = file ka naam (main.py)
    - *app* = `app = FastAPI()` wala variable
    - *--reload* = code change hote hi server automatically restart ho jayega.

```py
uvicorn main:app --reload
```