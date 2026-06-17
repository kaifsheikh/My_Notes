from sklearn.linear_model import LinearRegression

# (X = Experience, y = Salary)
X = [[1], [2], [3]]  # Hamesha 2D array/list hoti hai
y = [30000, 40000, 50000]

# Model ka object banaya
model = LinearRegression()

# Model ko data fit kiya or model ne pattern seekh liya!
model.fit(X, y)  

# Naye bande ki salary predict ki jiska 5 saal ka experience hai
naya_experience = [[5]]
prediction = model.predict(naya_experience)

print(prediction)  # Output aayega: [70000]