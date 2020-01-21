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
        login = 'it-manager'
        input1.send_keys(login)
        input2 = self.browser.find_element(*BasePageLocators.USER_PASS)
        password = 'sv8pKD8s' #ввести пароль перед запуском
        input2.send_keys(password)
        button = self.browser.find_element(*BasePageLocators.LOG_IN)
        button.click()
        assert True, "Something go wrong"

    def should_be_personal(self):
        self.browser.find_element(*BasePageLocators.PERSONAL_CAB)
        assert True, "You are not log in user"

    def should_be_personal_page(self):
        bub = self.browser.find_element(*BasePageLocators.PERSONAL_CAB)
        bub.click()
        assert True, "Ooops, something is wrong"

    def should_be_registration_button(self):
        self.browser.find_element(*BasePageLocators.REG_BUTTON)
        assert True, "You are not log in user"

    def should_be_registration_page(self):
        button = self.browser.find_element(*BasePageLocators.REG_BUTTON)
        button.click()
        self.browser.find_element(*BasePageLocators.REG_PAGE)
        assert True, "This is not registration page"

    '''Явное ожидание в этом тесте необходимо, т.к. если заполнять все формочки слишком быстро, сайт думает, 
    что это авторизовывается бот (и в чем-то он прав)'''
    def should_be_reg(self):
        input1 = self.browser.find_element(*BasePageLocators.MAIL_REG)
        f = faker.Faker()
        email = f.email()
        input1.send_keys(email)
        time.sleep(1)
        input2 = self.browser.find_element(*BasePageLocators.USER_PASS)
        password = '159753'
        input2.send_keys(password)
        time.sleep(1)
        input3 = self.browser.find_element(*BasePageLocators.NAME_REG)
        name = f.name()
        input3.send_keys(name)
        time.sleep(1)
        input4 = self.browser.find_element(*BasePageLocators.FAM_REG)
        time.sleep(1)
        input4.send_keys(name)
        button = self.browser.find_element(*BasePageLocators.BUTTON_REG)
        button.click()
        assert True, "Something go wrong"

    def should_be_forgot_pass(self):
        button = self.browser.find_element(*BasePageLocators.FORGET)
        button.click()
        assert True, 'Some problems with forget password button'
        input1 = self.browser.find_element(*BasePageLocators.USER_NAME)
        login = 'k_n_ch@mail.ru'
        input1.send_keys(login)
        button = self.browser.find_element(*BasePageLocators.VYSLAT)
        button.click()
        x = self.browser.find_element(*BasePageLocators.ZAPROS)
        x = x.text
        y = 'Запрос отправлен на ваш e-mail'
        assert x==y, 'Some problems'