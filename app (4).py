import streamlit as st
import joblib

# Load model
model = joblib.load('model.pkl')

st.title("Insurance Premium Cost Predictor")

# Collect user input
age = st.slider("Age", 18, 100)
bmi = st.slider("BMI", 15.0, 40.0)
smoker = st.selectbox("Do you smoke?", ["Yes", "No"])
smoker_flag = 1 if smoker == "Yes" else 0

# Only use the 3 features the model was trained on
input_data = [[age, bmi, smoker_flag]]

# Predict
if st.button("Predict Premium"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Premium: ₹ {round(prediction, 2)}")
