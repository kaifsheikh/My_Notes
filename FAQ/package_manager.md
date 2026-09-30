# `PIP` : Python Package Manager

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

---

# NPM - Nodejs Package Manager:
1. **npm = Node Package Manager**
2. Ye Node.js ecosystem ka **package manager** hai.
3. Node.js ke packages/libraries install aur manage karta hai

# 1. Packages installation:

```powershell
# npm package installation process:
npm install package_name
npm i package_name

# install multiple Packages in ones:
npm install package_name package_name package_name 

# Agar exact version chahiye: 
npm install package_name@1.7.9
npm install package_name@5.1.0

# Package update karna:
npm update axios

# Package remove/uninstall karna:
npm uninstall package_name
npm remove package_name

# package ko globally install karna ho:
npm install -g package_name
npm i -g package_name

# Global package remove karna ho:
npm uninstall -g cline
npm remove -g cline

# Global packages ki list dekhne ho:
npm list -g --depth=0

# Current project folder ke packages dekhna ho:
npm list --depth=0

# npm global packages kis folder mein hain yeah check karne ka liya:
npm root -g

# Current project ka node_modules location dekhna ho:
npm root

# agar dekhna ho ke global packages actually kahan install ho rahe hain.
npm prefix -g

# kisi package ka new version check karna ho sirf:
npm view cline version

```