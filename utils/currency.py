def convert_currency(price, currency):

    rates = {
        "USD ($)": 1,
        "INR (₹)": 83,
        "EUR (€)": 0.92,
        "GBP (£)": 0.78
    }

    symbols = {
        "USD ($)": "$",
        "INR (₹)": "₹",
        "EUR (€)": "€",
        "GBP (£)": "£"
    }

    converted_price = price * rates[currency]

    return symbols[currency], converted_price