from selenium.webdriver.common.by import By
import random


class BasePageLocators():
    LOG_BUTTON = [By.CSS_SELECTOR, "#layer-reg"]
    USER_NAME = [By.CSS_SELECTOR, "input[name='USER_LOGIN']"]
    USER_PASS = [By.CSS_SELECTOR, "input[name='USER_PASSWORD']"]
    PERSONAL_CAB = [By.CSS_SELECTOR, 'span.btn-cabinet']
    LOG_IN = [By.CSS_SELECTOR, 'button[name="Login"]']
    REG_BUTTON = [By.CSS_SELECTOR, '#register_link_in_form']
    REG_PAGE = [By.CSS_SELECTOR, '#registration']
    POP_UP = [By.CSS_SELECTOR, 'div._wc-widget._wc-shadow._wc-position-bottom-right']
    MAIL_REG = [By.CSS_SELECTOR, 'input[name="USER_EMAIL"]']
    NAME_REG = [By.CSS_SELECTOR, 'input[name="USER_NAME']
    FAM_REG = [By.CSS_SELECTOR, 'input[name="USER_LAST_NAME']
    BUTTON_REG = [By.CSS_SELECTOR, 'button[name="Register']
    SOME_POP_GOOD = [By.XPATH, '/html/body/section/div[1]/div/section/div/div[1]/div/div/a[1]']


class UserPageLocators():
    ORDERS = [By.CSS_SELECTOR, "a[href='/personal/order/']"]
    DATE_ORDER = [By.XPATH, '/html/body/section/section/div/div[2]/div[2]/div[1]/div[2]/p' ] #не универсально


class ProductPageLocators():
    ONE_CLICK = [By.CSS_SELECTOR, 'button.btn.oneclick']
    SUB_ONE = [By.CSS_SELECTOR, 'button[name="web_form_submit"]']
    NAME = [By.CSS_SELECTOR, '#name']
    EMAIL = [By.CSS_SELECTOR, '#email']
    PHONE = [By.CSS_SELECTOR, '#phone']