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

