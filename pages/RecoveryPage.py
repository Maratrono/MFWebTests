import allure

from pages.BasePage import BasePage
from core.BaseTest import browser
from selenium.webdriver.common.by import By



class RecoveryPageLocators(BasePage):
    PHONE_BUTTON = (By.XPATH, '//*[@data-test-id="recovery-phone-btn"]')
    MAIL_BUTTON =  (By.XPATH, '//*//*[@id="recovery-email-btn"]')
    QR_CODE_BUTTON = (By.XPATH, '//*[@id="qr-image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@id="support-contact-btn"]')

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