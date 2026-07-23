# What is Opencv:
1. `Open Source Computer Vision Library ` yeah ek free aur open-source library hai. Isko C++ mein likha gaya hai, lekin aap isko Python mein bhi use kar sakte hain.
2. **Open Source**: Iska matlab hai yeh bilkul free hai, koi bhi isko use kar sakta hai aur iska code dekh sakta hai.
3. **Computer Vision**: Yeh computer science ki woh field hai jo computers ko insani aankhon ki tarah pictures aur videos ko analyze karna sikhati hai.

---

## OpenCV Purpose?

**Purpose** Insaan jab kisi cheez ko dekhta hai, to uska dimagh foran pehchan leta hai ke samne kya hai (jaise ke billi, gaari, ya kisi ka chehra). Lekin computer ke liye har picture sirf `numbers pixels` ka aik dher hoti hai. OpenCV ka maqsad computer ko aisi mathematical tools aur algorithms dena hai jis se woh un numbers ko samajh kar chehray, patterns, aur objects ko pehchan sakay.

---

## Where we use OpenCV:

* **Face Recognition:** Aapke phone ka Face Unlock feature ya Facebook par jab kisi ki picture par khud-ba-khud tag ka option aata hai, to peeche yeh tech chal rahi hoti hai.

* **Self-Driving Cars:** Tesla ya doosri autonomous (khud-kar) gaariyan road ki lanes, traffic lights, aur samne aane wale insano ko dekhne ke liye iska use karti hain.

* **CCTV Surveillance:** Security cameras mein jab koi achanak harkat (motion detection) hoti hai ya gaari ki number plate read karni hoti hai.

* **Medical Imaging:** X-rays, MRI scans, ya tumors wagera ko detect karne ke liye doctors aur software iska use karte hain.

* **Instagram/Snapchat Filters:** Jo filters aapke chehray par perfect set baithte hain (jaise dog ears ya glasses), woh OpenCV ke zariye chehray ke points ko track karke hi lagaye jaate hain.

---

## How to Work OpenCV:

OpenCV mein jab aap kisi image ko process karte hain, to uska aik bohot hi clear aur standard step-by-step tareeqay-kar (workflow) hota hai. Isay **Image Processing Pipeline** bhi kehte hain.

Aayein aasan Roman Urdu mein samajhte hain ke jab aap image processing karte hain, to sab se pehle kya hota hai, beech mein kya badlao aate hain, aur aakhir mein kya output milta hai.

---

## OpenCV Ka Overall Workflow:

1. **Image Ingestion / Input (Image Lena):** Step 1.
Sab se pehla kaam computer ko image dena hai. Aap `cv2.imread()` function ka use karke computer ki memory (hard drive ya direct camera feed) se image ko load karte hain. Is step par image apne asli rangon (BGR format) mein load hoti hai.


2. **Preprocessing (Image Ki Safai):** Step 2.
Asli image mein bohot zyada data hota hai jo computer ko slow kar sakta hai. Isliye hum image ko tayyar karte hain:

	- **Grayscale Conversion:** Rangon ko khatam karke image ko Black and White (Grayscale) kiya jata hai taake processing fast ho.
	- **Resizing:** Agar image bohot bari hai to uska size chota kiya jata hai.
	- **Blurring (Smoothing):** Image se faltu ka kachra ya "noise" (pixels ki kharabi) saaf karne ke liye use halka sa blur kiya jata hai.


3. **Segmentation & Detection (Ahem Hissay Alag Karna):** Step 3.
Ab computer image ke andar ahem cheezon ko dhoondta hai:

	- **Edge Detection:** Image mein maujood cheezon ke kinare (edges) dhoondna (jaise Canny Edge Detection).
	- **Thresholding:** Image ke background ko bilkul black aur kaam ki cheez ko bilkul white kar dena.
	- **Contours:** Shapes ki outer boundaries (boundaries) ko trace karna.


