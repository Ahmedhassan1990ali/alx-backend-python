import mysql.connector

def stream_users():
    """
    Generator that yields user records one by one from the user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # 🔁 Replace with your actual MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        # Single loop — yields one row at a time
        for row in cursor:
            yield row

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return
