from pages.AdPage import AdPageLocators, AdPageHelper
from pages.HelpPage import HelpPageHeplper, HelpPageLocators
from pages.BasePage import BasePage
from core.BaseTest import browser
from pages.LoginPageForOk import LoginPageForOkHelper

import allure

BASE_URL = 'https://ok.ru/'

@allure.suite("Скролл на странице 'Помощь' и переход на страницу 'Рекламный кабинет'")
@allure.title("Переход на страницу 'Помощь'")
def test_scroll_page_help(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPageForOk = LoginPageForOkHelper(browser)
    LoginPageForOk.click_help_button()
    HelpPage = HelpPageHeplper(browser)
    HelpPage.scrollToitems(HelpPageLocators.AD_ACCOUNT_LINK)
    AdPage = AdPageHelper(browser)
    AdPage.check_page()

