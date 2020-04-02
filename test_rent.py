from .pages.rent_page import RentPage
from .pages.login_page import LoginPage
from .settings import linkrent



class TestRentPage():


    def test_logged_in_user_can_rent(self, browser):
        page = LoginPage(browser, linkrent)
        page.open()
        page.go_to_login_page()
        page.should_be_login()
        page.should_be_personal()
        page = RentPage(browser, linkrent)
        page.should_rent()


    def test_new_user_can_rent(self, browser):
        page = RentPage(browser, linkrent)
        page.open()
        page.should_rent()