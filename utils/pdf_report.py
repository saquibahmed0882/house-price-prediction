from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(country, state, city, price, symbol):

    file_name = "House_Price_Report.pdf"

    pdf = canvas.Canvas(file_name, pagesize=letter)

    pdf.setFont("Helvetica", 14)

    pdf.drawString(
        100,
        750,
        "House Price Prediction Report"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        100,
        700,
        f"Location: {city}, {state}, {country}"
    )

    pdf.drawString(
        100,
        670,
        f"Estimated Price: {symbol}{price:,.2f}"
    )

    pdf.drawString(
        100,
        620,
        "Model: Random Forest Regression"
    )

    pdf.drawString(
        100,
        590,
        "Dataset: King County House Sales Dataset"
    )

    pdf.save()

    return file_name