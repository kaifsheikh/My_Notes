# Important Build-in-Functions in PHP:
### Empty();
yeah check karta hai ke variable khaali hai ya nahi.

``` php
$name = "";

if (empty($name)) {
  echo "Name nahi diya gaya";
} // Output: Name nahi diya gaya
```
### isset();
yeah check karta hai ke:
Variable set hai (matlab ban gaya hai), <br>
or NULL nahi hai Yani variable bana to hai, lekin khaali hai, usme kuch bhi assign nahi kiya gaya.<br>
Agar variable set hai aur NULL nahi hai, to isset() return karta hai true.

``` php
$city = NULL;

if (isset($city)) {
  echo $city;
} else {
  echo $city;
} // Output: kch nahe ayga
```
### strlen();
String ki length (characters ki ginti) nikalta hai.

``` php
echo strlen("Hello");  // Output: 5
```
### explode();
String ko array mein convert karta hai. <br>
explode('Seperator' , $Variable_Name) <br>
separator = wo character ya symbol jahan se string ko todna hai ( , | - space)

``` php
$data = "Apple , Banana , Grapes";
$fruits = explode("," , $data);
print_r($fruits);

// Output: Array ( [0] => Apple [1] => Banana [2] => Grapes )

$data = "Apple | Banana | Grapes";
$fruits = explode("|" , $data);
print_r($fruits);

// Output: Array ( [0] => Apple [1] => Banana [2] => Grapes )
```
### implode();
Array ko string mein convert karta hai.

``` php
$fruits = ["Apple", "Banana", "Grapes"];
$data = implode(" - ", $fruits);
echo $data;
// Output: Apple - Banana - Grapes
```
### array_push();
Array mein new item add karta hai Last mein.

``` php
$colors = ["red", "blue"];
array_push($colors, "green");
print_r($colors);
// Output: Array ( [0] => red [1] => blue [2] => green )
```

### in_push();
Check karta hai ke koi value array ke andar exist karti hai ya nahi.

``` php
$names = ["Ali", "Sara", "Ahmed"];
if(in_array("Sara", $names)) {
  echo "Yes";
}else{
  echo "No";
}
// Output: Yes
```