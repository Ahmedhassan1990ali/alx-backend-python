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

- `1-batch_processing.py`  
  Implements batch logic using generators:
  - `stream_users_in_batches(batch_size)` – Yields users in chunks using `fetchmany()`
  - `batch_processing(batch_size)` – Filters and prints users with age > 25

- `2-main.py`  
  Test script that runs `batch_processing(50)` and prints filtered user records (as dictionaries)

- `2-lazy_paginate.py`  
  Implements:
  - `paginate_users(page_size, offset)` – Fetches one page of users from the DB
  - `lazy_pagination(page_size)` – Generator that lazily yields one page at a time using a single loop

- `3-main.py`  
  Test script that prints paginated users in batches using `lazy_pagination(100)`


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

5. Run batch processing (filters users over age 25):

   ```bash
   chmod +x 2-main.py
   ./2-main.py | head -n 5
   ```
6. Run lazy pagination (fetches one page at a time):

    ```bash
    chmod +x 3-main.py
    ./3-main.py | head -n 7
    ```

## ✅ Example Output

- From `1-main.py` (single user stream):

        ```bash
        ('b123...', 'Alice Smith', 'alice@example.com', 35)
        ('c456...', 'Bob Johnson', 'bob@example.com', 42)
        ...
        ```

- From `2-main.py` (filtered batch as dictionaries):

    ```bash
    {'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
    {'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
    ...
    ```


- From `3-main.py` (lazy pagination output):

    ```bash
    {'user_id': '...', 'name': 'Alice', 'email': 'alice@example.com', 'age': 35}
    ...
    ```
















