# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv('insurance.csv')

# Feature engineering
df['BMI'] = df['Weight'] / (df['Height']/100) ** 2

# Select features and target
X = df[['Age', 'BMI', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants', 'ChronicDiseases',
        'KnownAllergies', 'HistoryOfCancerInFamily', 'NumberOfMajorSurgeries']]
y = df['PremiumPrice']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model to file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model.pkl")
