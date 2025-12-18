## `Example 01`
```js
$(document).ready(function(){
  $("#box").css({
    "background-color": "lightgreen",
    "width": "200px",
    "height": "100px"
  });
```
## `Example 02`
```js
 $("#btnAdd").click(function(){
    $("#box").addClass("highlight");   // CSS class add kare
  });
```
## `Example 03`
```js
 $("#btnRemove").click(function(){
    $("#box").removeClass("highlight");// CSS class remove kare
  });
```
## `Example 04`
```js
  $("#btnToggle").click(function(){
    $("#box").toggleClass("highlight");// Add/remove toggle kare
  });
```
## `Example 05`
```js
$(document).ready(function(){
  $("#appendBtn").click(function(){
    $("#list").append("<li>New Item (End)</li>");
  });

  $("#prependBtn").click(function(){
    $("#list").prepend("<li>New Item (Start)</li>");
  });

  $("#removeBtn").click(function(){
    $("#list").remove();
  });
});
```

## `Example 06`
```js
$(document).ready(function(){
  
  // Fade in
  $("#showBtn").click(function(){
      $("#box").fadeIn("slow");
  });

  // Fade out
  $("#hideBtn").click(function(){
      $("#box").fadeOut(1000);
  });

  $("#toggleBtn").click(function(){
      $("#box").fadeToggle(500);
  });

});
```
## `Example 07`
```js
$(document).ready(function(){
  
  // Slide up
  $("#slideUpBtn").click(function(){
      $("#box").slideUp("slow");
  });

  // Slide down
  $("#slideDownBtn").click(function(){
      $("#box").slideDown("slow");
  });

  // Slide toggle
  $("#slideToggleBtn").click(function(){
      $("#box").slideToggle(700);
  });

});
```