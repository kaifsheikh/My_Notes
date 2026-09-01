# What is Model?
1. Model aik Pre trained mathematical system hota hai
2. jo input (text, image, audio) ko process karta hai or Response mein hume output milta hai jaise ka (answer, prediction, text) generate karta hai.
3. Model bade datasets par train kiya jata hai. Yeh patterns seekhta hai, predictions karta hai, ya naya content generate karta hai.

## Model Parameters?
1. Parameter wo numerical values hote hai. jo model ke andar store hoti hain.
2. aur ye decide karte hain ke model input ko kaise process karega aur output kya dega.
3. or parameters floating-point numbers hotay hain String , Integer yeah Words nahe hote hai
4. Agar hum kahein ke GPT-3 ke **175 Billion parameters** hain, to iska matlab hai uske paas 175 billion chotay chotay "knobs" ya "settings" hain jo usay batate hain ke kis lafz ka kya matlab nikalna hai Jitne zyada parameters, AI utna hi smart hota hai.

## Model ka andar Paramter kaha per hote hai?
Model ke andar hotay hain:
1. Weights
2. Biases

## Weight:
1. Weight aik number hota hai
2. jo ye decide karta hai ke kisi input ki importance kitni hai.

## Bias:
1. Bias aik extra number hota hai
2. jo output ko thora sa adjust karta hai.

# Type of Models:
1. **Type 01:** wo models jo humera system ko manage karte hai jaise ka file create karna , delete karna , folder create karna , humera file ko read karke or oiske instruction ko follow karke code likha, humera batay gay instruction ko follow karna yeah sub powers `Agentic Models` ka pass hoti hai.

2. `Agentic Models` bhe humera LLM Models ka he hisa hai or Agentic Models mein yeah 3 cheezay hoti hai: <br>
    a. `Tool Calling` -> Filesystem tools ko use karne ki samajh <br>
    b. `Planning` -> Steps ko sequence mein execute karne ki ability <br>
    c. `Autonomy` -> Bina har step ke liye poochhe aage badhna <br>

# Free Models:
1. `Open Weight Models` -> yeah wo models hote hai jinhe hum free mein use kar sakte hai or yeah models publically `Open Source` hote hai jinhe koi bhe use kar sakta hai.

---

# What is AI Agent?

1. AI Agent ek aisa system hai jo AI model ko apna dimagh bana kar use karta hai. aur usme tools, memory, aur autonomy jod kar kaam karta hai.
2. Agent environment se information leta hai, sochta hai, aur phir actions perform karta hai — jaise files edit karna, web search karna, code run karna, ya API calls karna. Agent ka maqsad kisi goal ko poora karne ke liye multiple steps khud execute karna hai.

# AI Agent ke Zaroori Components:

1. **Model (LLM)**: Reasoning engine jo input samajh kar plan banata hai.
2. **Tools**: Functions jo agent call kar sakta hai (e.g., file padho, file likho, terminal chalao, web search karo).
3. **Memory**: Short-term (baat cheet ka history) aur long-term (data store) taake context yaad rahe.
4. **Planning/Orchestration**: Complex kaam ko chhote hisson mein todna, unka order tay karna, aur zaroorat par dobara try karna.
5. **Environment Interface**: Wo jagah jahan agent kaam karta hai (terminal, codebase, chat window).

# Type of AI Agent:

1. **Conversational Agents**: Sirf baat karte hain, jawab dete hain (ChatGPT, customer support bots).
2. **Task-Oriented Agents**: Khaas kaam karte hain (flight book karna, data scrape karna).
3. **Autonomous Agents**: Lambey kaam khud plan karke karte hain (AutoGPT, Devin).
4. **Multi-Agent Systems**: Kayi agents milkar kaam karte hain (research, writing, review).
5. **Embodied Agents**: Physical robots ya game AI.