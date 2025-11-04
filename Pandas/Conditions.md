```py
import pandas as pd

data = pd.DataFrame({
    "Name": [
        "Ali", "Sara", "Umar", "Hina", "Bilal",
        "Shayan", "Asma", "Usman", "Areeba", "Farhan",
        "Kiran", "Hassan", "Nadia", "Saad", "Tania",
        "Hamza", "Zara", "Imran", "Noor", "Ahmad"
    ],
    "Age": [
        22, 25, 28, 24, 30,
        27, 26, 29, 23, 32,
        31, 33, 24, 28, 25,
        29, 26, 27, 24, 30
    ],
    "Salary": [
        45000, 55000, 60000, 52000, 75000,
        68000, 64000, 70000, 48000, 80000,
        78000, 82000, 50000, 67000, 58000,
        73000, 62000, 65000, 54000, 77000
    ],
    "Performance_Score": [
        88, 92, 76, 81, 95,
        89, 85, 91, 80, 94,
        87, 90, 83, 88, 86,
        93, 84, 89, 82, 90
    ]
})

hight_salary = data.loc[ (data["Salary"] > 70000) & (data["Performance_Score"] > 90)]

print(hight_salary)

```


https://youtu.be/qrMnoY8qBJM?si=K8KR7zMCsASXnc5d&t=4048