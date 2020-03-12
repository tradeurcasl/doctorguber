from .pages.base_page import BasePage
from .pages.login_page import LoginPage

class TestSearchForm():
    def test_user_can_find_items(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_use_search()