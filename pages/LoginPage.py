
from pages.BasePage import BasePage
#Импортируется класс By который позволяет искать локаторы(элементы по id, xpath и т.д.)
#если WebDriverWait отвечает за вопрос «Когда искать?», то класс By отвечает за вопрос «Как искать?» (по какому признаку)
from selenium.webdriver.common.by import By

#Создаем класс для хранения найденных элементов на странице по xpath
class LoginPageLocators(BasePage):
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    #LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.XPATH, '//*[@id="field_password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_BUTTON_QR_CODE = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[//button/span/span[text()= "Зарегистрироваться"]')
    REGISTRATION_BUTTON_BY_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    REGISTRATION_BUTTON_BY_MAIL = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    REGISTRATION_BUTTON_BY_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    QR_LOGIN_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')

class LoginPageHelper(BasePage):
    pass