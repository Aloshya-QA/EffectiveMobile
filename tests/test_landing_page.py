import allure
import pytest
import pytest_check as check

class TestLandingPage:

    BUTTONS = ["about_us", "more_info", "cases", "reviews", "contacts"]

    @allure.title("Checking click buttons")
    @pytest.mark.parametrize("button", BUTTONS)
    def test_landing_buttons(self, landing_page, button):
        landing_page.open().is_opened().click_button(button)
        check.is_true(landing_page.button_is_clicked(button),
                      f"Button '{button}' click failed")
