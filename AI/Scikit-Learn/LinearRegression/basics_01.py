# print(
# """
# 1. Topic is : Multiple Linear Regression

#     - Regression: Matlab humein koi continuous number (value) predict karni hai.
#     - Linear: Matlab features aur target ke darmiyan ek seedha rishta (straight-line relationship) hai
#     - Multiple: Matlab prediction karne ke liye hamare paas ek feature nahi hai, balkay ek se zyada (multiple)   features hain.

# Jab hum ek se zyada input columns (Features) ki madad se kisi ek number (Target) ko predict karte hain, toh us model ko Multiple Linear Regression kehte hain.

# 2. Real Example:

#     - Farz karein aapko aik Ghar ki Price predict karni hai.Simple Linear Regression mein kya hota tha?
#     - Hum sirf ek feature lete thay (jaise ghar ka size).
#     - Lekin aam zindagi mein sirf size dekh kar price pata nahi chalti.
#     - Multiple Linear Regression mein hum aam zindagi ki tarah boht saare features ikthay dekhte hain jaise ka.

#         - Features X -> Size (Square Feet mein)
#         - Features X -> Numbers of Bedrooms
#         - Features X -> Age of House (Ghar kitna purana hai saalon mein)
    
#     - or Target Y -> Ghar ki Price yeh humera main target hai jo hume price ko predict karwana hai.

# 3. Sklearn Mein Iska Workflow Kaise Chalta Hai?

#     - Ab dekhein jo workflow humne pehle seekha tha, woh yahan coding mein kaise apply hota hai. Pandas aur NumPy ki madad se hum yeh steps karte hain:
# """    
# )

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [1000, 2, 5],   # Ghar 1: 1000 sqft, 2 rooms, 5 saal purana
    [1500, 3, 2],   # Ghar 2: 1500 sqft, 3 rooms, 2 saal purana
    [1200, 2, 10],  # Ghar 3: 1200 sqft, 2 rooms, 10 saal purana
    [2000, 4, 1]    # Ghar 4: 2000 sqft, 4 rooms, 1 saal purana
])

y = np.array([50, 80, 55, 120])

# 1. Khali model banaya
house_model = LinearRegression()

# 2. Model ko sikhaya (.fit)
house_model.fit(X, y)

# Naye ghar ke features ko hamesha 2D array [[ ]] mein dena hai
new_house = np.array([[1600, 3, 4]])

# Computer se prediction li
predicted_price = house_model.predict(new_house)

# point ke baad sirf 2 digits tak round karein
round_off = round(predicted_price[0], 2)

print(f"Is naye ghar ki estimated price hai: {round_off} Lakhs")