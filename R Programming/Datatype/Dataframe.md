
# `Data Frame:`
1. Data Frame ek table hoti hai jisme rows aur columns hote hain, bilkul Excel sheet ki tarah.
2. Isme hum her type ka data ko store karte hain — numbers, text, categories sab kuch.

## `Object`
1. Object ek `box` ya `container` jisme hum koi bhi cheez (data, list, result, ya function) store kar sakte hain.
2. aur is box ke andar `number`, `text`, `vector`, `matrix`, `data frame`, `function`... sab kuch aa sakta hai.

## `Example 01 (Data Frame):`
```r
df <- data.frame(
  name = c("Ali" , "Ahmed" , "Karlie" , "Smith" , "Shai1"),
  marks = c(480 , 300 , 259 , 400 , 360),
  age = c(20 , 24 , 29 , 19 , 18)
)

print(df)

1. # `df` - df yeah object hai iske andar hum ek data frame (table) store kar rahe ha.
2. # data.frame() - Ye function hai jo ek table (data frame) banata hai.
2. # `name` , `marks` , `age` - yeh humera columns hai jo object ka andar hai or inha hum Variables bolte hai.
```

## `Examples`
```r
# Sample data frame
students <- data.frame(
  Name = c("Ali", "Sara", "Ahmed", "Hina", "Zoya"),
  Age = c(20, 21, 19, 22, 20),
  Grade = c("A", "B", "A", "B", "A")
)

head(students, 3) # 1 se 3 Rows ka data Show hoga

tail(students, 2) # Last ka 2 Rows ka Data show karne ka liya

students$Name # kisi Specific Column ko Dekhne ka liya

students[1:3 , ] # 1 se 3 tak ki Rows show honge Sari Columns ki

students[1:3 , c("Name" , "Grade")] # 1 se 3 Rows show honge lakin Name or Grade Columns ka Data only

view(students) # Table ki form mein show hoga Data
```