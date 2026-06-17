# print(
# """
# 1. from sklearn.model_selection import train_test_split
#     - train_test_split Yeh Scikit-learn ki woh scissor hai jo aap ke poore data ko do hisson mein divide kar deti hai:
#     - Aik hissa padhai ke liye (Train Data)
#     - Aik hissa exam ke liye (Test Data).

# 2. X - Experience or Y - Salary

#     - X ko double brackets [[1]] mein is liye likha hai kyunke Scikit-learn ko X hamesha ek table/matrix ki form    mein chahiye hota hai.
    
# 3. test_size=0.2
#     - meri total rows hai 10 test_size-0.2 iska matlab hai ke 10 rows mein se 20% data cut kardu for testing purpose ka liya
#     - 10 rows ka 20% hota hai 2 rows. baaki 80% data training ka liya rekho.

#     - X_train: Padhai karne ke liye 8 logon ka Experience (8 rows).
#     - y_train: Padhai karne ke liye unhi 8 logon ki sahi Salary.
#     - X_test: Exam lene ke liye bache hue 2 logon ka Experience (Yeh model se chhupa kar rakha jayega).
#     - y_test: Un 2 logon ki asli Salary (Yeh answer sheet hai, jo end mein check hogi).

# 4. model = LinearRegression()
#     - aik blank model ready kiya

# 5. model.fit(X_train, y_train)
#     - ois Model ko Train kiya or oisa sikha diya

# 6. predictions = model.predict(X_test)
#     - ab model Predict karayga
# """
# )


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=124)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)