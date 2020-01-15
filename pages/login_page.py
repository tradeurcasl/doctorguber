from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
import faker
import time

class LoginPage(BasePage):
    def should_be_login_button(self):
        self.browser.find_element(*BasePageLocators.LOG_BUTTON)
        assert True, "There is no login button"

    def should_be_login(self):
        input1 = self.browser.find_element(*BasePageLocators.USER_NAME)
        login = 'k_n_ch@mail.ru'
        input1.send_keys(login)
        input2 = self.browser.find_element(*BasePageLocators.USER_PASS)
        password = '159753'
        input2.send_keys(password)
        button = self.browser.find_element(*BasePageLocators.LOG_IN)
        button.click()
        assert True, "Something go wrong"

    def should_be_personal(self):
        self.browser.find_element(*BasePageLocators.PERSONAL_CAB)
        assert True, "You are not log in user"

    def should_be_registration_button(self):
        self.browser.find_element(*BasePageLocators.REG_BUTTON)
        assert True, "You are not log in user"

    def should_be_registration_page(self):
        button = self.browser.find_element(*BasePageLocators.REG_BUTTON)
        button.click()
        self.browser.find_element(*BasePageLocators.REG_PAGE)
        assert True, "This is not registration page"