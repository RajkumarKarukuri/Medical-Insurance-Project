import streamlit as st
import joblib
import pandas as pd

# Load artifacts
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("best_model.pkl")

# Streamlit UI
st.title("🏥 Medical Insurance Expense Predictor")

st.markdown("Enter patient details to predict medical expenses.")

# Input fields
age = st.number_input("Age", min_value=0, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Predict button
if st.button("Predict Expenses"):
    # Prepare input data
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # Preprocess
    X_processed = preprocessor.transform(input_data)

    # Prediction
    prediction = model.predict(X_processed)[0]

    st.success(f"💰 Estimated Medical Expenses: ${prediction:,.2f}")
