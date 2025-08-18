import allure
import pytest_check as check

class TestLandingPage:

    BUTTONS_TO_TEST = ["about_us", "more_info", "cases", "reviews", "contacts"]

    @allure.title("Checking click buttons")
    @pytest.mark.parametrize("button", BUTTONS_TO_TEST)
    def test_landing_buttons(self, landing_page, button):
        landing_page.open().is_opened()
        for button in self.BUTTONS_TO_TEST:
            landing_page.click_button(button)
            check.is_true(landing_page.button_is_clicked(button),
                          f"Button '{button}' click failed")
