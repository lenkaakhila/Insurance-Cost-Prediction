import streamlit as st
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Insurance Premium Estimator")

age = st.slider("Select Age", 18, 100)
bmi = st.number_input("Enter BMI")
smoker = st.radio("Smoker", ["Yes", "No"])
children = st.number_input("Number of Children", 0, 5, step=1)

if st.button("Estimate Premium"):
    smoker_flag = 1 if smoker == "Yes" else 0
    prediction = model.predict([[age, bmi, smoker_flag, children]])
    st.success(f"Estimated Premium: ₹ {prediction[0]:,.0f}")


