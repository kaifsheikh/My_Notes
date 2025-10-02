# CSS 3D Axis Basic Idea

| **Axis** | **Direction**   | **Imagine karo**           |
|----------|----------------|---------------------------|
| **X**    | Horizontal     | Left ↔ Right              |
| **Y**    | Vertical       | Top ↕ Bottom              |
| **Z**    | Depth          | Screen ke andar ↔ bahar  |

---

💡 **Simple socho:**  
- **X-axis** = side to side  
- **Y-axis** = up and down  
- **Z-axis** = screen ke andar/baahar


# Transform Properties:
Element ko move karta hai.
```css
transform: translate(100px, 50px);

/*

1. translateX(50px) → right side 50px
2. translateX(-50px) → left side 50px

3. translateY(50px) → down side 50px
4. translateY(-50px) → top side 50px

5. translate(50px, 100px) → right 50px, down 100px

*/
```

# rotate()
Element ko rotate karne ka liya use karte hai

```css
transform: rotate(45deg);

/*

1. rotate(45deg) → 45 degree clockwise
2. rotate(-45deg) → 45 degree anticlockwise

3. rotateX(45deg); → box top ya bottom ki taraf tilt ho jaata hai.
4. rotateY(45deg); → box left ya right ki taraf tilt ho jaata hai.

*/
```
# scale()
Element ko bada ya chhota karta hai.

```css
transform: scale(1.5);

/*

1. scaleX(2) → Sirf width ka size change karta hai.
2. scaleY(2) → Sirf height ka size change karta hai.

3. scale(2, 0.5); → Width aur height ko alagalag sizes me change karte hai.

*/
```
# Skew()
skew element ko tilt ya tedha karne ke liye use hota hai. <br>
Ye element ko horizontally ya vertically ya dono directions me slope deta hai.

```css
transform: skewY(20deg);
transform: skewX(30deg);
transform: skew(30deg, 20deg);


/*

1. skewY(20deg) → Sirf vertical tilt karta hai (up-down direction).
2. skewX(20deg) → Sirf horizontal tilt karta hai (left-right direction).
3. skew(30deg, 20deg) → Dono direction me tilt karta hai. skew(x-angle, y-angle)

*/
```
# 1. `matrix()` kya hai?
CSS ka `matrix()` function **ek hi line mein element ko move, scale, rotate aur skew** karne ke liye use hota hai.  

**Simple words:**  
> “Ek hi function se element ka size, angle aur position change kar sakte ho.”

---

## 2. Matrix ke 6 numbers

`matrix(a, b, c, d, e, f)` mein 6 numbers hote hain:

| Number | Meaning | Easy Words |
|--------|---------|------------|
| a      | Horizontal scale (width) | Width ko kitna bada/chhota karna hai |
| b      | Vertical skew (y-axis) | Element ko vertical tilt karna |
| c      | Horizontal skew (x-axis) | Element ko horizontal tilt karna |
| d      | Vertical scale (height) | Height ko kitna bada/chhota karna hai |
| e      | TranslateX (horizontal move) | Element ko horizontal move karna (px ya %) |
| f      | TranslateY (vertical move) | Element ko vertical move karna (px ya %) |

> **Tip:**  
- a & d → size (scale)  
- b & c → rotate/skew  
- e & f → move (translate)

---

## 3. Examples

### A. Normal element (no transform)
```css
div {
  transform: matrix(1, 0, 0, 1, 0, 0);
}
