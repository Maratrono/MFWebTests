import time

from pages import LoginPage
from pages.RecoveryPage import RecoveryPageHelper
from pages.BasePage import BasePage
from core.BaseTest import browser
from pages.LoginPage import LoginPageHelper

import allure
import random

BASE_URL = "https://ok.ru/"

LOGIN_TEXT = "Asd"
PASSWORD_TEXT_FOR_FIRST_CLICK = 'EWQ'
PASSWORD_TEXT_FOR_SECOND_CLICK = 'ASD'
PASSWORD_TEXT_FOR_THIRD_CLICK = '123'

@allure.suite("Проверка страницы восстановления доступа")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_page(browser):
    BasePage(browser).get_url(BASE_URL)
    DYNAMIC_LOGIN_TEXT = f"user_{random.randint(1000, 9999)}"
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(DYNAMIC_LOGIN_TEXT)
    LoginPage.type_password(PASSWORD_TEXT_FOR_FIRST_CLICK)
    LoginPage.click_login()
    time.sleep(2)
    LoginPage.type_password(PASSWORD_TEXT_FOR_SECOND_CLICK)
    LoginPage.click_login()
    time.sleep(2)
    LoginPage.type_password(PASSWORD_TEXT_FOR_THIRD_CLICK)
    LoginPage.click_login()
    time.sleep(2)
    LoginPage.click_recovery()
    time.sleep(2)
    RecoveryPageHelper(browser)





