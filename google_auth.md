Bilkul Kaif! Ab main tumhein Google Auth Start (yani ke Google OAuth 2.0 ka setup) ko bilkul easy, step-by-step, roman-urdu mein samjha deta hoon. Yeh sabse important step hota hai Google Login ko website per chalane ke liye.

Isko parhne ke baad tum bilkul easily Google Login setup kar paoge.

⭐ GOOGLE AUTH START — EASY GUIDE

Google Auth start karne ke liye tumhein sirf 3 jagah kaam karna hota hai:

Google Cloud Console → Project create

OAuth Consent Screen setup

OAuth Credentials (Client ID + Secret) create

Bas yeh 3 steps complete karte hi tum Google Auth start kar sakte ho.

Main niche har step ko simple tareeke se samjha raha hoon.

✅ STEP 1 — Google Cloud Console per Project Create Karo
👉 Follow:

Open: https://console.cloud.google.com/

Top per Select Project ya “Create Project” dikhega

“New Project” per click karo

Project ka naam do:
my-site-login

Create per click kar do

🟢 Ho gaya!
Ab tumhare paas ek khaali project ready hai.

✅ STEP 2 — OAuth Consent Screen Setup (VERY IMPORTANT)

Google ko batana padta hai ke tum kis purpose ke liye login use kar rahe ho.

👉 Steps:

Left side menu → APIs & Services

Click on OAuth Consent Screen

User Type = External select karo

App name likho (ex: My Site Login)

Email add karo

Save karo

🟢 Ho gaya!

✅ STEP 3 — OAuth Credentials Create Karo

Yahan se tumhein Client ID aur Client Secret milti hai. Yeh dono code me use hoti hain.

👉 Steps:

Left menu → APIs & Services → Credentials

Top per Create Credentials

Select → OAuth Client ID

Now:

Application Type: Web Application

Name: Google Login

AUTHORIZED REDIRECT URI add karo
Yeh bahut important hota hai.

Example:

https://yourwebsite.com/callback.php


Save karo

Google tumhein 2 cheezein dega:

✔ Client ID
✔ Client Secret

🎉 Yahi Google Auth Start ka main content hai!

Ab tum Google Login start kar sakte ho.

⭐ Ab Tum Code Me Yeh 2 Cheezein Use Karoge

Example:

$client_id = "YOUR_GOOGLE_CLIENT_ID";
$client_secret = "YOUR_GOOGLE_CLIENT_SECRET";
$redirect_uri = "https://yourwebsite.com/callback.php";

🔥 Google Auth Start ka Flow

User clicks: Login with Google

Tumhari website user ko bhejti hai Google par (google-login.php)

Google permission mangta hai

Google user ko tumhari site ke callback page per bhejta hai

Tumhy name, email, picture mil jati hai

Login ho jata hai

⭐ If You Want → Main tumhare liye poora ready-made setup bana sakta hoon:

✔ google-login.php
✔ callback.php
✔ login.php
✔ logout.php
✔ session system
✔ MySQL database insert (optional)

Bas mujhe yeh batao:

👉 Tumhari website live domain per hai? (jese: mysite.com)
ya
👉 Tum localhost (XAMPP / WAMP) per ho?

Jis base per ho, main uske hisaab se tumhara pura Google Auth setup bana dunga.