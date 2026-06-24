from sklearn.linear_model import LogisticRegression

# Maan lein X sugar level hai
# aur Y bimari ka stage 1 means sub theek hai
# ager 0 hua tu theek nhe hai
X = [[80], [90], [150], [180]]
y = [0, 0, 1, 1] 

# 2. Model ka object banaya
clf_model = LogisticRegression()

# 3. Model ko train kiya (Fit)
clf_model.fit(X, y)

# 4. Naye patient ka test kiya jiska sugar level 160 hai
prediction = clf_model.predict([[149]])

print(prediction)