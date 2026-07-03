# Auto open Chrome browser:

```py
# libraries import karein
import chromedriver_autoinstaller
from selenium import webdriver

# ChromeDriver auto-install kareinga
# (apne aap version match kar lega)
chromedriver_autoinstaller.install()

# Yeh bridge hai aapke code aur browser ke beech mein.
# Driver hi browser ko commands bhejta hai.
driver = webdriver.Chrome()

# is ULR ko open karayga
driver.get("https://www.google.com")
```

# WebElement:
1. Website ka har ek clickable, typeable, ya visible part ek **WebElement** hai.
    - 🔍 Google ka search box
    - 🔘 Login button
    - 📝 Input field (email, password)
    - 🔗 Links
    - 🖼️ Images
    - 📋 Dropdown menus
    - ✅ Checkboxes

```py
from selenium.webdriver.common.by import By

# Yeh sab WebElements hain
search_box = driver.find_element(By.NAME, "q")        # WebElement
login_button = driver.find_element(By.ID, "login")    # WebElement
heading = driver.find_element(By.TAG_NAME, "h1")      # WebElement
```

# By Locators:
1. By batata hai ke element ko kaisa dhundhna hai (ID se, class se, name se, etc.)
2. By aik Locator hai jiska main purpose hai Attributes ko find karna
3. total **8 locators** hote hai selenium mein

    - **By locators** = aik helper jo attribute ko find karne mein madaad karta hai.
    - **ID, NAME, CLASS** = Attributes (Properties) hai.
    - **By locators** se attributes ko find karte hain.

```py
from selenium.webdriver.common.by import By

By.ID                  # id attribute se
By.NAME                # name attribute se
By.CLASS_NAME          # class name se
By.TAG_NAME            # tag name se (div, input, button, etc.)
By.CSS_SELECTOR        # CSS selector se
By.XPATH               # XPath se (most powerful)
By.LINK_TEXT           # link text se
By.PARTIAL_LINK_TEXT   # link text ka kuch hissa se
```

--- 

# Example 01:

| Import | Aasan Lafz | Kis Kaam aata hai? |
| :--- | :--- | :--- |
| `chromedriver_autoinstaller` | **Driver Installer** | ChromeDriver khud download karna |
| `webdriver` | **Remote** | Browser kholna aur band karna |
| `By` | **Address Book** | Element dhoondne ka tareeqa batana |
| `Keys` | **Keyboard** | Enter, Backspace jaise dabana |
| `WebDriverWait` | **Waiter/Alarm** | Element aane ka intezar karna |
| `EC` | **Shart/Checker** | Waiter ko batana *kis* cheez ka intezar hai |

---

```py
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# automatic chromeDriver download karta hai 
chromedriver_autoinstaller.install()

# yah chrome ko commands bhejne ka liya use hota hai like open , close etc
driver = webdriver.Chrome()

# jo open karna hai oisa link
driver.get("https://www.google.com")

# jabtak isko q webElement se kch nhe milta yeah 10 seconds tak wait karayga 
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# searc_box mein jo window milayge yah wo box hai
search_box.send_keys("Selenium WebDriver")

# yeah ois box mein type karega "Selenium WebDriver"
search_box.send_keys(Keys.RETURN)

# Search results ke aane tak wait (max 20 sec) – results wala div (id="search") dikhna chahiye
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
)

# Pehla result jo heading (h3) mein dikhta hai, use dhundhte hain
first_result = driver.find_element(By.CSS_SELECTOR, "div#search h3")

# Pehle result ka text print karte hain
print("Robot ka jawab:", first_result.text)

# Browser band karne se pehle user se Enter press karwate hain, taake result dekh sakein
input("Browser band karna hai toh Enter dabayein...")
driver.quit()
```

# Major Imports:

```py
# ChromeDriver apne aap download karta hai, version ki khud se select hota hai.
import chromedriver_autoinstaller

# isa humera browser programmatically controlled hota hai
from selenium import webdriver

# Element dhundhne ke tareeqe, jaise By.ID, By.XPATH waghaira.
from selenium.webdriver.common.by import By

# Keyboard ki special keys (ENTER, TAB) bhejne ke liye.
from selenium.webdriver.common.keys import Keys

# Element ke liye wait karna, taki page load ho jaaye.
from selenium.webdriver.support.ui import WebDriverWait

# Wait ke saath condition dena, jaise "element dikhne tak ruko".
from selenium.webdriver.support import expected_conditions as EC

# Bot detection se bachne ke liye browser ko chhupata hai (anti-bot).
from selenium_stealth import stealth

# Mouse se hover, double-click, drag & drop ke liye.
from selenium.webdriver.common.action_chains import ActionChains

# <select> wale dropdown ki value choose karne ke liye.
from selenium.webdriver.support.select import Select

# Jab element na mile ya wait timeout ho jaye, test fail na ho isliye error handle karne ke liye.
from selenium.common.exceptions import NoSuchElementException, TimeoutException
```