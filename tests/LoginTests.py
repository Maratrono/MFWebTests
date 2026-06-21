import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"


@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки авторизации при пустом поле логина")
def test_empty_login(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    import time;time.sleep(1.5)
    # Добавил эту строчку, чтобы Одноклассники успели показать ошибку до скриншота, а то скриншот у меня был без текста ошибки
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки авторизации при пустом поле пароля")
def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_keys_login(text_for_send= "admin")
    LoginPage.click_login()
    import time;time.sleep(1.5)
    # Добавил эту строчку, чтобы Одноклассники успели показать ошибку до скриншота, а то скриншот у меня был без текста ошибки
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR