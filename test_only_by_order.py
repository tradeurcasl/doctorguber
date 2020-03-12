from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .settings import link1


class TestByOrder():
    def test_new_user_can_order_by_order(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_buy_by_oneclick_new()

    def test_reg_user_can_order_by_order(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.go_to_login_page()
        page.should_be_login()
        page.should_be_personal()
        page = ProductPage(browser, link1)
        page.should_buy_by_oneclick_new()
