# Example 01:

1. > ### yeah script sirf `wikipedia` ki Website ko open karayge 5 seconds ka liya

```py
import chromedriver_autoinstaller
from selenium import webdriver

# ChromeDriver apne aap set ho jayega
chromedriver_autoinstaller.install()

# Chrome browser start karo
driver = webdriver.Chrome()

# Website kholo
driver.get("https://www.wikipedia.org")

# 5 second ruko, taake dekh sakein
import time
time.sleep(5)

# Browser band karo
driver.quit()
print("Browser Closed!")
```

# Example 02:

1. > ### yeah script wikipedia ka searchbox per world war 2 search karke dega.

```py
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome driver auto setup
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Wikipedia kholo
driver.get("https://www.wikipedia.org")
driver.maximize_window()

# 1. Search box ko clickable hone tak wait karo, phir type karo
search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchInput")))
search_box.send_keys("world war 2")

# 2. Search button ko clickable hone tak wait karo, phir click karo
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
search_button.click()

input("show to Enter")
driver.quit()
```

# Example 03:

1. > ### auto form filler

```py
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
import random
import string
import time 

# Setup
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.roboform.com/filling-test-all-fields")
driver.maximize_window()

# ---- Helper Functions ----
def rand_str(n=8): return ''.join(random.choices(string.ascii_letters, k=n))
def rand_num(n=6): return ''.join(random.choices(string.digits, k=n))
def rand_email(): return f"{rand_str(5)}@example.com"

# Slow typing function
def slow_type(element, text, delay=0.1):
    """Ek-ek character type karega, beech mein delay ke saath"""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # second mein delay (0.1 = 100ms)
# --------------------------

# Ab sab jagah slow_type() use karo, send_keys() ki jagah
# Left side text inputs
slow_type(driver.find_element(By.NAME, "01___title"), random.choice(["Mr.", "Mrs.", "Ms."]))
slow_type(driver.find_element(By.NAME, "02frstname"), rand_str(6))
slow_type(driver.find_element(By.NAME, "03middle_i"), random.choice(string.ascii_uppercase))
slow_type(driver.find_element(By.NAME, "04lastname"), rand_str(8))
slow_type(driver.find_element(By.NAME, "04fullname"), rand_str(6) + " " + rand_str(7))
slow_type(driver.find_element(By.NAME, "05_company"), rand_str(8) + " Inc.")
slow_type(driver.find_element(By.NAME, "06position"), random.choice(["Manager", "Developer"]))
slow_type(driver.find_element(By.NAME, "10address1"), rand_num(3) + " " + rand_str(6) + " St.")
slow_type(driver.find_element(By.NAME, "11address2"), "Apt " + rand_num(2))
slow_type(driver.find_element(By.NAME, "13adr_city"), rand_str(7))
slow_type(driver.find_element(By.NAME, "14adrstate"), rand_str(2).upper())
slow_type(driver.find_element(By.NAME, "15_country"), random.choice(["India", "USA"]))
slow_type(driver.find_element(By.NAME, "16addr_zip"), rand_num(5))
slow_type(driver.find_element(By.NAME, "20homephon"), rand_num(10))
slow_type(driver.find_element(By.NAME, "21workphon"), rand_num(10))
slow_type(driver.find_element(By.NAME, "22faxphone"), rand_num(10))
slow_type(driver.find_element(By.NAME, "23cellphon"), rand_num(10))
slow_type(driver.find_element(By.NAME, "24emailadr"), rand_email())
slow_type(driver.find_element(By.NAME, "25web_site"), "https://www." + rand_str(5) + ".com")

# Right side text inputs
slow_type(driver.find_element(By.NAME, "30_user_id"), rand_str(8))
slow_type(driver.find_element(By.NAME, "31password"), rand_str(10))
slow_type(driver.find_element(By.NAME, "41ccnumber"), rand_num(16))
slow_type(driver.find_element(By.NAME, "43cvc"), rand_num(3))
slow_type(driver.find_element(By.NAME, "44cc_uname"), rand_str(6) + " " + rand_str(5))
slow_type(driver.find_element(By.NAME, "45ccissuer"), random.choice(["HDFC", "ICICI"]))
slow_type(driver.find_element(By.NAME, "46cccstsvc"), rand_num(10))
slow_type(driver.find_element(By.NAME, "60pers_sex"), random.choice(["Male", "Female"]))
slow_type(driver.find_element(By.NAME, "61pers_ssn"), rand_num(9))
slow_type(driver.find_element(By.NAME, "62driv_lic"), rand_str(8).upper())
slow_type(driver.find_element(By.NAME, "66pers_age"), str(random.randint(18, 65)))
slow_type(driver.find_element(By.NAME, "67birth_pl"), rand_str(7))
slow_type(driver.find_element(By.NAME, "68__income"), str(random.randint(20000, 150000)))
slow_type(driver.find_element(By.NAME, "71__custom"), "Custom: " + rand_str(4))
slow_type(driver.find_element(By.NAME, "72__commnt"), "Comment: " + rand_str(10))

# Dropdowns (yahan send_keys nahi, Select hi use hoga, kyunki dropdown hai)
Select(driver.find_element(By.NAME, "40cc__type")).select_by_index(random.randint(1, 5))
Select(driver.find_element(By.NAME, "42ccexp_mm")).select_by_index(random.randint(1, 12))
Select(driver.find_element(By.NAME, "43ccexp_yy")).select_by_index(random.randint(1, 18))
Select(driver.find_element(By.NAME, "66mm")).select_by_index(random.randint(1, 12))
Select(driver.find_element(By.NAME, "67dd")).select_by_index(random.randint(1, 31))
Select(driver.find_element(By.NAME, "68yy")).select_by_index(random.randint(1, 110))

time.sleep(2)  # Bharra hua form dekhne ke liye thoda wait
reset_btn = driver.find_element(By.CSS_SELECTOR, "input[type='reset']")
reset_btn.click()
print("🔄 Reset button click ho gaya! Saare fields khali ho gaye.")

input("Browser band karne ke liye Enter dabao...")
driver.quit()
```