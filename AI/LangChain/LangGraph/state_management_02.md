# What is State?

1. **State** basically aapke AI agent ka **Central Memory Box** ya **Data Container** hota hai.
2. Jab LangGraph mein koi kaam shuru hota hai, toh saara data—jaise user ka sawal, AI ka jawab, aur run hone wale tools ka result—ek jagah jama hota hai. Is poore jama shuda data ko hum **State** kehte hain.
3. LangGraph mein Node ek Python function hota hai jo State (central memory) se data parhta hai, apna specific kaam (LLM call ya tool) karta hai, aur updated data wapas State mein save kar deta hai. Isi tarah data State ke zariye ek Node se doosre Node tak travel karta rehta hai.

4. Python mein State ka structure define karne ke liye hum do alag tareeqon ka istemal karte hain:
    - **TypedDict**
    - **Pydantic Class**.

## 1. TypedDict (Simple Python Dictionary)

1. `TypedDict` Python ka ek built-in feature hai. Yeh ek normal Dictionary ki tarah kaam karti hai, lekin is mein hum pehle se fix kar dete hain ke konsi Key mein kis type ka data aayega (jaise String, Integer, ya List).

```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# Function ke zariye State definition banana
def get_agent_state():
    return TypedDict('AgentState', {
        'messages': Annotated[list, add_messages],
        'user_name': str
    })

# Call karke state structure mil gaya
AgentState = get_agent_state()
```

---

## 2. Pydantic Class (Advanced Data Validation)

1. Pydantic Python ki ek popular library hai jo Data Validation ke liye use hoti hai. Agar aap chahte hain ke State mein aane wala data bilkul sahi type ka ho (e.g. Age integer hi ho, email valid ho), toh Pydantic use karte hain.

```python
from pydantic import BaseModel, EmailStr

class UserProfileState(BaseModel):
    username: str
    age: int
    email: EmailStr  # Pydantic khud check karega ke email ka format sahi hai ya nahi
```
