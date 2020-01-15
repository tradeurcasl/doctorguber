from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest

link = 'https://www.test.doctorguber.ru/'

class TestProductCart():
    def test_log_in_user_can_buy_one_click(self, browser):
        page = BasePage(browser, link)
        page.open()