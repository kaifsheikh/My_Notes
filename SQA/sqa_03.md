# What is STLC:

1. **STLC** means **Software Testing Life Cycle**.
2. Yeh woh complete way hai jo aik QA Tester ko kisi software ki testing karte waqt start se lekar end tak follow karna parta hai taake testing properly ho.
3. Jaise SDLC poora software banane ka safar hai, bilkul waise hi STLC sirf us software ko test karne ka mukammal process hai jise follow karne se koi bug chhoot nahi pata.

# Purpose:

* **Har cheez check karna:** Taake app ka koi bhi chota ya bara hissa testing se reh na jaye aur sab kuch cover ho jaye.
* **Bugs ka record rakhna:** Professional tareeqay se ghaltiyon ko dhoondna, record karna aur developers se theek karwana.
* **Quality ki guarantee dena:** Company aur client ko itminan dilana ke ab app 100% theek kaam kar rahi hai aur market mein launch ke liye tayar hai.

---

## Step 1: Requirement Analysis:

* **means:** Sab se pehle Tester app ki file ya document (SRS) parhta hai taake samajh sake ke app banayi kyun gayi hai aur isme kya kya test karna hai.
* **example:** Aap document parhte hain aur note karte hain ke, "Mujhe is Food App mein Login page, Menu page, aur Payment system ki testing karni hai."

## Step 2: Test Planning:

* **means:** Is step mein QA Manager ya team lead faisla karta hai ke testing kaise hogi, kitna waqt lagega, aur kaun sa tester kya kaam karega.
* **example:** Plan banta hai ke testing mein 5 din lagenge. Aap (Tester 1) sirf Login aur Payment check karenge, aur Tester 2 sirf food order ka hissa check karega.

## Step 3: Test Case Development:

* **means:** Testing shuru karne se pehle tester copy, Excel ya Jira mein likhta hai ke woh practically app ko kin steps mein check karega.
* **example:** Aap Excel mein likhte hain: "Agar user ghalat password dale, toh app login nahi honi chahiye aur 'Wrong Password' ka error aana chahiye."

## Step 4: Test Environment Setup:

* **means:** Testing shuru karne ke liye zaroori cheezein (jaise testing mobile, laptop, fast internet, ya dummy accounts) ready ki jati hain.
* **example:** Aap apne mobile mein woh kachi (un-released) Food App install karte hain aur test karne ke liye fake email/passwords ready karte hain.

## Step 5: Test Execution (Asal Testing / Action Time):

* **means:** Jo Test Cases aapne Step 3 mein likhe thay, ab aap sach mein mobile par app chala kar unko apply karte hain. Agar koi ghalti miley toh usay "Bug" kehte hain.
* **example:** Aapne app mein ghalat password dala, lekin error aane ke bajaye app login ho gayi! Yeh bug hai. Aap foran screenshot lete hain aur developer ko bhej dete hain ke isko theek karo.

## Step 6: Test Cycle Closure:

* **means:** Jab sab bugs pakre jate hain, developer unko theek kar deta hai, aur aap dobara check (re-testing) kar lete hain, toh aakhir mein aik summary report banai jati hai.
* **example:** Aap aakhri report banate hain: "Humne 100 cheezein test ki theen, 15 bugs nikle thay jo ab theek ho chuke hain. Hamari taraf se app bilkul pass hai."