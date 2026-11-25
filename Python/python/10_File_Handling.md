# What is File Handling?
File handling ek process hai jisme hum kisi file ko open karte hain, usme kuch padhte ya likhte hain, aur kaam khatam hone par file ko close kar dete hain. Python mein built-in functions aur keywords ise bahut easy banate hain.

---

# Purpose:
1. **Data Permanent Rakhna**: Program band hone par bhi data file mein save rehta hai (jaise user settings, game progress).
2. **Bade Data Ke Saath Kaam**: Agar bahut saara data hai, to use memory mein rakhne ki jagah file se line-by-line padhna efficient hota hai.
3. **Multiple Programs Ke Beech Data Share Karna**: Ek program file mein likhe, doosra program use padh sakta hai.
4. **Logs aur Reports Generate Karna**: Jaise error logs, student reports, etc.
5. **Input/Output Operations**: User se input lekar file mein save karna ya file se data dikhana.

---

### 🔹 File Handling Ke 3 Basic Steps
1. **File Open Karna** – `open()` function se.
2. **Read/Write Operation Karna** – padhna ya likhna.
3. **File Close Karna** – `close()` method se.

---

### 🔹 `open()` Function – File Open Karna
```python
file_object = open("file_name.txt", "mode")
```
- `"file_name.txt"` – file ka naam (path ke saath bhi de sakte hain).
- `"mode"` – file kholne ka tareeka (read, write, append, etc.).

**Common Modes:**

| Mode | Purpose (Kaam) |
|------|----------------|
| `'r'` | Sirf padhne ke liye (default). File exist karni chahiye, nahi to error. |
| `'w'` | Sirf likhne ke liye. Agar file exist karti hai to purana data delete hoga, nahi to nayi file banegi. |
| `'a'` | Append (jor) karne ke liye. File ke end mein naya data jodta hai, purana data safe rehta hai. |
| `'x'` | Create mode – sirf nayi file banane ke liye, agar file pehle se hai to error. |
| `'r+'` | Padhna aur likhna dono. File exist karni chahiye. |
| `'w+'` | Padhna aur likhna dono. Purana data delete hoga, nayi file agar nahi hai to banegi. |
| `'a+'` | Append aur padhna dono. File end se likhta hai. |

Binary files (images, PDF) ke liye `'b'` jod do: `'rb'`, `'wb'`, etc.

---

# File (Reading)

#### 1. `read()` – Poori file ek string mein padhna
```python
f = open("sample.txt", "r")
content = f.read()
print(content)
f.close()
```

#### 2. `read(n)` – Sirf `n` characters padhna
```python
f = open("sample.txt", "r")
print(f.read(10))  # pehle 10 characters
f.close()
```

#### 3. `readline()` – Ek line (enter tak) padhna
```python
f = open("sample.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1, line2)
f.close()
```

#### 4. `readlines()` – Poori file ki lines ki list
```python
f = open("sample.txt", "r")
lines = f.readlines()  # ['line1\n', 'line2\n', ...]
for line in lines:
    print(line.strip())
f.close()
```

---

### 🔹 File Mein Likhna (Writing)

#### 1. `write()` – String likhna
```python
f = open("output.txt", "w")
f.write("Hello, duniya!\n")
f.write("Python seekh raha hoon.\n")
f.close()
```

#### 2. `writelines()` – List ki strings likhna
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
f = open("output.txt", "w")
f.writelines(lines)
f.close()
```

**Dhyan rakho:** `'w'` mode purana sab kuch mita kar naye sire se likhta hai. Agar purana data rakhna hai aur aage jodna hai to `'a'` (append) mode use karo.

---

### 🔹 Append Mode – Purane Data Ke Aage Jodna
```python
f = open("log.txt", "a")
f.write("Naya error entry\n")
f.close()
```

---

### 🔹 `with` Statement – Automatic File Close Karna (Best Practice)
`with` block se file automatically close ho jaati hai, chahe error aaye ya na aaye. `close()` manually likhne ki zaroorat nahi.

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# yahan f.close() automatic call ho jaata hai
```

Isi tarah likhne ke liye:
```python
with open("info.txt", "w") as f:
    f.write("Secure way to write\n")
```

---

### 🔹 Complete Example: Student Records File Banayein aur Padhein
```python
# Step 1: Write student data
with open("students.txt", "w") as file:
    file.write("Rahul, 85\n")
    file.write("Priya, 92\n")
    file.write("Amit, 78\n")

# Step 2: Read and display all
print("Student Records:")
with open("students.txt", "r") as file:
    for line in file:          # file object ko directly iterate kar sakte hain
        name, marks = line.strip().split(", ")
        print(f"{name} ke marks: {marks}")
```

**Output:**
```
Student Records:
Rahul ke marks: 85
Priya ke marks: 92
Amit ke marks: 78
```

---

### 🔹 Error Handling – File Exist Na Ho To?
Agar file nahi milti to `FileNotFoundError` aata hai. `try-except` se handle karo:
```python
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili! Pehle file create karo.")
```

---

### 🔹 Important Points (Yaad Rakho)
- **Path**: Agar file current folder mein nahi hai to poora path do, jaise `"C:/Users/Name/Documents/file.txt"`.
- **Escape Characters**: Raw string `r"C:\folder\file.txt"` use karo taaki `\n` wagerah problem na karein.
- **Newline `\n`**: Text files mein line break ke liye `\n` use hota hai.
- **Binary Files**: Images, PDFs ke liye `'rb'` / `'wb'` modes with `read()` and `write()` (bytes handle karte hain).

---

### 🔹 Summary
- **File Handling** = open → read/write → close.
- Modes decide karte hain ki padhna hai, likhna hai ya append.
- `with open(...) as f:` is safest and cleanest.
- Real applications mein data files (TXT, CSV, JSON) se hi manage hota hai.

Ab tum simple log system, notes app, ya data logger asani se bana sakte ho. Kisi specific cheez mein aur detail chahiye to poocho!