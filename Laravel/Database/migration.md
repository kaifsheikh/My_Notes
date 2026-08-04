# What is Migration?
1. Migration Laravel ka ek system hai jisse hum `database` ki tables ko `code` ke zariye create karte hai hai means Migration file mein sirf Table ka structure define hota hai like:

2. Migration file ka kam table create karne ka nahe hai isme sirf Table ko define kiya jata hai jaise: 
> Table ka naam<br>
> Columns define karna<br>
> Datatypes<br>
> Primary or Foreign Key<br>

3. Migration = Database ka version control hai jaise Git code ko save or track karta hai waise he database ko track or oiske structure ko migration file mein save karta hai.

## Make Connection in `.env` file:
1. Laravel project mein aik `.env` file hoti hai isme hum `database` connection mein apne database ka naam likhte hai.

## Make table:
1. laravel mein table create karne ka liya direct `Mysql` mein table create nahe karte hai.
2. for Example = ager muje `patients` naam ki table create karne hai tu hume phela `Migration` file create karne parti hai oiska liya yeah command likhte hai
3. `php artisan make:migration create_patients_table` = is command se aik file create hoti hai is location per `database/migration/2026_01_06_XXXXXX_create_patients_table.php` her table create karte time `create` & `table` likhna zarori hota hai or iska beech mein `table_name` likhte hai.

4. is file ka andar hum apne `table` ka structure ko define karte hai kch is terha se

```php
public function up()
{
    Schema::create('patients', function ($table) {
        $table->id();              // id column
        $table->string('name');    // name column
        $table->integer('age');    // age column
        $table->string('gender');  // gender
        $table->timestamps();      // created_at & updated_at
    });
}
```
5. Table ka structure ko define karne ka bad hum is command ko likhte hai.
6. `php artisan migrate` = is command se actual table create ho jaati hai `Mysql` ka andar

## Possibe Chances:
1. Migration banate waqt table ka naam galat likh diya lekin `php artisan migrate` ABHI tak run nahe kare ho
> ✔ Migration file ko delete kar do <br>
> ✔ Dobara sahi naam se command chalao <br>

1. Migration banate waqt table ka naam galat likh diya lekin `php artisan migrate` ABHI tak run nahe kare ho
> ✔ Migration file ko delete kar do <br>
> ✔ Dobara sahi naam se command chalao <br>

1. Migration se file bhe create karde or migrate bhe kardiya jisa database mein table bhe create hogai ager laravel se file ko or database se table ko delete karna ho permanennt tu oiska liya

> ✔ `php artisan migrate:rollback` <br>
> isa `database` se wo table delete hojayge.
> or laravel project mein hume khud se manually delete karne hoge bs.

`php artisan migrate:fresh` <br>
1. Ye command sabse pehle database ke saare tables ko bilkul khatam (delete) kar deti hai.
1. Phir ye aapke database/migrations folder ko dekhti hai. Wahan jitni files maujood hoti hain, ye sirf unhi ke tables dobara banati hai.

