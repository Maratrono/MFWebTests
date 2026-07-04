import allure

from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.LoginPageForOk import LoginPageForOkHelper
from pages.RegistrationPage import RegistrationPageHelper
from core.BaseTest import browser

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка страницы Регистрациия")
@allure.title("Проверка соответствия кода страны маске номера телефона")
def test_registration(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageForOkHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_button_value()
    assert Selected_country_code == Actual_country_code.strip()