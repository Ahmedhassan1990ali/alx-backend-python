
# Python Generators - 0x01

This project introduces the use of **Python decorators** to log SQL queries executed by functions that interact with a database. The goal is to enhance visibility into SQL operations using clean, reusable decorator logic with `datetime` and `print()`.

## 📁 Project Structure

- ### `0-log_queries.py`  
  Implements a logging decorator:
  - `log_queries()` – Logs SQL queries passed to the decorated function using `print()` and includes a timestamp using `datetime.now()`.
  - Demonstrates usage with `fetch_all_users(query)`, which connects to an SQLite database and returns query results.
  - Logs appear in the terminal output (no log file used).
- ### `1-with_db_connection.py`  
  Implements a decorator:
  - `with_db_connection()` – Opens a connection to `users.db`, passes it to the decorated function, and ensures it's closed after execution.
  - Demonstrates usage with `get_user_by_id(user_id)`, which retrieves a single user record from the database by ID.
  - Helps eliminate repetitive connection handling logic and reduces boilerplate code.
- ### `2-transactional.py`  
  Implements two decorators:
  - `with_db_connection()` – Opens and closes the SQLite connection automatically.
  - `transactional()` – Wraps function logic in a transaction. Automatically commits if successful, rolls back if an exception occurs.
  - Demonstrates usage with `update_user_email(user_id, new_email)` which updates a user's email.
- ### `3-retry_on_failure.py`  
  Implements:
  - `retry_on_failure(retries=3, delay=1)` – A decorator that retries a database operation up to a specified number of times if it raises an exception.
  - Reuses `with_db_connection()` to manage SQLite connections.
  - Demonstrates usage with `fetch_users_with_retry()`, which fetches all users and retries up to 3 times if it fails.
- ### `4-cache_query.py`  
  Implements:
  - `cache_query()` – Caches the result of a SQL query based on the query string to avoid redundant DB calls.
  - Reuses `with_db_connection()` for DB access.
  - Demonstrates usage with `fetch_users_with_cache(query)`.
  - Uses an in-memory dictionary (`query_cache`) for caching results across repeated calls.

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
3. Run the connection-handling decorator script:

   ```bash
   chmod +x 1-with_db_connection.py
   ./1-with_db_connection.py
   ```

4. Run the transaction-handling script:

   ```bash
   chmod +x 2-transactional.py
   ./2-transactional.py
   ```

5. Run the retrying fetch script:

   ```bash
   chmod +x 3-retry_on_failure.py
   ./3-retry_on_failure.py
   ```

6. Run the caching query script:

   ```bash
   chmod +x 4-cache_query.py
   ./4-cache_query.py
   ```

## ✅ Example Output

* From `0-log_queries.py` (printed result and log):

  ```bash
  [2025-07-08 14:45:22] Executing SQL Query: SELECT * FROM users
  [('b123...', 'Alice Smith', 'alice@example.com', 35), ('c456...', 'Bob Johnson', 'bob@example.com', 42)]
  ```

* From `1-with_db_connection.py` (fetch user by ID with auto-managed connection):

  ```bash
  ('1', 'Alice Smith', 'alice@example.com', 35)
  ```

* From `2-transactional.py` (transactional email update):

  - ✅ If the user exists and the update succeeds:

    ```bash
    (no output — transaction committed silently)
    ```

  - ❌ If the table `users` doesn't exist or the ID is invalid:

    ```bash
    [ERROR] Transaction failed: no such table: users
    Traceback (most recent call last):
      ...
    ```

* From `3-retry_on_failure.py` (auto-retry on failure):

  - ✅ If table exists and query works:

    ```bash
    [('1', 'Alice Smith', 'alice@example.com', 35), ('2', 'Bob Johnson', 'bob@example.com', 42)]
    ```

  - ❌ If table is missing or fails temporarily:

    ```bash
    [RETRY 1] Failed with error: no such table: users
    [RETRY 2] Failed with error: no such table: users
    [RETRY 3] Failed with error: no such table: users
    [GIVE UP] Max retries reached.
    Traceback (most recent call last):
      ...
    ```

* From `4-cache_query.py` (first call hits DB, second call uses cache):

  ```bash
  [CACHE MISS] Executing and caching result.
  [CACHE HIT] Returning cached result.
  [('1', 'Alice Smith', 'alice@example.com', 35), ('2', 'Bob Johnson', 'bob@example.com', 42)]
  ```