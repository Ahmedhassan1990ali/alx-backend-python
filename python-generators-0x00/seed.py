import mysql.connector
import csv
import os
import uuid

# 🔌 Connect to MySQL server (no specific database)
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Change if you use a different MySQL user
            password="yourpassword" # <-- Change this to your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# 🏗️ Create database ALX_prodev if not exists
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

# 🔌 Connect directly to ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Change if you use a different MySQL user
            password="yourpassword", # <-- Change this to your MySQL password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

# 🧱 Create table user_data if not exists
def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

# 📥 Insert data from CSV if not already in table
def insert_data(connection, csv_file):
    cursor = connection.cursor()

    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found.")
        return

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the record already exists
            cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row['user_id'],))
            exists = cursor.fetchone()
            if not exists:
                insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    row['user_id'],
                    row['name'],
                    row['email'],
                    row['age']
                ))

    connection.commit()
    cursor.close()
    print("CSV data inserted into user_data table (if not already present)")
