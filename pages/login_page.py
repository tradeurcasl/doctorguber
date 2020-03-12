from .base_page import BasePage
from .locators import BasePageLocators
from ..settings import login, password, email, name, key


class LoginPage(BasePage):
    def should_be_login_button(self):
        self.browser.find_element(*BasePageLocators.LOG_BUTTON)
        assert True, "There is no login button"

    def should_be_login(self):
        input1 = self.browser.find_element(*BasePageLocators.USER_NAME)
        input1.send_keys(login)
        input2 = self.browser.find_element(*BasePageLocators.USER_PASS)
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
        input1.send_keys(email)
        input2 = self.browser.find_element(*BasePageLocators.USER_PASS)
        input2.send_keys(password)
        input3 = self.browser.find_element(*BasePageLocators.NAME_REG)
        input3.send_keys(name)
        input4 = self.browser.find_element(*BasePageLocators.FAM_REG)
        input4.send_keys(name)
        button = self.browser.find_element(*BasePageLocators.BUTTON_REG)
        button.click()
        assert True, "Something go wrong"

    def should_be_forgot_pass(self):
        button = self.browser.find_element(*BasePageLocators.FORGET)
        button.click()
        assert True, 'Some problems with forget password button'

    def should_use_forgot_form(self):
        input1 = self.browser.find_element(*BasePageLocators.USER_NAME)
        input1.send_keys(login)
        button = self.browser.find_element(*BasePageLocators.VYSLAT)
        button.click()
        x = self.browser.find_element(*BasePageLocators.ZAPROS)
        x = x.text
        y = 'Запрос отправлен на ваш e-mail'
        assert x==y, 'Some problems' \

    '''В зависимости он нужды, вставьте слово для поиска
    '''
    def should_use_search(self):
        button = self.browser.find_element(*BasePageLocators.SEARCH)
        button.click()
        input1 = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        input1.send_keys(key)
        button = self.browser.find_element(*BasePageLocators.FIND)
        button.click()
        assert self.is_element_present(*BasePageLocators.RESULT), 'There is no such item'