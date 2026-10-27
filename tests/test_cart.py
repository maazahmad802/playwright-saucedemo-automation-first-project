from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_and_add_backpack(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.expect_products_page()
    inventory.add_backpack_to_cart()
    return inventory


def test_cart_shows_added_product(page):
    inventory = login_and_add_backpack(page)
    inventory.open_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(
        "Sauce Labs Backpack"
    )


def test_product_can_be_removed_from_cart(page):
    inventory = login_and_add_backpack(page)
    inventory.open_cart()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="cart-list"] .cart_item')).to_have_count(0)


def test_user_can_log_out(page):
    inventory = login_and_add_backpack(page)
    inventory.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator('[data-test="login-button"]')).to_be_visible()
