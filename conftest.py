import pytest
from playwright.sync_api import sync_playwright

from pages.landing_page import LandingPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            yield browser
        finally:
            browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10000)
    try:
        yield page
    finally:
        try:
            page.close()
        except:
            pass
        context.close()

@pytest.fixture
def landing_page(page):
    return LandingPage(page)
