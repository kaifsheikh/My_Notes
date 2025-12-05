# Charater (Text)
1. Character R mein wo datatype hota hai jis mein -> Alphabets , Words , Sentences , Special characters , Numbers-as-text

2. Character values double quotes " " ya single quotes ' ' ke andar hoti hain.

```r
x <- "Hello World"
typeof(x) # "character"


# Ye function characters ko join karta hai aur space by default beech mein dal deta hai.
paste("Hello", "Kaif")   # "Hello Kaif"

# yeah Without space join karta hai
paste0("Hello", "Kaif")  # "HelloKaif"


# her word ko , se Seperate karta hai Seperator dosra bhe use kar sekhte hai like . / ; etc
message <- paste("Hello", "This is", "Sample", "Text", sep="-")
print(message) # "Hello-This is-Sample-Text"


# String ko break karta hai
strsplit("A-B-C", "-") # "A" "B" "C"


# Charater Count karne ka liye
a <- nchar("Pakistan")
print(a) # 8

# Uppercase or Lowercase ka liye
toupper("pakistan")
tolower("PAKISTAN")

# String ka part ko Extract karega
substr("Pakistan", 1, 4) # "Paki"

# Number ko Charater Datatype mein convert karne ka liye
num <- 150
char_num <- as.character(num)
typeof(char_num)   # "character"

# Special Characters (Escape Sequences)

1. Escape sequences wo special characters hain jo aap normally directly string ke andar nahi likh sakte.
Is liye R inko represent karne ke liye backslash \ ka use karta hai.

| Escape | Meaning       |
| ------ | ------------- |
| `\"`   | Inside quotes |
| `\'`   | Single quote  |
| `\\`   | Backslash     |
| `\n`   | New line      |
| `\t`   | Tab           |

```