from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_page_loads(page):
    login = LoginPage(page)
    login.open()

    expect(page).to_have_title("Swag Labs")
    expect(login.username_input).to_be_visible()
    expect(login.password_input).to_be_visible()
    expect(login.login_button).to_be_visible()


def test_valid_login_succeeds(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.expect_products_page()


def test_invalid_username_is_rejected(page):
    login = LoginPage(page)
    login.open()
    login.login("wrong_user", "secret_sauce")

    login.expect_login_error("Username and password do not match")


def test_invalid_password_is_rejected(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_password")

    login.expect_login_error("Username and password do not match")


def test_empty_username_is_rejected(page):
    login = LoginPage(page)
    login.open()
    login.login("", "secret_sauce")

    login.expect_login_error("Username is required")


def test_empty_password_is_rejected(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "")

    login.expect_login_error("Password is required")
