# Git Command:

## git branch "Branch Name"
    Is command ki madad se aik branch create hojayegi jiska naam kuch rakh sakte hain.

## git checkout -b "Branch_Name"
    isa aik new Branch create hojayge or -b ka matlab hai wo switch bhe hojayge new branch per

## 	git branch
    Is command ki madad se sari branches ajayengi jo humne create ki hui hain.

## git checkout "Branch_Name_here"
    Agar kisi specific branch ke andar jana ho to yehi command hai.

## git branch -d "Branch_name_here"
    Agar kisi branch ko delete karna ho to yehi command hai.

## 	git branch -m "New_Branch_Name"
    Agar kisi branch ka name rename karna ho to yehi command hai.

## Git log
    Yeah Commad History dekhati hai jiski madaad se hum apne saray commit dehk sekhte hai ka humne kab or kis waqt or kis time per commit kiya tha."or yeah her Commit per aik Link generate hota hai jiska hum ID bolte hai

## Git log --oneline
    Ye command aapko har commit ka short summary dikhata hai — sirf ek line mein.

## git show "Commit_Link"
    yeah humera commit wale link ki Information Provide karti hai.

## Git checkout "Past here Commit Link"
    Ager hume koi Commit delete karna ho jo humne phela kiya the tu oiski commad yeah hai ise humera Commit delete hojayga
    
## Git push origin "Branch_Name_Here"
    Is command ki madaad se humeri Branch jo humne phela se create ki the wo Branch humera Github ki Repository per Upload ho jayge lakin main/ master branch ka andar upload nahe hoge iski alag se branch create hoge github per.

## Git diff main
    Is command ki madaad se hum kisi branch ko kisi dosre branch se compare kar sekhte hai jis branch ko apne compare karna hai phela oiska andar ana hai then yeah command likhne hai (Git diff main) tu yeah apki main branch se compare karayge.

## Git merge branch_name
    Yeah command hum jab likhte hai jab hume kisi branch ko merge karna ho kisi dosre branch mein example ka liya meri aik main branch hai or aik css ki branch hai jiska andar mena css se related saray commits karay hua hai ager hume apne css wali branch ko main branch mein merge karna hai tu subse phela hume main branch ka andar ana hai or yeah command likhne hai. Isa humeri css wali branch main branch ka andar marge hojayge.
    
    yeah command humera Visual Studio ka terminal se Aik branch ko dosre branch se marge karta hai
    
## Git pull origin main
    Ager humne github ki website se kisi branch ko kisi dosre branch se merge kia hai tu yeah command hum likhte hai

## Git Deleting Methods

```bash
Difference Samjho:
Command	| Commit	   | Code	        | Staging
--soft	| ❌ Delete   | ✅ Safe	    | ✅ Staged
--mixed	| ❌ Delete	  | ✅ Safe	        | ❌ Unstaged
--hard	| ❌ Delete	  | ❌ Delete	    | ❌ Delete
```
