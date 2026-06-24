# print("""

# - Hum computer ko sikhayenge ke "Kitne hours parhne se kitne marks aate hain
# - aur phir us se naye student ke marks predict karwayenge.

# - Yahan hamara Feature X hai Study Hours
# - Aur hamara Target Y hai Marks jo hum predict karengay.

# """)

import numpy as np
from sklearn.linear_model import LinearRegression

# X = Features -> Time Hours
X = np.array([ [2], [3], [4], [5], [6] ])

# y = Target -> Past Student Marks 
y = np.array([20, 40, 60, 80, 100])

# Ek khali model banaya (Abhi isko kuch nahi pata)
model = LinearRegression()

# Model ko data de kar sikhaya -> .fit() ka matlab hai data se "Sikho!"
model.fit(X, y)

# Naya data hamesha 2D array mein dena hota hai [[6]]
naya_student = np.array([ [1] ])

# predict() ka matlab hai ab -> "Jawab do!"
prediction = model.predict(naya_student)

print(f"if you study for {naya_student} hours your marks will be : {prediction[0]}")