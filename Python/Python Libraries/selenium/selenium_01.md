## Whar is Selenium:

**Selenium** ek powerful tool hai jo **web browsers ko automate** karta hai. Matlab, aap Python code likh kar browser (Chrome, Firefox, Edge) ko khud ba khud kuch karne ke liye keh sakte hain, jaise koi insaan keyboard aur mouse use kar raha ho.

**Simple Definition:**  
> Selenium ek Python library hai jo websites ke saath automatically interact karti hai — jaise pages open karna, buttons click karna, text type karna, screenshots lena, aur data scrape karna.

---

## Selenium ka Purpose:

1. **Web Automation** — Repeat hone wale tasks automate karna (jaise daily reports download karna)
2. **Web Scraping** — Un websites se data nikalna jo dynamic hain (JavaScript se load hoti hain)
3. **Web Testing** — Check karna ke website sahi kaam kar rahi hai ya nahi (automated testing)
4. **Form Filling** — Automatically forms bharwana
5. **Screenshots** — Web pages ke screenshots lena

---

## Selenium Kab Use Karte Hain?

| Scenario | Example |
|----------|---------|
| Jab website JavaScript use karti hai aur normal scraping (BeautifulSoup) kaam nahi karti | Amazon, Flipkart, Social media sites |
| Jab aapko login karna ho aur baad mein data lena ho | Gmail, Banking sites |
| Jab aapko button click, dropdown select, ya scroll karna ho | Search results load karna |
| Jab aapko multiple pages navigate karni ho | E-commerce product listing |

---

### Step 1: Installation

```bash
pip install selenium
```

### Step 2: WebDriver Download Karna

WebDriver ko rakhne ke do aasan tareeke hain. Pehla aur sabse aasan tareeqa hai **use direct code mein path dena**, aur doosra hai **usay system ke PATH variable mein add karna taake woh kisi bhi jagah se work kare** or aik **autointaller command ki through automatic webdriver download karne ka bhe option hai**

### Auto-Installer for Chrome:

1. yeah packages `chromedriver-binary`  ya `chromedriver-autoinstaller` Jab aap code chalayen, toh yeh check karta hai ke aap ke computer mein sahe ChromeDriver (woh bridge jo Python ko Chrome se jorta hai) hai ya nahi. Agar nahi, toh yeh khud internet se download kar ke rakh deta hai aur auto-setup kar deta hai.

```bash
pip install chromedriver-autoinstaller
```

```python
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# only for checking purpose
```