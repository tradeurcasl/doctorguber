
from .locators import UserPageLocators
from .base_page import BasePage
from datetime import date

today = date.today()
d1 = today.strftime("%d.%m.%Y")

class UserPage(BasePage):
    def go_to_orders(self):
        button = self.browser.find_element(*UserPageLocators.ORDERS)
        button.click()

    def should_see_current_date_order(self):
        date = self.browser.find_element(*UserPageLocators.DATE_ORDER)
        date = date.text
        assert date == d1, 'There is new orders'
