import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Streamlit UI
st.title("🏥 Insurance Premium Cost Predictor")

st.markdown("Enter the following details to estimate your health insurance premium:")

# Input fields
age = st.slider("Age", 18, 100, step=1)
bmi = st.slider("BMI (Body Mass Index)", 15.0, 45.0, step=0.1)
smoker = st.radio("Do you smoke?", ("Yes", "No"))
smoker_flag = 1 if smoker == "Yes" else 0

# Make prediction
if st.button("Predict Premium"):
    input_data = [[age, bmi, smoker_flag]]  # Must match training features!
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Premium: ₹ {round(prediction, 2)}")

