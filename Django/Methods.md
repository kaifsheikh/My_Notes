## render()
```py
render(request, template_name, context=None, content_type=None, status=None, using=None)
```
1. `render()` method mein waise tu 6 paramters hote hai jisme se 4 Optional hote hai. 
1. `Request` : Ye user ki `request` hoti hai jo Browser se aati hai (URL, method, user info etc.)
2. `Template_Name` : Ye HTML file ka naam hota hai Jo Django ko batata hai ke kaunsa page show karna hai
3. `Context` : Ye dictionary hoti hai Ismein hum Python ka data HTML ko bhejte hain.
3. `Content_Type` : 
4. `status` : HTTP status code set karne ke liye

## Context:
1. Context ek dictionary hoti hai jisme woh data hota hai jo hum apni view (Python file) se template (HTML file) ko bhejna chahte hain.
2. hum Direct koi Data pass nahe kar sekhte hai jo bhe Data hoga wo Dictionary mein he Pass hoga.
3. Jo data Python mein hota hai (name, list, database results), woh HTML tak nahi jata tu isliye hum Context ko aza bridge ki terha use karte hai jisa View se HTML tak data bhejne ja sakay jiska liye hum“context” ka use karte hai.
4. Context sirf render() function ke andar use hota hai or render() mein 3 parameters expect karta hai.