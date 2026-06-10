# Pass or Fail Logics

```py
import pandas as pd
import matplotlib.pyplot as plt

# 2D DataFrame
df = pd.DataFrame({
    'student': ['Ali','Bilal','Shayan','Smith','Karlie'],
    'score': [82, 45, 67, 90, 33],
    'age': [21,22,20,23,21]
})

# Make result column and add Pass or Fail
df.loc[df['score'] >= 50, 'result'] = 'Pass'
df.loc[df['score'] < 50, 'result'] = 'Fail'

# Alag-alag data frames
passed = df[df['result'] == 'Pass']
failed = df[df['result'] == 'Fail']

# Plot
plt.figure(figsize=(6,4))

# Bar charts – Store in Variables
bars_pass = plt.bar(passed['student'], passed['score'], color='green', label='Pass')
bars_fail = plt.bar(failed['student'], failed['score'], color='red', label='Fail')

# Pass Students Bar Values
for bar in bars_pass:
    height = bar.get_height()               
    x_center = bar.get_x() + bar.get_width()/2 
    
    plt.text(x_center, height, str(height),   
             ha='center', va='bottom',         
             fontsize=10, color='black')

# Fail Students Bar Values
for bar in bars_fail:
    height = bar.get_height()
    x_center = bar.get_x() + bar.get_width()/2

    plt.text(x_center, height, str(height),
             ha='center', va='bottom',
             fontsize=10, color='black')

# Middle Gray Line
plt.axhline(50, color='gray', linestyle='--')

# Show Mini Box
plt.legend()

# Headings
plt.title('Student Results')
plt.xlabel("Students Name")
plt.ylabel("Marks")

# Show
plt.show()
```

---

# Fail and pass with Advanced Version:

```py
import pandas as pd
import matplotlib.pyplot as plt

# 2D DataFrame
df = pd.DataFrame({
    'student': ['Ali','Bilal','Shayan','Smith','Karlie'],
    'score': [82, 45, 67, 90, 33],
    'age': [21,22,20,23,21]
})

# Make result column and add Pass or Fail
df.loc[df['score'] >= 50, 'result'] = 'Pass'
df.loc[df['score'] < 50, 'result'] = 'Fail'

# Alag-alag data frames
passed = df[df['result'] == 'Pass']
failed = df[df['result'] == 'Fail']

# Summary calculations
pass_count = len(passed)    
fail_count = len(failed)        
pass_marks = 50                   

# Plot
plt.figure(figsize=(6,4))

# Bar charts – Store in Variables
bars_pass = plt.bar(passed['student'], passed['score'], color='green', label='Pass')
bars_fail = plt.bar(failed['student'], failed['score'], color='red', label='Fail')

# Pass Students Bar Values
for bar in bars_pass:
    height = bar.get_height()               
    x_center = bar.get_x() + bar.get_width()/2 
    
    plt.text(x_center, height, str(height),   
             ha='center', va='bottom',         
             fontsize=10, color='black')

# Fail Students Bar Values
for bar in bars_fail:
    height = bar.get_height()
    x_center = bar.get_x() + bar.get_width()/2

    plt.text(x_center, height, str(height),
             ha='center', va='bottom',
             fontsize=10, color='black')

# Middle Gray Line
plt.axhline(pass_marks, color='gray', linestyle='--')

# Summary text box
summary_text = f"Pass Students: {pass_count}\nFail Students: {fail_count}\nPassing Marks: {pass_marks}"
# \n se nayi line aati hai

plt.text(0.95, 0.95, summary_text,               # x=0.95, y=0.95 (axes coordinates, 0 se 1)
         transform=plt.gca().transAxes,          # axes ke relative position
         fontsize=10,
         verticalalignment='top',                # box ke top ko y=0.95 par rakho
         horizontalalignment='right',            # box ke right edge ko x=0.95 par
         bbox=dict(boxstyle='round,pad=0.5',     # round corners, light padding
                   facecolor='lightyellow',       # Light yellow background
                   edgecolor='gray',              # border gray
                   alpha=0.9))                    # Light transparency

# Show Mini Box (legend)
plt.legend()

# Headings
plt.title('Student Results')
plt.xlabel("Students Name")
plt.ylabel("Marks")

# Show
plt.show()
```

---

# Pass or Fail Logics with CSV File

```py
import pandas as pd
import matplotlib.pyplot as plt
import sys

file_name = input("Enter CSV file Name here: ")

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"Error: '{file_name}' file not found.")
    sys.exit()

# Check karo ki zaroori columns hain ya nahi
required_cols = ['student', 'score']
for col in required_cols:
    if col not in df.columns:
        print(f"Error: in CSV '{col}' column not found.")
        sys.exit()

# ---- Threshold lena ----
pass_threshold = float(input("Enter Passing Marks"))

# ---- Pass/Fail add Category
df.loc[df['score'] >= pass_threshold, 'result'] = 'Pass'
df.loc[df['score'] < pass_threshold, 'result'] = 'Fail'

# ---- Filtering ----
passed = df[df['result'] == 'Pass']
failed = df[df['result'] == 'Fail']

# ---- Plotting (automated) ----
plt.figure(figsize=(8, 5))

bars_pass = plt.bar(passed['student'], passed['score'], color='green', label='Pass')
bars_fail = plt.bar(failed['student'], failed['score'], color='red', label='Fail')

# Pass Students bar Values 
for bar in bars_pass:
    height = bar.get_height()
    x_center = bar.get_x() + bar.get_width()/2
    plt.text(x_center, height, str(height), ha='center', va='bottom', fontsize=9)

# Fail Students bar Values 
for bar in bars_fail:
    height = bar.get_height()
    x_center = bar.get_x() + bar.get_width()/2
    plt.text(x_center, height, str(height), ha='center', va='bottom', fontsize=9)

# Threshold line
plt.axhline(pass_threshold, color='gray', linestyle='--', label=f'Passing ({pass_threshold})')

# Show Mini Box
plt.legend()

# Headings
plt.title('Student Results from CSV')
plt.xlabel('Student Name')
plt.ylabel('Marks')

# Rotate X Axis Name
plt.xticks(rotation=45)
plt.tight_layout()

# SHow
plt.show()
```