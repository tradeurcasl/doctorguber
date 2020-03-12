from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest
from .settings import link

class TestLoginForm():
    #@pytest.mark.skip
    def test_can_see_login_button_by_main_page(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_button()

    #@pytest.mark.skip
    def test_can_use_login_button_by_main_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

    #@pytest.mark.skip
    def test_user_can_log_in(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login()
        page.should_be_personal()

    #@pytest.mark.skip
    def test_new_user_can_reg(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_registration_button()
        page.should_be_registration_page()
        page.should_be_reg()
        page.should_be_personal()

    #@pytest.mark.skip
    def test_user_forgot_password(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_forgot_pass()
        page.should_use_forgot_form()
