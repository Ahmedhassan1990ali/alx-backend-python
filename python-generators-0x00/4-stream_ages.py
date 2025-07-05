#!/usr/bin/python3
import seed  # assumes seed.py contains connect_to_prodev()

def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield float(row[0])  # Yield each age as float

    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Uses the generator to compute the average age efficiently.
    """
    total = 0
    count = 0

    for age in stream_user_ages():  # First and only loop
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")
