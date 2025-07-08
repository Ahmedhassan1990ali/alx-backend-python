# Python Context and Async Operations - 0x02

This project focuses on building custom context managers and exploring asynchronous operations in Python. The goal is to learn how to manage resources efficiently and structure asynchronous code using clean, reusable patterns.

## 📁 Project Structure

- ### `0-databaseconnection.py`  
  Implements:
  - `DatabaseConnection` – A class-based context manager using `__enter__` and `__exit__` to open and close a SQLite connection.
  - Demonstrates usage with a `with` block to perform a query: `SELECT * FROM users`.
- ### `1-execute.py`  
  Implements:
  - `ExecuteQuery` – A class-based context manager that takes a SQL query and parameters.
  - Automatically handles database connection and query execution inside a `with` block.
  - Demonstrates usage with a query filtering users by age (`age > 25`).



## 💡 Prerequisites

- Python 3.x
- SQLite3 (standard with Python)

## 🚀 Usage

1. Ensure the file is executable:

   ```bash
   chmod +x 0-databaseconnection.py
   ```

2. Run the script:

   ```bash
   ./0-databaseconnection.py
   ```

2. Run the reusable query context manager:

   ```bash
   chmod +x 1-execute.py
   ./1-execute.py
   ```

## ✅ Example Output

* From `0-databaseconnection.py`:

    ```bash
    [('1', 'Alice Smith', 'alice@example.com', 35), ('2', 'Bob Johnson', 'bob@example.com', 42)]
    ```

* From `1-execute.py`:

    ```bash
    [('2', 'Bob Johnson', 'bob@example.com', 42)]
    ```