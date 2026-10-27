from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_as_standard_user(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.expect_products_page()
    return inventory


def test_products_are_displayed_after_login(page):
    inventory = login_as_standard_user(page)

    expect(inventory.inventory_items).to_have_count(6)
    expect(page.locator('[data-test="inventory-item-name"]').first).to_be_visible()


def test_product_can_be_added_to_cart(page):
    inventory = login_as_standard_user(page)
    inventory.add_backpack_to_cart()

    expect(inventory.cart_badge).to_have_text("1")


def test_cart_badge_updates_when_product_is_removed(page):
    inventory = login_as_standard_user(page)
    inventory.add_backpack_to_cart()
    inventory.remove_backpack_from_products()

    expect(inventory.cart_badge).to_have_count(0)
