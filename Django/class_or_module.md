# What is Class?
1. [Class Basics Question](../OOP/class_object.md)

2. Python aur Django mein jab bhi hum `class` ko define karte hai phela hum apni class ka koi bhe naam likhte hai or phir brackets `()` ka andar kuch likha hota hai, wo class hoti hai isko or ache se samajte hai.

# Example:

```py
class StudentSerializer(serializers.ModelSerializer):
```

## Parent Class or Child Class:
1. Yahan **`ModelSerializer`** ek **Parent Class** hai. Parent class mein Code or logic phela se define hoti hai isko hum apne Class mein `Inherit` karte hai taake is Parent Class ki sari Power jo phela se define hoti hai django ki teraf se wo hum apne Child Class ka andar miljay jiska naam `StudentSerializer` hai `StudentSerializer` yeah humeri Child Class khelati hai jo humne khud create kari hai iska naam kch bhe rekh sekhte hai

2. Agar koi cheez `class MyName(...):` ke brackets ke andar likhi hai, to 100% wo ek **Class** hi hogi Python mein classes ko pehchanne ka ek standard tareeqa hai jise **PascalCase** kehte hain `Class` ka pehla letter hamesha **(Capital)** letter hota hai jaise ka `ModelSerializer` , `StudentSerializer`

## Module:
1. `serializers` yeah humera Module hai Module sirf ek Python file hoti hai iska anda python code hota hai bs Module ka naam likhna ka reason hai ka Jab aapka project bara hone lagta hai, to aap saara code ek hi file mein nahi rakhte (warna wo hazaron lines ki ho jayegi aur dhoondna mushkil ho jayega). Aap code ko alag-alag files mein baant dete hain. Inhi files ko Modules kehte hain.
