
# Python Generators - 0x01

This project introduces the use of **Python decorators** to log SQL queries executed by functions that interact with a database. The goal is to enhance visibility into SQL operations using clean, reusable decorator logic with `datetime` and `print()`.

## 📁 Project Structure

- ### `0-log_queries.py`  
  Implements a logging decorator:
  - `log_queries()` – Logs SQL queries passed to the decorated function using `print()` and includes a timestamp using `datetime.now()`.
  - Demonstrates usage with `fetch_all_users(query)`, which connects to an SQLite database and returns query results.
  - Logs appear in the terminal output (no log file used).

## 💡 Prerequisites

- Python 3.x
- No external packages required (uses standard library only)

## 🚀 Usage

1. Ensure the script is executable:

   ```bash
   chmod +x 0-log_queries.py
   ```

2. Run the script:

   ```bash
   ./0-log_queries.py
   ```

## ✅ Example Output

* From `0-log_queries.py` (printed result and log):

  ```bash
  [2025-07-08 14:45:22] Executing SQL Query: SELECT * FROM users
  [('b123...', 'Alice Smith', 'alice@example.com', 35), ('c456...', 'Bob Johnson', 'bob@example.com', 42)]
  ```




