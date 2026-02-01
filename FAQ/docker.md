# What is Docker?
1. Docker ek open-source platform hai jo application yeah website ko uske poore environment ke sath ek `Container` mein pack karta hai, taake wo application har system par bilkul same tarah se run ho like apne Local System per tu sahe run hota hai lakin jab hum Server Side per run karte hai tu ho sekhta hai Errors ay.

2. ager hum kisi Company yeah Team work kar reha ho or team members ka system different ho like kisi ka pass Windows yeah kisi ka pass linux yeah macbook ab hota kia hai ka ager windows mein humeri application yeah website run ho rehi hai lakin wahi same code linux per yeah mac per nahe run ho reha hai yeah jo code macbook per run ho reha hai wo windows mein run nahe ho reha is problems ko solve karne ka liya hum docker ka use karte hai.

## Example:
1. for example aap ne ek computer game banayi jo aap ke laptop par sahi chal rahi hai, lekin jab aap ne wahi same code apne dost ka laptop per run kiya to uske paas error aa gaya kyunke uske paas koi specific software ya setting missing thi.

2. Docker iska solution hai. Ye aapke code, libraries, aur settings ko ek Box `Container` mein pack kar deta hai. Ab ye Box dunya ke kisi bhi computer laptop linux yeah macbook par bilkul waisa hi chalega jaisa aap ke laptop per run ho raha tha.

# What is Docker and Docker Daemon?
1. Docker ek command-line-Interface aur platform hai jisse hum containers ko manage karte hain means Tumhara remote control / app jo Docker containers chalata hai, banata hai, delete karta hai means yeah sirf aik GUI / CLI hai jisa hum sirf direct Interact karte hai bs.

2. Doker Daemon ek background service hai jo Docker ke commands ko actually perform karta hai means Docker ka main engine / worker jo sab containers ko chalata hai, stop karta hai, delete karta hai, build karta hai.

## Example:
1. Jab tum docker run php:8.2 type karte ho → Docker command jaata hai Daemon ke paas, aur wo container create aur run karta hai.

# What is Docker `Image`?
1. `Image` aik Blueprint hota hai means aik Ready to Use Template jiska andar Project ka Enviroment Set hota hai means.

2. Image ek blueprint hoti hai (plan) jo ready-to-use template hoti hai jisme project ka poora environment pehle se set hota hai

3. Image mein environment hota hai, project files nahi hoti hai means.
4. `Image` = Container ka blueprint / template / recipe
5. image aik Ready Only template hota hai ager aik bar image create hogai tu wo bad mein update nahe ho sekhte ha. yeah tu oisa delete karna parta hai. yeah phir new image create karne parti hai

## `Blueprint`: 
1. pehle se bana hua naqsha / plan means
> kaunsi language use hogi <br>
> kaunsa version hoga <br>
> kaunsa software install hoga <br>

## `Ready to Use Template`: 
1. jo cheez phela se ready ho use karne ka liya means.
> PHP install nahi karna <br>
> Version select nahi karna <br>
> Composer setup nahi karn <br>
> Sab already ready hota hai 

## `Enviroment`: 
1. wo jagah jahan project chal raha hota hai means.

> Software project ka environment <br>
Operating system <br>
Programming language <br>
Language ka version <br>
Tools & libraries <br>
Agar environment same ho Project har jagah same chalta hai

# What is Docker `Container`?
1. Docker mein `Container` ek `running environment` hota hai jisme application aur uski saari required cheezen ek `Container`ka andar run hoti hai means.

## Isolated Container
2. her Container `Isolated` hota hai means `Container A` kisi dosre `Conrainer B` per Depend nahe karta hai yeah dono alag hote hai aik dosre se.

> Container A → PHP 8.2 <br>
Container B → PHP 7.4 <br>
Dono same machine pe run kar rahe hain, lekin ek doosre se bilkul alag. tu isliya her Container Isolated hota hai<br>

## Container Insight Image:
1. Container Image ka andar nahe hota hai yeah Image ka `Object` (Running Instance) hota hai jo Image se ban kar Run hota hai.

2. hum aik Image se Multiple Container bana sekhte hai or her Container dosre Container se Isolated hota hai

2. Image tu sirf aik Static File hoti hai lakin Container ka andar he poora Enviroment run hota hai isme mein sari file and folder hote hai Project ka.

- Container ke andar sirf website nahi hoti, balkay:
- Application ka code (Laravel, PHP, etc.)
- Runtime Enviroment (PHP, Node, Python)
- Libraries & dependencies
- Configuration files
- OS level files (minimal Linux)
- sab kuch ready-to-use hota hai aik `Container` ka andar.
- 👉 Code + Environment = `Container`

| Cheez   | Image                        | Container              |
| ------- | ---------------------------- | ---------------------- |
| Nature  | Blueprint                    | Running instance       |
| Role    | Define karta hai environment | Project ko chalata hai |
| Files   | Normally nahi hoti           | Hoti hain              |
| Version | Define hota hai              | Use hota hai           |
| State   | Static                       | Running / Stopped      |

# Docker Commands
1. `docker pull <image_name>`
2. `docker run -it <image_name> /bin/bash`