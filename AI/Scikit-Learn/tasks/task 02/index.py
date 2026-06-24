import pandas as pd
import numpy as np
import warnings
# Un zaroori warnings ko chupane ke liye (Jo screen par aa rahi thin)
warnings.filterwarnings("ignore", category=UserWarning)

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# 1. CSV file load kiya
df = pd.read_csv('./data.csv')

# 2. Income text ko number mein badla
income_encoder = LabelEncoder()
df['Source_of_Income_Encoded'] = income_encoder.fit_transform(df['Source_of_Income'])

# 🌟 NAYI APGRADE: Ab hum training mein Budget (Car Price) ko bhi daal rahe hain!
# Inputs (X) mein ab 3 cheezein hain: [Salary, Income Source, Car Price]
X = df[['Min_Salary_Needed_Lakhs', 'Source_of_Income_Encoded', 'Car_Price_Lakhs']]
y_car = df['Car_Company']
y_class = df['Target_Customer_Type']

# 3. Data ko scale kiya
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. AI Models ko train kiya
model_car = KNeighborsClassifier(n_neighbors=1)
model_car.fit(X_scaled, y_car)

model_class = KNeighborsClassifier(n_neighbors=1)
model_class.fit(X_scaled, y_class)

# --- LIVE USER INPUT SCREEN ---
print("=========================================")
print("   WELCOME TO AI CAR RECOMMENDATION SYSTEM  ")
print("=========================================\n")

salary_input = float(input("Apni Monthly Salary likhein (Lakhs mein, e.g., 5.7): "))
budget_input = float(input("Car khareedne ka Total Budget likhein (Lakhs mein, e.g., 79): "))

print("\nSource of Income select karein:")
print(" - Job (Salary)")
print(" - Business")
print(" - Business / Job")
source_input = input("\nApna Source of Income enter karein: ")

# --- AI PREDICTION LOGIC ---
try:
    source_encoded = income_encoder.transform([source_input])[0]
    
    # 🌟 NAYI LOGIC: Naye customer ke data mein budget bhi daal diya
    # [Salary, Source, Budget]
    naya_customer = [[salary_input, source_encoded, budget_input]]
    
    # DataFrame banaya taake feature names ki warning khatam ho jaye
    naya_customer_df = pd.DataFrame(naya_customer, columns=['Min_Salary_Needed_Lakhs', 'Source_of_Income_Encoded', 'Car_Price_Lakhs'])
    naya_customer_scaled = scaler.transform(naya_customer_df)
    
    # AI ne teenon cheezon ko dekh kar car predict ki
    predicted_car = model_car.predict(naya_customer_scaled)[0]
    predicted_category = model_class.predict(naya_customer_scaled)[0]
    
    # CSV se us car ki actual details nikali
    car_info = df[df['Car_Company'] == predicted_car].iloc[0]
    actual_car_price = car_info['Car_Price_Lakhs']
    min_salary_required = car_info['Min_Salary_Needed_Lakhs']
    
    print("\n================ AI DECISION ================")
    
    # Pehle check karein ke kahin salary hi bilkul kam toh nahi
    if salary_input < 0.4:
        print("❌ Sorry! Aapki salary boht kam hai. Humari list mein koi bhi car nahi aati.")
        
    # Agar AI ne jo car dhoondi, woh user ke budget se barri nikal aayi
    elif budget_input < actual_car_price:
        # 🌟 BACKUP LOGIC: Agar AI phir bhi galti kare, toh pure CSV mein se budget ke andar wali sasti car nikaal lo!
        sasti_cars = df[(df['Car_Price_Lakhs'] <= budget_input) & (df['Min_Salary_Needed_Lakhs'] <= salary_input)]
        
        if not sasti_cars.empty:
            # Sab se behtareen aur mehngi car jo budget ke andar ho
            best_car = sasti_cars.sort_values(by='Car_Price_Lakhs', ascending=False).iloc[0]
            print(f"✅ Haalraat! Aapke budget ke mutabiq car mil gayi hai.")
            print(f"🚗 Recommended Car: {best_car['Car_Company']}")
            print(f"💰 Car Ki Actual Price: {best_car['Car_Price_Lakhs']} Lakhs")
            print(f"📊 Aapki Customer Category: {best_car['Target_Customer_Type']}")
        else:
            print(f"❌ Sorry! Aapka budget {budget_input} Lakh hai, par is price mein koi car aapki salary requirement se match nahi kar rahi.")
            
    else:
        # Agar AI ki batayi hui car bilkul budget ke andar fit baithi
        print(f"✅ Mubarak Ho! Aap bilkul yeh car khareed sakte hain.")
        print(f"🚗 Recommended Car: {predicted_car}")
        print(f"💰 Car Ki Actual Price: {actual_car_price} Lakhs")
        print(f"📊 Aapki Customer Category: {predicted_category}")
        
    print("=========================================")

except ValueError:
    print("\n❌ Galat Input! Jaisa likha hai bilkul waisa hi type karein.")