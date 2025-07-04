# Python Generators - 0x00

This project demonstrates how to set up a MySQL database and use Python to populate and query it. It prepares the foundation for using generators to stream data from the database.

## 📁 Project Structure

- `0-main.py`  
  The main script that orchestrates the database setup and data insertion. It:
  - Connects to the MySQL server
  - Creates the `ALX_prodev` database (if not exists)
  - Connects to the new database
  - Creates the `user_data` table (if not exists)
  - Loads and inserts data from the CSV file
  - Verifies database and table creation
  - Prints the first 5 rows for confirmation

- `seed.py`  
  Contains all utility functions for database connection, table creation, and CSV data insertion. Functions include:
  - `connect_db()`
  - `create_database(connection)`
  - `connect_to_prodev()`
  - `create_table(connection)`
  - `insert_data(connection, csv_file)`

- `user_data.csv`  
  A sample dataset containing user records (UUID, name, email, age). Used for populating the `user_data` table.

## 💡 Prerequisites

- MySQL server installed and running
- Python 3.x
- `mysql-connector-python` module:  
  Install via `pip install mysql-connector-python`

## 🚀 Usage

Make sure `user_data.csv` is in the same directory as `0-main.py` and `seed.py`. Then:

```bash
chmod +x 0-main.py
./0-main.py
````

The script should confirm successful setup and display the first 5 rows from the `user_data` table.


