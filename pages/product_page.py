from .locators import ProductPageLocators
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BuyPageLocators
from .locators import UserPageLocators
import faker
import time

f = faker.Faker()
email = f.email()

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

    def non_reg_user_can_good_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.CART)
        button.click()
        button = self.browser.find_element(*ProductPageLocators.IN_CART)
        button.click()
        time.sleep(1)
        self.browser.find_element(*ProductPageLocators.LIST_CART)
        assert True, 'There is no items'

    def non_reg_user_can_buy(self):
        button = self.browser.find_element(*ProductPageLocators.CART)
        button.click()
        button = self.browser.find_element(*ProductPageLocators.IN_CART)
        button.click()
        time.sleep(2)
        #button = self.browser.find_element(*BasePageLocators.POOP_UP)
        #button.click()
        button = self.browser.find_element(*BasePageLocators.POP_UP)
        button.click()
        time.sleep(2)
        button = self.browser.find_element(*BuyPageLocators.LOG_BUTTON)
        button.click()
        button = self.browser.find_element(*ProductPageLocators.UNREG_BUY)
        button.click()
        time.sleep(1)
        input1 = self.browser.find_element(*BuyPageLocators.FIO)
        fio = 'Test ITS agency'
        input1.send_keys(fio)
        input2 = self.browser.find_element(*BuyPageLocators.EM)
        input2.send_keys(email)
        input3 = self.browser.find_element(*BuyPageLocators.TEL)
        phone = '77777977777'
        input3.send_keys(phone)
        input4 = self.browser.find_element(*BuyPageLocators.DESC)
        test = 'это тестовый заказ от тестировщика its.agency'
        input4.send_keys(test)
        button = self.browser.find_element(*BuyPageLocators.OK)
        button.click()
        time.sleep(3)
        button = self.browser.find_element(*BuyPageLocators.CONFIRM)
        button.click()
        self.browser.find_element(*UserPageLocators.ORDERS)
        assert True, 'Order is not right'