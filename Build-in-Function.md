# Important Build-in-Functions in PHP:

### Empty();

yeah check karta hai ke variable khaali hai ya nahi. <br>
ager Empty yeah Null hai tu yeah (True) Return karayga <br>
ager yeah Empty yeah Null nahe hai tu yeah (False) Return karayga

```php
$name = "";

if (empty($name)) {
  echo "Name nahi diya gaya";
} // Output: Name nahi diya gaya
```

### isset();

yeah check karta hai ke:
Variable set hai (matlab ban gaya hai), <br>
or NULL nahi hai Yani variable bana to hai, lekin khaali hai, usme kuch bhi assign nahi kiya gaya.<br>
Agar variable set hai aur NULL nahi hai means Value hai, to isset return karta hai (True) <br>
Ager Variable mein Value nahe hai yeah Varaible create nahe hai yeah Null hai tu yeah return karayga (False)

```php
$city = NULL;

if (isset($city)) {
  echo $city;
} else {
  echo $city;
} // Output: kch nahe ayga
```

### strlen();

String ki length (characters ki ginti) nikalta hai.

```php
echo strlen("Hello");  // Output: 5
```

### explode();

String ko array mein convert karta hai. <br>
explode('Seperator' , $Variable_Name) <br>
separator = wo character ya symbol jahan se string ko todna hai ( , | - space)

```php
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

```php
$fruits = ["Apple", "Banana", "Grapes"];
$data = implode(" - ", $fruits);
echo $data;
// Output: Apple - Banana - Grapes
```

### array_push();

Array mein new item add karta hai Last mein.

```php
$colors = ["red", "blue"];
array_push($colors, "green");
print_r($colors);
// Output: Array ( [0] => red [1] => blue [2] => green )
```

### in_push();

Check karta hai ke koi value array ke andar exist karti hai ya nahi.

```php
$names = ["Ali", "Sara", "Ahmed"];
if(in_array("Sara", $names)) {
  echo "Yes";
}else{
  echo "No";
}
// Output: Yes
```

### move_uploaded_file();

move_uploaded_file() PHP ka function hai <br>
jo uploaded file ko temporary folder se le kar aapke specified folder (jaise uploads/) mein move karta hai, taa keh wo permanently server par save ho jaye. <br>

```php
$image_Name = $_FILES['image']['name'];
$tmp_Name = $_FILES['image']['tmp_name'];
$folder = "uploads/" . $image_Name;

move_uploaded_file($tmp_Name, $folder);
```

### pathinfo();

yeah function ek associative array return karta hai jisme file ke baare mein 4 important cheezein hoti hain:

1. dirname -> (uploads) Folder ya path jisme file hai
2. basename -> (myphoto.jpg) File ka full naam (with extension)
3. extension -> (jpg) File ka extension
4. filename -> (myphoto) Sirf file ka naam (extension ke bina)

```php
$imagePath = $image;

$info = pathinfo($imagePath);

$filename = $info['filename'];
$extension = $info['extension'];
$dirname = $info['dirname'];
$basename = $info['basename']; 

```
