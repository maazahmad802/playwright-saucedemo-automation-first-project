from playwright.sync_api import Page, expect


class LoginPage:
    """Reusable locators and actions for the SauceDemo login page."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_error(self, message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(message)
