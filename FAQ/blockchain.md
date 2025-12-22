# What is Blockchain?
1. Digital Register / Khata (Ledger) jisme records (data) safe tareeke se store hota hain. aur ye blocks chain ki tarah ek dusre se linked hote hain.
2. bas fark yeah hai ka Blockchain computer par hota hai aur kisi aik admi / company ke control mein nahi hota.
3. Aisa system jisme record change nahi hota, sab ke paas copy hoti hai,

# What is Block?
1. Ek block ek page jaisa hota hai jisme:
2. Transaction info (kis ne kis ko paisay bheje)
3. Time & date
4.  

# What is Chain?
1. chain (zanjeer) ki tarah jure hotay hain Ek block → next block se linked hota hai

# Example 01: `Student Records`
1. Har students ki degree ek `Block` hai.
2. “Har block apne pichle block se connected hota hai kch is terha se

### Block 01   
`Name:` Ali <br>
`Roll No:` 1001 <br>
`Degree:` BSc

### Block 02
`Name:` Sara <br>
`Roll No:` 1002 <br>
`Degree:` BBS

### Block 03
`Name:` Ahmed <br>
`Roll No:` 1003 <br>
`Degree:` ADS

## Workflow:

1. `Block1:` **Ali** `Hash:` **abc123** `Previous:` **0**
   
2. `Block2:` **Sara** `Hash:` **def456** `Previous:` **abc123**
   
3. `Block3:` **Ahmed** `Hash:` **ghi789** `Previous:` **def456**

## Identify kaise hoga ka kisme Change hua hai:
`Block 2` me `Block 1` ka number likha hai <br>

`Block 3` me `Block 2` ka number likha hai <br>

Agar koi `Block 2` change karega tu → `Block 3` me likha number Mismatch hojayga → or pata chal jaye

