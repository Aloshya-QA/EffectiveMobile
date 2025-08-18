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

import pytest
import allure

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["landing_page"].page
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

