import allure
from selenium.webdriver.common.bidi.browsing_context import XPathLocator

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class AdPageLocators(BasePage):
    AD_CABINET_TITLE = (By.XPATH, "//span[text()='Рекламный кабинет']")

class AdPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver



    def check_page(self):
        with allure.step("Проверяем корректность страницы Рекламы"):
            self.attach_screenshot()
        self.find_element(AdPageLocators.AD_CABINET_TITLE)