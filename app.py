import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("marksModel.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Grade Prediction System")
st.write("Linear Regression Deployment (Inference Only)")

hours = st.number_input(
    "Enter Hours Studied",
    min_value=0.0,
    max_value=15.0,
    step=0.5
)

if st.button("Predict"):
    grade = model.predict(np.array([[hours]]))[0]

    status = "Pass" if grade >= 70 else "Fail"

    if grade >= 90:
        result = "A"
    elif grade >= 80:
        result = "B"
    elif grade >= 70:
        result = "C"
    else:
        result = "D"

    st.success(f"Predicted Grade: {grade:.2f}")
    st.info(f"Status: {status}")
    st.warning(f"Result: {result}")
