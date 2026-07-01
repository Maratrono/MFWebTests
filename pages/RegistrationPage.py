import allure
import random

from pages.BasePage import BasePage
#Импортируется класс By который позволяет искать локаторы(элементы по id, xpath и т.д.)
#если WebDriverWait отвечает за вопрос «Когда искать?», то класс By отвечает за вопрос «Как искать?» (по какому признаку)
from selenium.webdriver.common.by import By

class RegistrationPageLocators(BasePage):
    COUNTRY_OR_CODE_BUTTON = (By.XPATH, '//*[@aria-label="Страна или код"]')
    COUNTRY_LIST = (By.XPATH, '//div[contains(@class, "CountryList-module_countryList__listItem__")]')
    COUNTRY_ITEM = (By.XPATH, "//span[text()='Афганистан']")
    PHONE_BUTTON = (By.XPATH, '//*[@inputmode="tel"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')
    BLANK_BUTTON = (By.XPATH, '//*[@href="https://id.vk.com/promo"]')

class RegistrationPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем корректность загрузки станицы"):
            self.find_element(RegistrationPageLocators.COUNTRY_OR_CODE_BUTTON)
            #self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.PHONE_BUTTON)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.BLANK_BUTTON)
            self.attach_screenshot()

    @allure.step("Выбор рандомной страны")
    def select_random_country(self):
        random_number = random.randint(0, 205)
        self.find_element(RegistrationPageLocators.COUNTRY_OR_CODE_BUTTON).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_LIST)
        country_code = country_items[random_number].text.split('\n')[-1]
        country_items[random_number].click()
        self.attach_screenshot()
        return country_code
        #item общий список стран

    @allure.step("Клик по полю 'Введите номер телефона' для выбора страны по коду")
    def get_phone_button_value(self):
        self.attach_screenshot()
        return self.find_element(RegistrationPageLocators.PHONE_BUTTON).get_attribute('value')