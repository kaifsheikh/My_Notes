from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

app = Flask(__name__)

# --- Load data ---
if not os.path.exists('data.csv'):
    raise FileNotFoundError("data.csv not found!")

df = pd.read_csv('data.csv')

# 🔥 1. EXACT MATCH DICTIONARY (100% accurate for known places)
exact_lookup = df.set_index('nearest_place')['city'].to_dict()
print("✅ Exact lookup ready with", len(exact_lookup), "entries")

# --- Train ML Model (for unseen/partial inputs) ---
def train_model():
    X = df[['nearest_place', 'postal_code']]
    y = df['city']

    # Text features: Word n-grams, sab unique words rakhein
    text_processor = TfidfVectorizer(
        analyzer='word',
        ngram_range=(1, 2),
        lowercase=True,
        stop_words='english',
        max_features=None          # "Lalamusa" jaise rare words ko mat girayen
    )

    # 🔥 2. NUMERIC FIX: Missing postal code ko MEDIAN se fill karein ( -1 nahi)
    numeric_processor = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),  # <--- YAHAN CHANGE
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer([
        ('text', text_processor, 'nearest_place'),
        ('num', numeric_processor, ['postal_code'])
    ])

    # High C (100) takay rare words (Lalamusa) ka weight zyada ho
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(
            max_iter=1000,
            C=100,
            class_weight='balanced',
            random_state=42
        ))
    ])

    model.fit(X, y)
    print("✅ ML Model trained successfully!")
    return model

# Load model
try:
    ai_pipeline = train_model()
except Exception as e:
    print(f"❌ Error: {e}")
    ai_pipeline = None

# --- Flask Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if ai_pipeline is None:
        return jsonify({'error': 'Model not loaded'}), 500

    data = request.json
    nearest_place = data.get('nearest_place', '').strip()
    postal_code = data.get('postal_code', '').strip()

    if not nearest_place:
        return jsonify({'error': 'Nearest Place is required'}), 400

    # 🚀 STEP 1: EXACT MATCH (Postal code ki zaroorat nahi, 100% sahi)
    if nearest_place in exact_lookup:
        return jsonify({
            'predicted_city': exact_lookup[nearest_place],
            'confidence': 100.0,
            'method': '✅ Exact Match'
        })

    # STEP 2: ML Prediction (Unseen places ke liye)
    # 🔥 IMPORTANT: Agar postal code nahi diya, toh NaN bhejo (Median imputer khud handle karega)
    postal_code_val = np.nan
    if postal_code:
        try:
            postal_code_val = int(postal_code)
        except ValueError:
            postal_code_val = np.nan  # Agar kuch aur likha (jaise 'abc') toh NaN

    input_df = pd.DataFrame([{
        'nearest_place': nearest_place,
        'postal_code': postal_code_val
    }])

    try:
        prediction = ai_pipeline.predict(input_df)[0]
        proba = ai_pipeline.predict_proba(input_df)[0].max()

        return jsonify({
            'predicted_city': prediction,
            'confidence': round(proba * 100, 2),
            'method': '🤖 ML Prediction'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)