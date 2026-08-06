import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class VkProjectPageLocators(BasePage):
    PROJECTS_BUTTON = (By.XPATH, '//span[text() ="Проекты"]')


class VkProjectPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем открытие страницы ВК/Проекты"):
            self.find_element(VkProjectPageLocators.PROJECTS_BUTTON)
            self.attach_screenshot()


    def get_window_id(self, index):
        return self.driver.window_handles[index]

        # driver.window_handles - выдает список всех открытых вкладок/окон (в виде списка строк). это спец команда
        # driver.current_window_handle — выдает ID только той одной вкладки, на которую сейчас сфокусирован Selenium.

        # Создаем функцию для выбора вкладки по номеру по window_id

    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)