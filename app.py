import streamlit as st
import joblib
import numpy as np



st.set_page_config(
    page_title="House Price Prediction App",
    page_icon="🏠",
    layout="wide"
)



model = joblib.load("house_price_model.pkl")



st.title("🏠 House Price Prediction App")

st.markdown("""
### Developed by **Saquib Ahmed**
**B.Tech Artificial Intelligence & Machine Learning**

This application uses Machine Learning to predict house prices
based on property features using a Random Forest Regression model.
""")

st.divider()



st.sidebar.title("📌 Project Information")

st.sidebar.markdown("""
### House Price Prediction

**Developer:**  
Saquib Ahmed

**Model Used:**  
Random Forest Regression

**Dataset:**  
King County House Sales Dataset

**Technologies:**
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

**Performance:**

R² Score: 0.68

Mean Absolute Error:
127681
""")



st.subheader("🏡 Enter House Details")


col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=10,
        value=3
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        max_value=10.0,
        value=2.0
    )

    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=100,
        value=2000
    )

    sqft_lot = st.number_input(
        "Lot Area (sqft)",
        min_value=100,
        value=5000
    )


with col2:
    floors = st.number_input(
        "Floors",
        min_value=1.0,
        max_value=5.0,
        value=1.0
    )

    grade = st.number_input(
        "Grade",
        min_value=1,
        max_value=13,
        value=7
    )

    yr_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    yr_renovated = st.number_input(
        "Year Renovated",
        min_value=0,
        value=0
    )


waterfront = st.selectbox(
    "Waterfront",
    [0,1]
)

view = st.number_input(
    "View",
    min_value=0,
    max_value=4,
    value=0
)

condition = st.number_input(
    "Condition",
    min_value=1,
    max_value=5,
    value=3
)

sqft_above = st.number_input(
    "Sqft Above",
    min_value=100,
    value=1500
)

sqft_basement = st.number_input(
    "Sqft Basement",
    min_value=0,
    value=500
)




if st.button("🔮 Predict House Price"):

    input_data = np.array([[
        bedrooms,
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
        yr_renovated
    ]])

    prediction = model.predict(input_data)

    st.success(
        f"🏠 Estimated House Price: ${prediction[0]:,.2f}"
    )

    st.balloons()