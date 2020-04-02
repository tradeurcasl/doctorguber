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
    FORGET = [By.CSS_SELECTOR, 'a.forget']
    VYSLAT = [By.CSS_SELECTOR, "button[name='send_account_info']"]
    ZAPROS = [By.CSS_SELECTOR,'p.h1']
    SEARCH = [By.CSS_SELECTOR, 'span.search.a']
    SEARCH_INPUT = [By.CSS_SELECTOR, '#title-search-input']
    FIND = [By.CSS_SELECTOR, 'button[name="s"]']
    RESULT = [By.CSS_SELECTOR, 'div.search-page-blocks']

class UserPageLocators():
    ORDERS = [By.CSS_SELECTOR, "a[href='/personal/order/']"]

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
    REG_SUB = [By.CSS_SELECTOR, '#btn-submit-cart']

class RentPageLocators():
    BUTTON_PAGE = [By.CSS_SELECTOR, ' div.rent__info > button']
    NAME = [By.CSS_SELECTOR, '#rentName']
    PHONE = [By.CSS_SELECTOR, '#rentTel']
    EMAIL = [By.CSS_SELECTOR, '#rentEmail']
    COMM = [By.CSS_SELECTOR, '#rentComment']
    BUTTON_MODAL = [By.CSS_SELECTOR, 'div.rent__modal-info > button']
    CLOSE = [By.CSS_SELECTOR, 'button.rent__modal-close']
