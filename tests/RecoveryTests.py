import time

from pages import LoginPage
from pages.RecoveryPage import RecoveryPageHelper
from pages.BasePage import BasePage
from core.BaseTest import browser
from pages.LoginPage import LoginPageHelper

import allure
import random

BASE_URL = "https://sn.rv-school.ru/"

LOGIN_TEXT = "Asd"
PASSWORD_TEXT = "1"

@allure.suite("Проверка страницы восстановления доступа")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_page(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(LOGIN_TEXT)

    for i in range(3):
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.click_login()
        time.sleep(2)

    LoginPage.click_recovery()
    time.sleep(2)
    RecoveryPageHelper(browser)





