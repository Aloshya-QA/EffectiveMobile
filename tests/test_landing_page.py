import allure
import pytest
import pytest_check as check

class TestLandingPage:

    BUTTONS = ["about_us", "more_info", "cases", "reviews", "contacts"]

    @pytest.fixture
    def landing_page_opened(landing_page):
        landing_page.open().is_opened()
        return landing_page

    @allure.title("Checking click buttons")
    @pytest.mark.parametrize("button", BUTTONS)
    def test_landing_buttons(self, button):
        landing_page_opened.click_button(button)
        check.is_true(landing_page_opened.button_is_clicked(button), f"Button '{button}' click failed")
