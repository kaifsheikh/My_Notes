import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('./youtube_data.csv')

# 'Age' column ko X mein daal diya
X = df[['Age']] 

# 'Preference' column ko Y mein daal diya
y = df['Preference']

# KNeighborsClassifier – ye ek machine learning algorithm hai jise K-Nearest Neighbors (KNN) kehte hain. Ye naye data point ki category predict karne ke liye uske sabse qareebi (nearest) data points ko dekhta hai.

# n_neighbors=2 – iska matlab hai ke jab bhi kisi naye user ki age aegi, to model sirf 2 sabse qareebi purane users ki preferences dekh kar faisla karega. Jaise, agar aapki age 25 hai, to model aapki age ke aas-paas ki 2 mojooda entries dhundega aur unki Preference dekh kar batayega ke aapko gaming pasand aegi ya news.
model = KNeighborsClassifier(n_neighbors=2)

# Model ko train kardiya oisa sikha diya
model.fit(X, y)

# function Jo user se input lega
def get_user_recommendation():
    user_age = input("Enter your Age: ")
    user_age = int(user_age)
    
    # Scikit-learn ko data hamesha double brackets [[ ]] mein chahiye hota hai
    formatted_input = pd.DataFrame([[user_age]], columns=['Age'])
    
    # Model se prediction lena
    prediction = model.predict(formatted_input)
    
    # Conditions Base result
    if prediction[0] == 1:
        print(f" your age is {user_age} so recommended you: 🎮 GAMING VIDEOS!")
    else:
        print(f" your age is {user_age} so recommended you: 📰 LIVE NEWS!")

# Function callback
get_user_recommendation()