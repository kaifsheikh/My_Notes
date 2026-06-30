# What is Python?
1. Python ek programming language hai.
2. jisme hum computer ko instructions dete hain
3. taake wo koi kaam apne aap kare — jaise calculation, data handle karna, website banana, ya machine learning.

# How Python Work?


## Why python is Popular?

| 💡 Reason              | 📝 Explanation (Easy Words)                                   |
| ---------------------- | ------------------------------------------------------------- |
| **Easy to Learn**      | English jesi language hai, syntax simple hai.                 |
| **Powerful Libraries** | Har kaam ke liye ready-made tools milte hain (ML, web, data). |
| **Free & Open Source** | Sab ke liye free hai, koi license nahi chahiye.               |
| **Cross-Platform**     | Windows, Mac, Linux sab pe chalti hai.                        |
| **Huge Community**     | Millions log use karte hain — help milti hai har problem pe.  |

---

# Python Libraies:
1. Programming mein library ka matlab hota hai —
2. ready-made code ka collection jo kisi kaam ko aasaan banata hai.

## 🐍 `Python ki Famous Libraries`

| 🔢 **Category**      | 📚 **Library Name**    | 💡 **Simple Explanation (Easy Words)**                                                   | 🧠 **Main Use / Purpose**                     |
| -------------------- | ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Data Analysis**    | **pandas**             | Excel jesi library hai — data ko table (rows & columns) me store aur analyze karte hain. | Data ko read, clean, aur manage karna.        |
|                      | **numpy**              | Numbers aur calculations ke liye fast library hai.                                       | Maths aur scientific calculation karna.       |
| **Visualization**    | **matplotlib**         | Simple charts (bar, line, pie) banane ke liye.                                           | Data ko graph me dikhana.                     |
|                      | **seaborn**            | Matplotlib ka advanced version — colorful aur stylish graphs banata hai.                 | Beautiful charts aur statistics graphs.       |
| **Machine Learning** | **scikit-learn**       | Machine ko “seekhne” ke liye (prediction models).                                        | Simple Machine Learning models banana.        |
|                      | **tensorflow / keras** | Deep learning ke liye (AI projects).                                                     | AI, neural network, image/speech recognition. |
| **Web Development**  | **flask**              | Simple aur chhoti websites banane ke liye.                                               | Small web apps ya APIs create karna.          |
|                      | **django**             | Badi aur advanced websites ke liye.                                                      | Full web applications (e.g. Instagram type).  |
| **Automation**       | **selenium**           | Browser automate karta hai (auto open, click, search).                                   | Website pe kaam automatic karwana.            |
|                      | **pyautogui**          | Mouse aur keyboard control karta hai.                                                    | Desktop automation (auto click, typing).      |

---

### 💬 **Summary (Easy Words)**
- 🧾 **Pandas & NumPy:** Data handle aur calculate karne ke liye.  
- 📈 **Matplotlib & Seaborn:** Data ko graphs me dikhane ke liye.  
- 🤖 **Scikit-learn & TensorFlow:** Machine ko seekhne aur predict karne ke liye.  
- 🌐 **Flask & Django:** Website aur backend apps banane ke liye.  
- ⚙️ **Selenium & PyAutoGUI:** Computer aur browser ke kaam automate karne ke liye.

# What is Pip?
1. Package Installer for Python
2. Yani PIP ek tool hai jiska kaam hota hai Python ke extra packages (ya libraries) install karna.
3. Package ya library ka matlab hota hai — pehle se likha gaya Python code jo aap use kar sakte ho.

```py
1. python --version
2. py --list # yeah apko apke python ka saray version show karayge jo apne download kiya hua hai apne system mein
1. pip install package_name # Install karne ke liye
2. pip uninstall package_name # Package Uninstall karne ke liye
3. pip show package_name # Check karne ke liye ke package install hai ya nahi
4. pip list # List of installed packages dekhne ke liye
5. pip freeze > file_name.txt # isa hum Python ka jitne bhe packages jo Virtual Env mein yeah Global Python mein install hongay wo download hojaygay dosre file ka andar
6.  
```

# Virual Enviroment in Python
1. Python ka Virtual Environment aik “alag jagah” hoti hai jahan hum apne project ki libraries clean aur safe tareeqe se install karte hain.

```py
1. python -m venv my_env_name # Ye command naya virtual environment banati hai
2. my_env_name\Scripts\activate # is location per hum apne virtual Env ko ayse Activate karte hai
3. deactivate # isa Deactive hojayga 

# Activate karne ka bad hum sari Python ki Commands use kar sekhte hai jo Normally karte hai Install , List sub kch lakin Activate karne ka bad 
```

## Ager Python mein Different Version ho tu oin per work kaise kare. 

```py

1. py --version # isa sirf default version show hoga means new version

2. py --list # yeah apko apke python ka saray version show karayge ager apne multiple python version download kiya hue hai tu apne system mein

3. py -version_name --version # isa pura python version show hoga means ka 3.11.9 is terha se

4. py -version_name -m venv [Environment Ka Naam] # ager kisi specific python version mein Virtual Enviroment create karna ho tu yeah oiska liye hai 

5. py -version_name -m pip list # yeah apko apke kisi specific version mein kitne packages installed hai wo check karna ho tu oiska liya hai

6. py -version_name -m pip install [Package Name] # ager kisi specific python version mein package ko Install karna ho tu yeah oiska liye hai.

7. py -version_name -m pip uninstall [Package Name] # ager kisi specific python version mein se package ko delete karna ho tu yeah oiska liye hai
```