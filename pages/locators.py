from selenium.webdriver.common.by import By

class BasePageLocators():
    LOG_BUTTON = [By.CSS_SELECTOR, "#layer-reg"]
    USER_NAME = [By.CSS_SELECTOR, "input[name='USER_LOGIN']"]
    USER_PASS = [By.CSS_SELECTOR, "input[name='USER_PASSWORD']"]
    PERSONAL_CAB = [By.CSS_SELECTOR, 'span.btn-cabinet']
    LOG_IN = [By.CSS_SELECTOR, 'button[name="Login"]']
    REG_BUTTON = [By.CSS_SELECTOR, '#register_link_in_form']
    REG_PAGE = [By.CSS_SELECTOR, '#registration']
    POP_UP = [By.CSS_SELECTOR, 'div._wc-widget._wc-shadow._wc-position-bottom-right']