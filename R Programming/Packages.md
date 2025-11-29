# What is Packages in R
1. Code Functions: Pehle se likhe hue functions (tools) jo koi khaas kaam karte hain (jaise data ko saaf karna, graphs banana, ya complex statistics karna).

# What is Repositories in R
1. R mein Repository ek aisi online jagah ya server ko kehte hain jahaan $\text{R}$ ke packages aur unse judi files ko store kiya jaata hai.
2. taaki users unhe aasaani se download aur install kar saken.
3. Yeh bilkul ek online library 📚 ya App Store 📲 ki tarah kaam karta hai jahaan aap apni zaroorat ke tools dhoondh sakte hain.

## CRAN (The Official Repository)
1. CRAN ka full form hai **Comprehensive R Archive Network**. Yeh $\text{R}$ programming ki official aur sabse mashhoor Repository hai.


# How to Install Packages
```r
install.packages("package_name")
 
install.packages("readxl") 
```
# How to Activate Packages
```r
# yeah dono same hai
library(package_name) # isa koi Single Package download hojayga
require(package_name) 

# Multiple Packages Download:
install.packages(c("package_name", "package_name", "package_name"))

# Multiple Packages ko Activate karna ho tu:
# Option 01:
library(package_name)
library(package_name)
library(package_name)

# Option 02:
all_packages <- c("package_name", "package_name", "package_name",)

lapply(all_packages, library, character.only = TRUE)
# lapply -> yeah function, vector ke har naam ko uthata hai aur us par library() function run kar deta hai. Yeh ek tarah ki automation hai.

# character.only = TRUE -> yeh batata hai ki lapply ke andar jo naam hain woh text (character) ki form  mein hain.
```
# How to Deactive Packages
```r
# isa jo Package Activate hoga wo Deactive hojayga isko run karne se
detach("package:package_name" , unload=TRUE)
```

# How to Open and Read files in different format:

## Read `CSV` File
```r
data <- read.csv("folder_name/students.csv", header = TRUE, stringsAsFactors = FALSE)

# header = TRUE → R ko pata chal gaya ke Name, Age, Grade yeah columns hain.

# header = FALSE → R unko column names nahi samjhega, numbers assign karega: V1, V2, V3

# stringsAsFactors = FALSE → iska matlab: Text (like Name) ko as text hi rakho, factor na banao.
```



<!-- https://youtu.be/yejGKijmZ6I?si=EQKPwOWZUZaHM3-l&t=9795 -->