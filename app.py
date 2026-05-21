import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("student_model.pkl")

# Title
st.title("Student Math Score Predictor")

# Inputs
reading = st.number_input("Enter Reading Score")
writing = st.number_input("Enter Writing Score")

# Prediction button
if st.button("Predict"):

    data = np.array([[reading, writing]])

    prediction = model.predict(data)

    st.success(f"Predicted Math Score: {prediction[0]:.2f}")