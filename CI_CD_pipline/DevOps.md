# What is DevOps?
1. Dev (Developers): Jo software banate aur code likhte thay
2. Ops (Operations): Jo us software ko servers par chalate aur maintain karte thay.
3. **Dev (Developers)**: Developers kehte thay mere computer pe chal raha hai, aur Operations kehte thay "server pe nahi chal raha." yeah aik issue hai
5. DevOps is masle ka hal hai. Ye koi tool nahi balkay ek soch (culture) hai jo in dono teams ko mila deti hai. Iska maqsad ye hai ke software jaldi banay, behtar quality ka ho, aur usme galtyan kam hon.

# What is CI or CD
## CI
1. CI ka matlab hai ke jab bhi koi developer code mein thori si bhi tabdeeli (change) kare, wo foran "Main Code" ke saath merge ho jaye aur system usey check kare.

## CD
1. CD ke 2 matlab hotey hain, aur dono hi CI ke baad aate hain.

## Continous Delivery:
Iska matlab hai ke aapka code har waqt "Ready" halat mein hai ke usay live (Internet par) kiya ja sake. Lekin live karne ke liye koi senior banda ek button dabata hai. Yaani automation toh hai, magar akhri faisla insaan ka hota hai.

## Continous Deployment:
Ye ek level upar hai. Isme koi button dabane ki zaroorat nahi hoti. Agar CI ke saare tests pass ho gaye, toh code khud-ba-khud live server par chala jata hai. User ko foran naya feature nazar aa jata hai.

# What is Gitlab?
1. GitLab ek Complete `DevOps platform` hai jo software development ke poore lifecycle ko manage karne ke liye istemal hota hai. Agar aasaan alfaaz mein kahein, toh ye ek aisi jagah hai jahan developers apna code rakhte hain, usey test karte hain, aur doosre logon ke saath mil kar kaam karte hain. means Planning, Coding, Testing, Security, aur Deployment ke saare tools aik hi software ke andar daal diye hain. Aapko koi teesra tool install karne ki zaroorat nahi parti or Ye Git naam ke version control system par base hai.

2. GitLab ka asli purpose software banane ke process ko tez aur asaan banana hai. yeah same Git ki terha hai hum apna code likhte hai commit karte hai push karte ager koi galti hojay tu oisa theek kar sekhte hai bilkul Git or Github per hota hai aik he project per multiple person bhe kam kar sekhte hai.

3. Self Hosting: hum Google , GitHub or Microsoft jaise model use karte hai apne Data or code ko store karna ka liya kue ka yeah Cloud-based hote hai. means hum iski Services use karte hai oe apne Data or Code ko store karne ka liya lakin Gitlab apko 2 option dyta hai.

- Aap chaho toh unki website (GitLab.com) use karo (bilkul GitHub ki tarah) apne code ka store karna ka liya.

- Ya phir aap unka software download karke apne Local computer ya apni company ke server par install kar lo. Phir aapka code/data kahin bahar nahi jayega, sirf aapke apne local Computer mein rahega isme Internet ki bhe need nahe parti hai isa hum khud data ka owner bana jate hai.

https://youtu.be/lFfqBxZf-6c?si=JYlcVyhx9XwnngvW

# Gitlab Pipeline:
1. jab hum Gitlab ka project mein is name ki file create karte hai `.gitlab-ci.yml` tu is file ko create karne se aik pipeline create ho jaate hai or ois Pipeline mein 4 stages hote hai .

2. `Build` , `Test` , `Push` or `Deploy` in stages ko hume khud define karna hota hai is `.gitlab-ci.yml` file mein karte hai

## Build:
1. Ye pehla step hai. Iska kaam code ko tayyar karna hota hai taake wo chalne ke qabil ho jaye.

## Test:
1. Build hone ke baad check kiya jata hai ke code mein koi galti tu nahi.

## Push:
1. Jab code test ho jata hai, tu usay kahin safe jagah save kiya jata hai jahan se deployment ho sake.

## Deploy:
1. Ye aakhri step hai jahan aapka code "Live" ho jata hai.

## Job:
1. Python mein Job ka matlab hota hai wo commands jo hum terminal ya command prompt par manually likhte hain, lekin GitLab unhein hamare liye automated tareeqay se chalata hai.



