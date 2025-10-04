### World’s largest GIF library. Yahan aapko har type ke animated GIFs milenge: funny, reactions, nature, art, etc.

1. https://giphy.com/explore/animated-background?utm_source=chatgpt.com

2. https://www.animatedimages.org/?utm_source=chatgpt.com#google_vignette

3. https://pixabay.com/gifs/search/background/?utm_source=chatgpt.com

4. https://www.freepik.com/motion-graphics

# Add video lika BG Video

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      #bg-video {
        position: fixed; /* screen pe fix ho jaye */
        top: 0;
        left: 0;
        width: 100%; /* full width cover kare */
        height: 100%; /* full height cover kare */
        object-fit: cover; /* video stretch na ho, aspect ratio maintain ho */
        z-index: -1; /* content ke peeche rahe */
      }
    </style>
  </head>
  <body>
    <!-- Video -->
    <video autoplay muted loop playsinline id="bg-video">
      <source src="watch.mp4" type="video/mp4" />
    </video>
  </body>
</html>


<!--

autoplay → video automatic start ho jaye
muted → browser autoplay allow kare
loop → video baar-baar repeat ho
playsinline → mobile me page ke andar play ho

-->
```