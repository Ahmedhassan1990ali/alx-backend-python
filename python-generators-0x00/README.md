# Python Generators - 0x00

This project demonstrates how to set up a MySQL database, populate it with user data from a CSV file, and stream data efficiently using Python generators.

## 📁 Project Structure

- `0-main.py`  
  Main setup script that:
  - Connects to MySQL
  - Creates the `ALX_prodev` database and `user_data` table (if not already existing)
  - Loads user data from `user_data.csv`
  - Confirms setup and prints the first 5 rows

- `seed.py`  
  Helper module that provides:
  - `connect_db()` – Connects to MySQL server
  - `create_database(connection)` – Creates the `ALX_prodev` database
  - `connect_to_prodev()` – Connects to the `ALX_prodev` database
  - `create_table(connection)` – Creates the `user_data` table
  - `insert_data(connection, csv_file)` – Loads data from the CSV file into the table

- `user_data.csv`  
  A CSV file containing user records with UUID, name, email, and age fields.

- `0-stream_users.py`  
  Contains a generator function:
  - `stream_users()` – Connects to the database and yields rows one by one using a single loop and `yield`.

- `1-main.py`  
  Test script that uses `islice()` to print the **first 6 user records** streamed from the database using the `stream_users()` generator.

## 💡 Prerequisites

- Python 3
- MySQL server running locally
- Python package: `mysql-connector-python`  
  Install it using:

  ```bash
  pip install mysql-connector-python
  ```

## 🚀 Usage

1. Make sure `user_data.csv` is in the same directory as the scripts.

2. Update MySQL credentials in `seed.py` and `0-stream_users.py`.

3. Run the setup script:

   ```bash
   chmod +x 0-main.py
   ./0-main.py
   ```

4. Run the generator test script:

   ```bash
   chmod +x 1-main.py
   ./1-main.py
   ```

## ✅ Example Output

```bash
('b123...', 'Alice Smith', 'alice@example.com', 35)
('c456...', 'Bob Johnson', 'bob@example.com', 42)
...
```

This confirms the generator is yielding user data one row at a time from the database.


