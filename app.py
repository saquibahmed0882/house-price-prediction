import streamlit as st
import joblib
import numpy as np


# Load trained model
model = joblib.load("house_price_model.pkl")

# User Inputs

bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=0.0, max_value=10.0, value=2.0)

sqft_living = st.number_input("Living Area (sqft)", min_value=100, value=2000)

sqft_lot = st.number_input("Lot Area (sqft)", min_value=100, value=5000)

floors = st.number_input("Floors", min_value=1.0, max_value=5.0, value=1.0)

waterfront = st.selectbox("Waterfront", [0, 1])

view = st.number_input("View", min_value=0, max_value=4, value=0)

condition = st.number_input("Condition", min_value=1, max_value=5, value=3)

grade = st.number_input("Grade", min_value=1, max_value=13, value=7)

sqft_above = st.number_input("Sqft Above", min_value=100, value=1500)

sqft_basement = st.number_input("Sqft Basement", min_value=0, value=0)

yr_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)

yr_renovated = st.number_input("Year Renovated", min_value=0, value=0)


# Prediction button

if st.button("Predict Price"):

    input_data = np.array([[bedrooms,
                            bathrooms,
                            sqft_living,
                            sqft_lot,
                            floors,
                            waterfront,
                            view,
                            condition,
                            grade,
                            sqft_above,
                            sqft_basement,
                            yr_built,
                            yr_renovated]])

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")