import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HelpPageLocators(BasePage):
    #TOOLBAR_BUTTON_OK = (By.XPATH, '//a[@data-l="t,logo"]/div[@class="toolbar_logo_img"]')
    TOOLBAR_BUTTON_SEARCH = (By.XPATH, "//button[starts-with(@data-l, 'search')]")
    TOOLBAR_NAVIGATOR = (By.XPATH, "//button[@aria-expanded]/span[starts-with(@class, 'toolbar_nav')]")
    TOOLBAR_LOGIN = (By.XPATH, '//*[@data-l="t,login"]')
    INPUT_SEARCH = (By.XPATH, '//input[@type="search"]')
    PASSWORD_CHIPS = (By.XPATH, "//div[@data-uikit-old='Chip']/span[contains(text(), 'пароль')]")
    RECOVERY_CHIPS = (By.XPATH, "//div[@data-uikit-old='Chip']/span[contains(text(), 'восстановить профиль')]")
    UNLOCK_CHIPS = (By.XPATH, "//div[@data-uikit-old='Chip']/span[contains(text(), 'разблокировать')]")
    REGISTRATION_CHIPS = (By.XPATH, "//div[@data-uikit-old='Chip']/span[contains(text(), 'регистрация')]")
    QR_CODE_CHIPS = (By.XPATH, "//div[@data-uikit-old='Chip']/span[contains(text(), 'фото с кодом')]")
    TODAY_RELEVANT_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Сегодня актуально")]')
    REGISTRATION_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Регистрация")]')
    MY_PROFILE_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Мой профиль")]')
    CHAT_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Общение")]')
    PROFILE_ACCESS_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Доступ к профилю")]')
    SECURITY_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Безопасность")]')
    GROUPS_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Группы")]')
    PAID_SERVICES_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Платные функции")]')
    REPORT_AND_SPAM_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Нарушения и спам")]')
    GAMES_AND_APPS_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Игры и приложения")]')
    OTHERS_SERVICES_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Другие сервисы")]')
    USEFUL_INFO_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Полезная информация")]')
    AD_ACCOUNT_LINK = (By.XPATH, '//*[@class="help_app_info" and contains(text(), "Рекламный кабинет")]')


class HelpPageHeplper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем корректность страницы Помощь"):
            self.attach_screenshot()
        #self.find_element(HelpPageLocators.TOOLBAR_BUTTON_OK)
        self.find_element(HelpPageLocators.TOOLBAR_BUTTON_SEARCH)
        self.find_element(HelpPageLocators.TOOLBAR_NAVIGATOR)
        self.find_element(HelpPageLocators.TOOLBAR_LOGIN)
        self.find_element(HelpPageLocators.INPUT_SEARCH)
        self.find_element(HelpPageLocators.PASSWORD_CHIPS)
        self.find_element(HelpPageLocators.RECOVERY_CHIPS)
        self.find_element(HelpPageLocators.UNLOCK_CHIPS)
        self.find_element(HelpPageLocators.REGISTRATION_CHIPS)
        self.find_element(HelpPageLocators.QR_CODE_CHIPS)
        self.find_element(HelpPageLocators.TODAY_RELEVANT_LINK)
        self.find_element(HelpPageLocators.REGISTRATION_LINK)
        self.find_element(HelpPageLocators.MY_PROFILE_LINK)
        self.find_element(HelpPageLocators.CHAT_LINK)
        self.find_element(HelpPageLocators.PROFILE_ACCESS_LINK)
        self.find_element(HelpPageLocators.SECURITY_LINK)
        self.find_element(HelpPageLocators.GROUPS_LINK)
        self.find_element(HelpPageLocators.PAID_SERVICES_LINK)
        self.find_element(HelpPageLocators.REPORT_AND_SPAM_LINK)
        self.find_element(HelpPageLocators.GAMES_AND_APPS_LINK)
        self.find_element(HelpPageLocators.OTHERS_SERVICES_LINK)
        self.find_element(HelpPageLocators.USEFUL_INFO_LINK)
        self.find_element(HelpPageLocators.AD_ACCOUNT_LINK)

    @allure.step("Скроллим страницу до указанной кнопки и кликаем на него")
    def scrollToitems(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()