# 📁 0x03-Unittests and Integration Tests

This project focuses on writing unit tests and integration tests in Python, using the `unittest` module and `parameterized`, as well as testing patterns such as mocking and fixtures.

---

## 📌 Learning Objectives

* Understand the difference between **unit** and **integration** tests.
* Know how to use `unittest` and `parameterized`.
* Apply mocking techniques to isolate parts of code.
* Use **fixtures** to cleanly structure your test data.

---

## 🗂️ File Structure

```
.
├── client.py
├── fixtures.py
├── test_client.py
├── test_utils.py
├── utils.py
```

---

## 📄 File Descriptions

### `utils.py`

* `access_nested_map()`: Navigate nested dictionaries by path.
* `get_json()`: Fetch JSON from a URL using `requests`.
* `memoize()`: Decorator to cache method results.

### `client.py`

* Defines `GithubOrgClient` which fetches data from the GitHub API for a given organization.
* Includes:

  * `.org()`: Fetch org metadata
  * `.repos_payload()`: Fetch repos list
  * `.public_repos()`: List of public repo names (with optional license filtering)
  * `.has_license()`: Check if a repo uses a specific license  

### `fixtures.py`

* Contains test data used in `test_client.py`

```python
ORG_PAYLOAD = {"login": "google"}
REPOS_PAYLOAD = [{"name": "repo1"}, {"name": "repo2"}]
EXPECTED_REPOS = ["repo1", "repo2"]

ORG_PAYLOAD_WITH_LICENSE = {
    "repos_url": "https://api.github.com/orgs/google/repos"
}
REPOS_PAYLOAD_WITH_LICENSE = [
    {"name": "repo1", "license": {"key": "my_license"}},
    {"name": "repo2", "license": {"key": "other_license"}},
]
```

---

## 🧪 Testing Files

### `test_utils.py`

Unit tests for `utils.py`, covering:

* `access_nested_map` using `@parameterized.expand`
* `get_json` using `mock`
* `memoize` by mocking method calls and checking caching

### `test_client.py`

Tests for `GithubOrgClient`:

* Org and repos URL fetching
* `public_repos()` return value
* License filtering
* Mocks `requests.get` and `utils.get_json`
* Uses fixtures from `fixtures.py`

---

## 🛠️ Tools & Libraries

* `unittest`: Standard Python testing framework
* `parameterized`: For running the same test with different inputs
* `unittest.mock`: For patching dependencies and simulating API calls

---

## 🚀 Run the Tests

From your project directory:

```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```

Or run all tests at once:

```bash
python3 -m unittest discover
```

---
