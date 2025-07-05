import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields users in batches of size `batch_size`.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # 🔁 Change to your MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # 👈 Yield a full batch at once

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return


def batch_processing(batch_size):
    """
    Filters users over the age of 25 from each batch and prints them.
    """
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        for user in batch:  # Loop 2
            if float(user['age']) > 25:
                print(user)
