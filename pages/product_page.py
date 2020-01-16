from .locators import ProductPageLocators
from .base_page import BasePage

import time

al_text = 'Заявка успешно отправлена. Мы скоро свяжемся с вами (обычно, в течении 2-х часов в рабочее время).'
class ProductPage(BasePage):
    def should_buy_by_oneclick(self):
        button = self.browser.find_element(*ProductPageLocators.ONE_CLICK)
        button.click()
        time.sleep(1)
        butto = self.browser.find_element(*ProductPageLocators.SUB_ONE)
        butto.click()
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        if alert_text == al_text:
            alert.accept()
        else:
            print("Something is wrong with alert")


