from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
import faker

class LoginPage(BasePage):
    def should_be_login_button(self):
        self.browser.find_element(*LoginPageLocators.LOG_BUTTON)
        assert True, "There is no login button"

    def should_be_login_form(self):
        button = self.browser.find_element(*LoginPageLocators.LOG_BUTTON)
        button.click()