4. **Feature Extraction & Analysis (Data Nikalna):** Step 4.
Is step par computer faisla karta hai ya information nikalta hai. Maslan, agar aap chehra dhoond rahe hain, to computer dekhega ke chehre ke features (aankhein, naak) kahan hain. Agar aap koi shape dhoond rahe hain, to computer uske corners aur size ko calculate karega.


5. **Output & Visualization (Natija Dikhana):** Step 5.
Yeh aakhri step hai jahan aapko result milta hai:

	- **Drawing:** Aap dhoondi gayi cheez par rectangle ya circle draw karte hain (jaise `cv2.rectangle()`).
	- **Saving/Displaying:** `cv2.imshow()` se result screen par dikhaya jata hai ya `cv2.imwrite()` se nayi processed image ko save kar liya jata hai.

---

# Installation:

```bash
pip install opencv-python
```

## read Image:
```py
# OpenCV library ko import kiya
import cv2

# Image ko read kiya
image = cv2.imread('my_picture.jpg')

# Image ko screen par dikhaya
cv2.imshow('My Window', image)

# 3. Window ko tab tak khula rakha jab tak koi key press na ho
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Black and white Image:
1. computer ke liye colorful images ko samajhna mushkil hota hai.
2. Isliye hum image ko grayscale **Black** and **White** kar dete hain taake computer apna kaam jaldi kar sakay.

```py
import cv2

# Image laod
image = cv2.imread('test.jpg')

# cv2.cvtColor function ke zariye BGR (Color) ko GRAY (Black & White) mein badla
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Ab black & white image ko screen par dikhaya
cv2.imshow('Black and White Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Threshold:

```py
import cv2

image = cv2.imread('image2.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.Canny algorithm ko image di. 100 aur 200 iski settings (thresholds) hain
edges = cv2.Canny(gray_image, 100, 200)

# Screen par sirf image ki lines (sketches) nazar aayein gi
cv2.imshow('Image Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Image ke Kinare (Edges) find karna:
1. Hum OpenCV ko bolte hain ke picture mein jahan jahan lines ya kinare (edges) hain, sirf unko highlight kare.
2. Iske liye hum **Canny Edge Detector** use karte hain.
3.  

```py
import cv2

image = cv2.imread('test.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.Canny algorithm ko image di. 100 aur 200 iski settings (thresholds) hain
edges = cv2.Canny(gray_image, 100, 200)

# Screen par sirf image ki lines (sketches) nazar aayein gi
cv2.imshow('Image Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Image Resize:
1. kisi image ko crop ya chota karna hain.

```py
import cv2
image = cv2.imread('car.jpg')

# Humne computer ko kaha ke image ka size badal kar 300 width aur 200 height kar do
choti_image = cv2.resize(image, (300, 200))

cv2.imshow('Resize Image', choti_image)
cv2.waitKey(0)
```

---

## Image Blurring:

```py
import cv2
image = cv2.imread('text.jpg')

# (11, 11) ka matlab hai kitna zyada blur karna hai. 
# Yeh numbers jitne baray honge, tasveer utni dhundli hogi.
dhundli_image = cv2.GaussianBlur(image, (11, 11), 0)

cv2.imshow('Blur Image', dhundli_image)
cv2.waitKey(0)
```

---

## Write any text in Image:

```py
import cv2
image = cv2.imread('cat.jpg')

# cv2.putText(image, text, starting_point, font, size, color_bgr, thickness)
# (0, 0, 255) ka matlab hai Red rang mein likho
cv2.putText(image, 'Hello World!', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Meme Text', image)
cv2.waitKey(0)
```

---

## Image Rotate:

```py
import cv2
image = cv2.imread('scenery.jpg')

# Image ko 90 degrees seedhay haath (clockwise) ghuma diya
rorate_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Rotated Image', rorate_image)
cv2.waitKey(0)
```

---

