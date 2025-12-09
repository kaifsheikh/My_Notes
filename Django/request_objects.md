# What is Request Objects in Django?
1. `Request object` ek **data box** ki terha hai jo browser se server tak ki har aik single request ki kch information yeah data Server ka pass laykar jaata hai.
2. oisme `GET` or `POST` yeah humesha use hote hai chahay Request kaise bhe ho.

# GET:
1. Django mein GET request ka matlab hai ki user sirf data dekhna chah raha hai.
2. GET Request se user Server mein kch (change) nahi kar sekhta hai sirf Data dekh sekhta hai.

## GET mein Data kaha show hota hai:
1. Data URL bar me show hota hai.
2. Page open karna like (Home, About, Articles)
3. Data ko Search karke dekhne Website per
4. Data ko Filter yeah Sort karke dekhna
5. Sensitive data URL mein send nahe karna chaiya like (Password , Credit card info)
   
# POST:
1. Django mein POST request ka matlab hai ki user server ko naya data send kar raha hai.
2. ya Existing data mein koi changes karna cha reha hai like oisme (add, update, delete) karna.

## POST mein Data kaha show hota hai:
1. Data URL bar me show nahe hota hai.
3. Registration ka data send karna , login , logout , Comments , File Uplaod yeah sub kar sekhte hai or etc..
4. Existing Data ko (Read , Update , Delete , Read) yeah sub kar sekhte hai easily.
5. Sensitive data ko POST se send karna chaiya like (Password , Credit card info)


<!-- https://youtu.be/vU-_kX-fKVg?si=nr3UBYsBS0XnBfZ4&t=837 -->

## Example `POST` Method

