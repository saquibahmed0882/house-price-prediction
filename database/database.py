import sqlite3
from datetime import datetime


DATABASE = "predictions.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        country TEXT,
        state TEXT,
        city TEXT,
        price REAL,
        currency TEXT,
        date TEXT

    )
    """)

    conn.commit()
    conn.close()



def save_prediction(country,state,city,price,currency):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions VALUES (?,?,?,?,?,?)
        """,
        (
            country,
            state,
            city,
            price,
            currency,
            datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    )

    conn.commit()
    conn.close()



def get_predictions():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM predictions"
    )

    data = cursor.fetchall()

    conn.close()

    return data