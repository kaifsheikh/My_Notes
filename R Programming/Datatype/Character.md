# Charater (Text)
1. Character R mein wo datatype hota hai jis mein -> Alphabets , Words , Sentences , Special characters , Numbers-as-text

2. Character values double quotes " " ya single quotes ' ' ke andar hoti hain.

## `paste()` & `paste0()`
```r
a = "Hello"
b = "World"
final = paste(a , b)

final # "Hello World" ---> Concate karne ka liya


a = "Hello"
b = "World"
final = paste0(a , b)

final # "HelloWorld" ---> Concate karne ka liya lakin without Spaces
```

```r
x <- "Hello World"
typeof(x) # "character"


# her word ko , se Seperate karta hai Seperator dosra bhe use kar sekhte hai like . / ; etc
message <- paste("Hello", "This is", "Sample", "Text", sep="-")
print(message) # "Hello-This is-Sample-Text"


# String ko break karta hai
strsplit("A-B-C", "-") # "A" "B" "C"


# Charater Count karne ka liye
a = "Pakistan"
final = nchar(a)
print(a) # 8

# Uppercase or Lowercase ka liye
toupper("pakistan")
tolower("PAKISTAN")

# Charaters ko Count karayga 1 se 4 tak
a = "Hello World"
final = substr(a , 1 , 4)

final # Hell

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