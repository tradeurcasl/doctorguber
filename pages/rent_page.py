from .locators import RentPageLocators
from .base_page import BasePage
from ..settings import email, name

class RentPage(BasePage):

    def should_rent(self):

        button = self.browser.find_element(*RentPageLocators.BUTTON_PAGE)
        button.click()
        input1 = self.browser.find_element(*RentPageLocators.NAME)
        input1.send_keys(name)
        input2 = self.browser.find_element(*RentPageLocators.PHONE)
        phone = '77777977777'
        input2.send_keys(phone)
        input3 = self.browser.find_element(*RentPageLocators.EMAIL)
        input3.send_keys(email)
        input4 = self.browser.find_element(*RentPageLocators.COMM)
        input4.send_keys(name)
        button = self.browser.find_element(*RentPageLocators.BUTTON_MODAL)
        button.click()
        button = self.browser.find_element(*RentPageLocators.CLOSE)
        button.click()
        assert True, 'Something go wrong with user`s rent'

