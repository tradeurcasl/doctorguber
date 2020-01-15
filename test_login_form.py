from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest

link = 'https://www.doctorguber.ru/'

class TestLoginForm():
    @pytest.mark.skip
    def test_can_see_login_button_by_main_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page = LoginPage(browser, link)
        page.should_be_login_button()

    @pytest.mark.skip
    def test_can_use_login_button_by_main_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_login_page()

    @pytest.mark.skip
    def test_user_can_log_in(self, browser):
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_login_page()
        time.sleep(1)
        pagec = LoginPage(browser, link)
        pagec.should_be_login()
        time.sleep(2)
        pagec.should_be_personal()


    def test_new_user_can_reg(self, browser):
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_login_page()
        time.sleep(1)
        pagec = LoginPage(browser, link)
        pagec.should_be_registration_button()
        time.sleep(1)
        pagec.should_be_registration_page()
        pagec.should_be_reg()
        time.sleep(2)
        pagec.should_be_personal()


