from .locators import ProductPageLocators
from .base_page import BasePage
import faker
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


    def should_buy_by_oneclick_new(self):
        button = self.browser.find_element(*ProductPageLocators.ONE_CLICK)
        button.click()
        time.sleep(1)
        input1 = self.browser.find_element(*ProductPageLocators.NAME)
        login = 'test_its'
        input1.send_keys(login)
        f = faker.Faker()
        email = f.email()
        input2 = self.browser.find_element(*ProductPageLocators.EMAIL)
        input2.send_keys(email)
        input3 = self.browser.find_element(*ProductPageLocators.PHONE)
        phone = '77777977777'
        input3.send_keys(phone)
        time.sleep(2)
        butto = self.browser.find_element(*ProductPageLocators.SUB_ONE)
        butto.click()
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        if alert_text == al_text:
            alert.accept()
        else:
            print("Something is wrong with alert")

    def reg_user_can_good_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.CART)
        button.click()
        button = self.browser.find_element(*ProductPageLocators.IN_CART)
        button.click()
        time.sleep(1)
        self.browser.find_element(*ProductPageLocators.LIST_CART)
        assert True, 'There is no items'