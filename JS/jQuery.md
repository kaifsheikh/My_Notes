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
