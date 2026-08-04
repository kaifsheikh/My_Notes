# View:
1. View ka kam sirf User ko oiski screen per `UI` dekhana means.
2. `HTML` , `CSS` ko show karwana View mein hum koi `Logic` nahi likhte hai.
2. View ki Location `resources/views/`

# What is `Blade Template` in Laravel?
1. `Blade` Laravel ka template engine hai jo HTML pages ko dynamic banata hai.
2. `Template engine` ka matlab `HTML` ke andar `PHP` ko simple aur clean tareeqe se likhna.
4. **Purpose:** `Template engine` ka kaam `Dynamic data` ko `HTML`or `CSS` ke sath jor kar final output banana hota hai

```php
index.blade.php

// index => Ye file ka naam hai
// .blade => Ye Laravel ka Blade template engine hai
// .php => Laravel ke andar sab kuch PHP par chalta hai Is liye last mein .php hota hai 
```

# What is `Sub View`?
1. `Chhoti view` file jo kisi `badi view` file ke andar `include` ki jaati hai tu ois choti view file ko` Sub View` bolte hai.
2. `View` = poora page
3. `Sub View` = page ka chhota hissa
4. `@include(folder_name.file_name)` yeah line jaha bhe likhte hai ois jagah par doosri `view file` ka content ajata hai.
5. **Purpose:** `@include()` Repeat hone wala code ek jagah likh kar har jagah use karna 
```php
// routes/web.php
<?php

use Illuminate\Support\Facades\Route;
use Symfony\Component\Translation\Provider\Dsn;
use App\Http\Controllers\UserController; // Import => UserController

Route::get('/home' , [UserController::class , "home"]); 

// app/Http/Controlles/UserController.php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Spatie\FlareClient\View;

class UserController extends Controller
{
    function home(){
        return view('header.inner');
    }
}

// resources/views/header/common.blade.php
<div style="background-color: black; color: white;">
    <h1>Header Part Common Code</h1>
</div>

// resources/views/header/inner.blade.php
@include('header.common')
<div>
    <h1>Inner File</h1>
</div>
```

# Laravel Blade Symbols:

| Symbol  | Kya hai                    | Kahan use hota hai                | Purpose (kyun use hota hai)                      | Easy Example        |
| ------- | -------------------------- | --------------------------------- | ------------------------------------------------ | ------------------- |
| `@`     | **Blade Directive**        | Sirf **Blade (.blade.php)** files | Decision / loop / Blade ka logic likhne ke liye  | `@if($user) @foreach`        |
| `$`     | **PHP Variable**           | PHP files **aur** Blade           | Data ko hold karne ke liye                       | `$errors`, `$user`  |
| `{{ }}` | **Blade Echo**             | Sirf Blade                        | Variable ka value **screen par dikhane** ke liye | `{{ $user->name }}` |
| `()`    | **Function / Method Call** | PHP + Blade                       | Function ko call karne ya value dene ke liye     | `$errors->any() all()`    |
| `' '`   | **String (text)**          | PHP + Blade                       | Fixed text pass karne ke liye                    | `'username'`        |
