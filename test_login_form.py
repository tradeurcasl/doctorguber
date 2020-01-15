from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest

class TestLoginForm():
    #@pytest.mark.skip
    def test_can_see_login_button_by_main_page(self, browser):
        link = 'https://www.doctorguber.ru/'
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page = LoginPage(browser, link)
        page.should_be_login_button()

    #@pytest.mark.skip
    def test_can_use_login_button_by_main_page(self, browser):
        link = 'https://www.doctorguber.ru/'
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_login_page()

    def test_user_can_log_in(self, browser):
        link = 'https://www.doctorguber.ru/'
        page = BasePage(browser, link)
        page.open()
        time.sleep(1)
        page.go_to_login_page()
        time.sleep(1)
        pagec = LoginPage(browser, link)
        pagec.should_be_login()
        time.sleep(2)
        pagec.should_be_personal()
        time.sleep(2)
