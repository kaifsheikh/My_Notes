```r

my_list <- list(10, "Ali", TRUE, c(1,2,3))

my_list[[1]] # 10
my_list[[2]] # Ali

```
```r
my_list <- list( 
    name = "Ali" ,
    age = 20 ,
    score = list(math=90 , scinece=50)
)

my_list$name # Ali
my_list$score$math # 90

```
```r
student <- list(
  name = "Ali",
  age = 20,
  subjects = c("Math", "Physics"), 
  marks = list(Math=95, Physics=90)
)

student$name       # "Ali"
student$subjects # Math Physics
student$marks$Physics # 90

```
```r
stats <- function(x) {
  mean_val <- mean(x)
  max_val <- max(x)
  min_val <- min(x)
  return( list(mean = mean_val, max = max_val, min = min_val) )
}

result <- stats( c(5,10,15) )
result$mean  # 10
result$max   # 15
result$min   # 5

```