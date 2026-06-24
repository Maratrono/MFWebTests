import allure

from pages.BasePage import BasePage
from core.BaseTest import browser
from selenium.webdriver.common.by import By



class RecoveryPageLocators(BasePage):
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    MAIL_BUTTON =  (By.XPATH, '//*[@data-l="t,email"]')
    QR_CODE_BUTTON = (By.XPATH, '//*[@class="qr_code_image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="support-link_item-text"]')

class RecoveryPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность страницы загрузки"):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.MAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE_BUTTON)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)