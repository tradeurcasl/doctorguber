from .pages.base_page import BasePage
from .pages.user_page import UserPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time
import pytest

link = 'https://www.doctorguber.ru/samogonovarenie/oborudovanie/distilyatsiya/distillyator-doktor-guber/'
"""Можно подставить любой другой товар по ссылке"""


class TestProductCart():
    """Так как тестовый сервер сейчас не работает, пишу для аккаунта it-manager.
    Должен работать для всех, просто изменить логин и пароль для требуемого юзера  логин пейдж
    """

    def test_log_in_user_can_buy_one_click_popular(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.should_be_login()
        page.should_be_personal()
        page = ProductPage(browser, link)
        page.should_buy_by_oneclick()
