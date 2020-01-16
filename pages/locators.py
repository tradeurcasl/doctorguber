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
    POOP_UP = [By.CSS_SELECTOR, 'div._wc-icon._wc-top-icon._wc-icon-close._wc-close']
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
    CART = [By.CSS_SELECTOR, 'button.btn.add-to-cart']
    IN_CART = [By.CSS_SELECTOR, 'span.personal-nav-cart']
    LIST_CART = [By.CSS_SELECTOR, '#basket_items_list']
    UNREG_BUY = [By.CSS_SELECTOR, 'a.btn.by_without_reg']

class BuyPageLocators():
    FIO = [By.CSS_SELECTOR, '#ORDER_PROP_1']
    EM = [By.CSS_SELECTOR, '#ORDER_PROP_3']
    TEL = [By.CSS_SELECTOR, '#ORDER_PROP_2']
    DESC = [By.CSS_SELECTOR, '#ORDER_DESCRIPTION']
    OK = [By.CSS_SELECTOR, '#step_2_validation']
    CONFIRM = [By.CSS_SELECTOR, '#ORDER_CONFIRM_BUTTON']
    GOTOVO = [By.CSS_SELECTOR, '#order_form_div']
    LOG_BUTTON = [By.CSS_SELECTOR, 'a.issue_without_reg']