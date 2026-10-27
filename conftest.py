import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    """Launch Chromium and provide a fresh page for each test."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        browser_context = browser.new_context()
        page = browser_context.new_page()
        page.set_default_timeout(5000)
        yield page
        browser_context.close()
        browser.close()
