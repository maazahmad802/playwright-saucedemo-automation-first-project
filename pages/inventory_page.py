from playwright.sync_api import Page, expect


class InventoryPage:
    """Reusable actions for the products/inventory and cart areas."""

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator('[data-test="title"]')
        self.inventory_items = page.locator(".inventory_item")
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')

    def expect_products_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.page_title).to_have_text("Products")
        expect(self.inventory_items.first).to_be_visible()

    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def remove_backpack_from_products(self):
        self.page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
