import streamlit as st
import joblib
import numpy as np
import pandas as pd

from utils.currency import convert_currency
from utils.location import get_countries, get_states, get_cities
from utils.pdf_report import generate_pdf
from database.database import (
    create_database,
    create_user_table,
    save_prediction,
    get_predictions,
    register_user,
    login_user
)




st.set_page_config(
    page_title="House Price Prediction App",
    page_icon="🏠",
    layout="wide"
)



model = joblib.load("house_price_model.pkl")




create_database()
create_user_table()



st.write("🔥 TEST 123")
st.title("🔥 THIS IS MY NEW APP")
st.write("🔥 APP UPDATED")



try:

    model = joblib.load("house_price_model.pkl")


except Exception as e:

    st.error("❌ Model file load nahi ho rahi")

    st.write(e)

    st.stop()



ADMIN_EMAIL = "saquibahmed0882@gmail.com"
ADMIN_PASSWORD = "0882umam"



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False




if not st.session_state.logged_in:

    st.title("🏠 House Price Prediction")

    option = st.radio(
        "Select Option",
        ["👤 User Login", "📝 Register", "👨‍💼 Admin Login"]
    )

    if option == "📝 Register":

        st.subheader("Create Account")

        name = st.text_input("Full Name")

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Create Account"):

            if password != confirm:

                st.error("Passwords do not match")

            else:

                result = register_user(
                    name,
                    email,
                    password
                )

                if result:

                    st.success("Account created successfully 🎉")

                else:

                    st.error("Email already registered")

    elif option == "👤 User Login":

        st.subheader("User Login")

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        if st.button("User Login"):

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True

                st.success("Login Successful 🎉")

                st.rerun()

            else:

                st.error("Invalid email or password")

    else:

        st.subheader("Admin Login")

        email = st.text_input("Admin Email")

        password = st.text_input("Admin Password", type="password")

        if st.button("Admin Login"):

            if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:

                st.session_state.logged_in = True

                st.success("Login Successful 🎉")

                st.rerun()

            else:

                st.error("Wrong Admin Email or Password")

    st.stop()



if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False

    st.rerun()




def show_history():

    history = get_predictions()


    if history:

        df = pd.DataFrame(
            history,
            columns=[
                "Country",
                "State",
                "City",
                "Price",
                "Currency",
                "Date"
            ]
        )


        st.subheader("📜 Prediction History")


        st.dataframe(
            df,
            use_container_width=True
        )


    else:

        st.info("No prediction history found")




st.title("🏠 House Price Prediction App")


st.markdown("""
## 👨‍💻 Saquib Ahmed

**B.Tech Artificial Intelligence & Machine Learning**

This application predicts house prices using
Random Forest Regression Machine Learning Model.
""")


st.divider()




currency = st.sidebar.selectbox(
    "💰 Select Currency",
    [
        "USD ($)",
        "INR (₹)",
        "EUR (€)",
        "GBP (£)"
    ]
)




st.sidebar.subheader("🌍 Location")


country = st.sidebar.selectbox(
    "Country",
    get_countries()
)


state = st.sidebar.selectbox(
    "State",
    get_states(country)
)


city = st.sidebar.selectbox(
    "City",
    get_cities(country,state)
)




if st.sidebar.button("📜 View History"):

    show_history()



st.sidebar.title("📌 Project Information")


st.sidebar.markdown("""
**Developer:** Saquib Ahmed

**Model:** Random Forest Regression

**Dataset:** King County House Sales Dataset

**R² Score:** 0.68
""")



st.subheader("🏡 Enter House Details")


col1, col2 = st.columns(2)


with col1:

    bedrooms = st.number_input(
        "Bedrooms",
        0,
        10,
        3
    )


    bathrooms = st.number_input(
        "Bathrooms",
        0.0,
        10.0,
        2.0
    )


    sqft_living = st.number_input(
        "Living Area",
        100,
        10000,
        2000
    )


    sqft_lot = st.number_input(
        "Lot Area",
        100,
        50000,
        5000
    )



with col2:

    floors = st.number_input(
        "Floors",
        1.0,
        5.0,
        1.0
    )


    grade = st.number_input(
        "Grade",
        1,
        13,
        7
    )


    yr_built = st.number_input(
        "Year Built",
        1800,
        2026,
        2000
    )


    yr_renovated = st.number_input(
        "Year Renovated",
        0,
        2026,
        0
    )


waterfront = st.selectbox(
    "Waterfront",
    [0,1]
)


view = st.number_input(
    "View",
    0,
    4,
    0
)


condition = st.number_input(
    "Condition",
    1,
    5,
    3
)


sqft_above = st.number_input(
    "Sqft Above",
    100,
    10000,
    1500
)


sqft_basement = st.number_input(
    "Sqft Basement",
    0,
    5000,
    500
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



    

    symbol, final_price = convert_currency(
        prediction[0],
        currency
    )



    

    save_prediction(
        country,
        state,
        city,
        final_price,
        currency
    )



   

    st.markdown(
        "## 🏠 Prediction Result"
    )


    col1, col2 = st.columns(2)



    with col1:

        st.metric(
            "Estimated House Price",
            f"{symbol}{final_price:,.2f}"
        )



    with col2:

        st.metric(
            "Location",
            f"{city}, {state}, {country}"
        )



   

    st.subheader(
        "📊 House Details Summary"
    )


    summary = {

        "Bedrooms": bedrooms,

        "Bathrooms": bathrooms,

        "Living Area": f"{sqft_living} sqft",

        "Lot Area": f"{sqft_lot} sqft",

        "Floors": floors,

        "Grade": grade,

        "Year Built": yr_built

    }



    st.json(summary)



    


    st.subheader(
        "📈 Price Comparison"
    )


    comparison_data = pd.DataFrame({

        "Category": [

            "Predicted Price",

            "Average Price",

            "High Range"

        ],


        "Price": [

            final_price,

            final_price * 0.8,

            final_price * 1.2

        ]

    })



    st.bar_chart(
        comparison_data.set_index("Category")
    )



    # PDF Report


    pdf_file = generate_pdf(

        country,

        state,

        city,

        final_price,

        symbol

    )



    with open(pdf_file, "rb") as file:


        st.download_button(

            label="📄 Download PDF Report",

            data=file,

            file_name="House_Price_Report.pdf",

            mime="application/pdf"

        )



    st.success(
        "Prediction Saved Successfully ✅"
    )


    st.balloons()