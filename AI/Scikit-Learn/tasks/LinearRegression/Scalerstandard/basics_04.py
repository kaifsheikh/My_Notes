from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# 1. Inputs (Features) - X
# Sq Ft High Scale hai (High Magnitude) means bara Number
# aur Rooms Low scale hai (Low Magnitude) means chota Number
X = [[1200, 2], [2500, 4], [3000, 5]]

# 2. Output (Target) - y (House Price Lakhs mein)
y = [60, 130, 160]

# 3. Data ko scale karne ke liye StandardScaler ka object banaya
scaler = StandardScaler()

# 4. Is line ne dono columns ka scale barabar kar diya (-3 se +3 ki range mein)
X_scaled = scaler.fit_transform(X)

# 5. Empty Linear Regression Model banaya
model = LinearRegression()

# 6. Model ko trained kiya (Sirf scaled data par)
model.fit(X_scaled, y)

# 4. Naya ghar jiski price maloom karni hai
new_house = [[10000, 12]]

# 5. Naye ghar ko purane scale ke mutabiq convert kiya
new_house_scaled = scaler.transform(new_house)

# 6. Model se price nikalwayi
predicted_price = model.predict(new_house_scaled)

print("New House Price: ", predicted_price[0], "Lakhs")