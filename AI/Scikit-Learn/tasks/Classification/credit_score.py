from sklearn.linear_model import LogisticRegression

# 1. Inputs (X): [Credit Score, Monthly Income]
X_train = [
    [750, 150000],  # Ali (Yes)
    [450, 40000],   # Bilal (No)
    [700, 120000],  # Sara (Yes)
    [500, 55000]    # Zain (No)
]

# 2. Labels (y): 1 matlab Yes, 0 matlab No
y_train = [1, 0, 1, 0]

# 3. Model ko banana aur train karna
model = LogisticRegression()
model.fit(X_train, y_train)  # Yahan computer ne patterns seekh liye

# New Data Credit Score = 710, Income = 135000
kamran_data = [[710, 135000]]

# 5. Model se prediction poochna
kamran_prediction = model.predict(kamran_data)

# 6. Jawab show karna
if kamran_prediction[0] == 1:
    print("AI Decision: LOAN APPROVED (YES)")
else:
    print("AI Decision: LOAN REJECTED (NO)")