import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ToolbarPageLocators(BasePage):
    TOOLBAR_BUTTON_OK = (By.XPATH, '//img[@aria-label="Логотип" and contains(@class, "light")]')
    TOOLBAR_BUTTON_SEARCH = (By.XPATH, '(//button[@aria-label="Искать"])[1]')
    TOOLBAR_NAVIGATOR = (By.XPATH, "//button[@aria-expanded]/span[starts-with(@class, 'toolbar_nav')]")
    MORE_BUTTON = (By.XPATH, '//span[text()="Ещё"]')



class ToolbarPageHeplper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем корректность кнопок в Toolbar страницы"):
            self.attach_screenshot()
        self.find_element(ToolbarPageLocators.TOOLBAR_BUTTON_OK)
        self.find_element(ToolbarPageLocators.TOOLBAR_BUTTON_SEARCH)
        self.find_element(ToolbarPageLocators.TOOLBAR_NAVIGATOR)

    @allure.step("Клик по кнопке 'Навигатор vk-ecosystem-toolbar'")
    def click_button_vk_ecosystem(self):
        self.attach_screenshot()
        self.find_element(ToolbarPageLocators.TOOLBAR_NAVIGATOR).click()


    @allure.step("Клик по кнопке 'Ещё'")
    def click_button_more(self):
        self.attach_screenshot()
        self.find_element(ToolbarPageLocators.MORE_BUTTON).click()

    #Необходимо получить id вкладки браузера, потому что после нажатия кнопки еще открывается
    # новая вкладка в браузере
    # Передаем параметр индекс для того чтобы выбирать вкладку, первую, вторую и т.д.
    def get_window_id(self, index):
        return self.driver.window_handles[index]

    #driver.window_handles - выдает список всех открытых вкладок/окон (в виде списка строк). это спец команда
    #driver.current_window_handle — выдает ID только той одной вкладки, на которую сейчас сфокусирован Selenium.

    #Создаем функцию для выбора вкладки по номеру по window_id
    def switch_window(self,window_id):
        self.driver.switch_to.window(window_id)