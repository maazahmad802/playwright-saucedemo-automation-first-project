# SauceDemo UI Automation Testing Project

A beginner-friendly UI automation project using **Python, Playwright, and pytest** against the public practice website https://www.saucedemo.com/.

## Coverage

The test suite includes:
1. Login page loads.
2. Valid login succeeds.
3. Invalid username is rejected.
4. Invalid password is rejected.
5. Empty username is rejected.
6. Empty password is rejected.
7. Products page displays after login.
8. Product can be added to cart.
9. Cart badge updates after adding a product.
10. Product can be removed from the cart.
11. Cart page displays the selected product.
12. User can log out.

## Requirements

- Python 3.10+
- VS Code recommended

## Setup

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

If `python` does not work, try `py` in the commands above.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

## Run tests

Run all tests in a visible browser:

```bash
pytest
```

Run with the browser visible explicitly:

```bash
pytest --headed
```

Run a single test file:

```bash
pytest tests/test_login.py
pytest tests/test_cart.py
```

Create an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Test account

SauceDemo provides this public practice account:

- Username: `standard_user`
- Password: `secret_sauce`

The test suite uses invalid credentials for negative login scenarios.

## Project structure

```text
playwright-saucedemo-automation/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_cart.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Notes

- This is a practice project for learning and demonstrating UI automation.
- The website is external; tests may be affected by site availability or changes.
- Do not use these scripts against websites without permission.
