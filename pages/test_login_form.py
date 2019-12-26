from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest

class TestLoginForm():
    def test_can_login_by_main_page(self, browser):
        link = 'https://www.doctorguber.ru/'
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_button()
