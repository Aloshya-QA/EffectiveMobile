import allure
import pytest
from loguru import logger
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from pages.base_page import BasePage


class LandingPage(BasePage):
    BUTTONS = {
        "specialists": "//a[@href='#specialists']",
        "about_us": "//a[@href='#about' and contains(text(), '[ О нас ]')]",
        "more_info": "//a[@href='#moreinfo' and contains(text(), '[ Услуги ]')]",
        "cases": "//a[@href='#cases' and contains(text(), '[ Проекты ]')]",
        "reviews": "//a[@href='#Reviews' and contains(text(), '[ Отзывы ]')]",
        "contacts": "//a[@href='#contacts' and contains(text(), '[ Контакты ]')]"
    }

    @allure.step("Opening Landing page...")
    def open(self):
        super().open()
        logger.info("Opening Landing page...")
        return self

    @allure.step("Landing page is opened")
    def is_opened(self):
        try:
            self.page.wait_for_selector(self.BUTTONS["specialists"], state="visible")
            logger.info("LandingPage is opened")
        except PlaywrightTimeoutError as e:
            logger.error(f"LandingPage isn't opened: {e}")
            pytest.fail("LandingPage isn't opened")
        return self

    @allure.step("Click '{name}' button")
    def click_button(self, name: str):
        if name not in self.BUTTONS:
            raise ValueError(f"Button '{name}' not found")
        self.page.click(self.BUTTONS[name])
        logger.info(f"Click '{name}' button")
        return self

    @allure.step("'{name}' button is clicked")
    def button_is_clicked(self, name: str) -> bool:
        if name not in self.BUTTONS:
            raise ValueError(f"Button '{name}' not found")
        locator = self.page.locator(self.BUTTONS[name]).first
        href = locator.get_attribute("href")
        logger.info(f"'{name}' button is clicked")
        return href in self.page.url
