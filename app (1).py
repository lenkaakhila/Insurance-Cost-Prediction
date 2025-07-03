import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("Insurance Premium Estimator")

# Input fields
age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
smoker = st.selectbox("Are you a smoker?", ['Yes', 'No'])
children = st.slider("Number of children", 0, 5, 1)

# Input transformation
input_data = np.array([[age, bmi, 1 if smoker == 'Yes' else 0, children]])

# Prediction
prediction = model.predict(input_data)[0]
st.subheader(f"Estimated Premium: ₹{prediction:,.2f}")
