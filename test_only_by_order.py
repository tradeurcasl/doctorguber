from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

link = 'https://www.doctorguber.ru/samogonovarenie/aksessuary-sn/sushilki_dlya_butylok/sushilka-dlya-butylok-plastikovaya/'
'''Можно использовать любую другую ссылку на товар под заказ, просто заменив ее здесь
Вообще, поскольку механизм однокликовой покупки и под заказ одинаков, то в этих тестах нет особой необходимости
(если сломается 1 клик, то и это полетит). Но так как в таких товарах только одна кнопка (а не две, как у норм товаров),
то чтобы несколько раз в одном кейсе не менять линк, я вынесла эти тесты в отдельный пак
Опять же юзер в логин-пэйдж может быть изменен - сейчас там стоит мой тестовый аккаунт
'''
class TestByOrder():
    def test_new_user_can_order_by_order(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_buy_by_oneclick_new()

    def test_reg_user_can_order_by_order(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login()
        page.should_be_personal()
        page = ProductPage(browser, link)
        page.should_buy_by_oneclick_new()
