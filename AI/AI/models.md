# What is Model?
1. Model aik trained mathematical function hota hai
2. jo input (text, image, audio) ko process karke
3. output (answer, prediction, text) generate karta hai.

## Model Parameters?
1. Parameter wo numerical values hotay hain
2. jo model ke andar store hotay hain
3. aur ye decide karte hain ke model input ko kaise process karega aur output kya dega.
4. or parameters floating-point numbers hotay hain String , Integer yeah Words nahe hote hai
5. Agar hum kahein ke GPT-3 ke 175 Billion parameters hain, to iska matlab hai uske paas 175 billion chotay chotay "knobs" ya "settings" hain jo usay batate hain ke kis lafz ka kya matlab nikalna hai Jitne zyada parameters, AI utna hi smart hota hai.

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
1. `Open Weight Models` -> yeah wo models hote hai jinhe hum free mein use kar sakte hai or yeah models publically `Open Source` hote hai jinhe koi bhe use kar sakta hai 

# What is Inference?
1. Inference wo process hai jisme trained model ko new input diya jata hai aur output liya jata hai
without training.

# What is MCP?
1. MCP `(Model Context Protocol)` Ye kisi bhe AI model ko external tools aur data sources se connect karne ki permission deta hai simple words mein - MCP ek universal adapter hai jo kisi bhe AI model ko files, databases, APIs, browsers, Excel se connect karne ki common language deta hai.
2. MCP ka benefit yeah hai ke AI ko har tool ke liye separate code likhne ki bajaye, MCP use karke kisi bhe tool se connect kiya ja sakta hai.
3. MCP ek universal bridge hai jo AI model ko kisi bhi external system se connect kar deta hai.
4. MCP complelety Open Source hai. koi bhe use kar sakta hai.

## MCP ka main 3 types hote hai:
1. `Data Source MCP Servers`
2. `Services MCP Servers`
3. `Tools MCP Servers`