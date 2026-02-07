# Render() or Redirect()
1. Django mein Render aur Redirect dono hi "Response" dene ke tariqe hain

## Render()
1. Iska matlab hai "Template mein HTML files ko dikhana". Jab user kisi URL par jata hai aur aap usay koi HTML page (template) dikhana chahte hain, to hum render use karte hain. Ye server se seedha HTML file utha kar browser ko bhej deta hai.

2. render sirf html ka page nahe dikhata hai balke yeah Python ka Dynamic Data ko bhe Context ka zariya HTML template ke andar fit kar dyta hai means render se hum Context (data) bhe bhej sakte hain. 

```py
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

# Redirect()
1. Iska matlab hai "Kisi aur raste par bhej dena". Jab kaam khatam ho jaye (maslan form submit ho jaye), to hum user ko kehte hain ke "Ab tum is page se hat kar dusre URL par chale jao". Ye browser ko ek naya address (URL) deta hai.

2. `redirect()` isme hum apne Route ka naam bhe likh sekhte hai or Name bhe likh sekhte hai jo `urls.py` mein pass karte hai wo wala name or iska ilawa hum isme `args (arguments)` or `Kwargs (keyword arguments)` bhe pass kar sekhte hai

```py
return redirect('url_name_or_path' , arug , kwargs)
```

# *args (Arguments) 🎒
Ye aik Magic Bag ki tarah hai. Aap is mein jitni marzi cheezein dalte jayen, ye un sab ko aik Tuple (aik kism ki list) mein band kar leta hai. Is mein "Asterisk" * ka nishan asal jadu hai, jo Python ko batata hai ke "baaki bache hue saare items is mein daal do" yeah aksar function ka parameter mein use hota hai.

# **kwargs (Keyword Arguments) 🏷️
Ye aik Label wali Diary ki tarah hai. Is mein aap cheezein "Naam" (Key) aur "Value" ke jore mein bhejte hain. Iska ** nishan Python ko batata hai ke ye aik Dictionary (jis mein key aur value ho) banani hai yeah aksar function ka parameter mein use hota hai. 


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

# What is Request Parameter?
1. Django mein jab aap kisi function (View) ke parameter mein request likhte hain, toh asal mein aap Django ko keh rahe hote hain ke browser se aane wali saari information is ek variable mein pack kar ke mujhe de do. Technical zubaan mein ise HttpRequest Object kehte hain.

2. is Request Parameter ko hum object bolte hai iska andar User aur uske browser ki saari info hoti hai.

3. Jab bhi koi user aapki website ke kisi link par click karta hai tu django aik Request bhejta hai jisa hum HttpRequest Object bolte hai. Is box ka naam hum aksar function mein `request` rakhte hain.