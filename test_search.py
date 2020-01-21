from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time
import pytest

link = 'https://www.doctorguber.ru/'

class TestSearchForm():
    def test_user_can_find_items(self, browser):
        page = LoginPage(browser, link)
        page.open()
        time.sleep(1)
        page.should_use_search()