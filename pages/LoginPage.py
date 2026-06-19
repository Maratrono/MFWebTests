
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
    REGISTRATION_BUTTON = (By.XPATH, '//button/span/span[text()= "Зарегистрироваться"]')
    REGISTRATION_BUTTON_BY_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    REGISTRATION_BUTTON_BY_MAIL = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    REGISTRATION_BUTTON_BY_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    QR_LOGIN_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    ERROR_TEXT = (By.XPATH, "//span[starts-with(text(), 'Введите')]")

class LoginPageHelper(BasePage):
#новый класс с наследованием BasePage
    def __init__(self,driver):
    # здесь создаем конструктор и передаем браузер
        self.driver = driver
        #определяем что именно этот driver это его
        self.check_page()
        #проверяем на какой на верной ли странице находимся


    def check_page(self):
    #создаем функцию проверки страницы,передаем self чтобы он мог узнать все параметры, функции своего класса и родительского класса
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        #как раз используем find element это и есть функция родительского класса BasePage
        # передаем ему LoginPageLocators, это новый класс, тоже унаследованный от BasePage, здесь указаны локаторы
        # вызываем функцию найти элемент, указываем какой именно локатор ищем
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR_CODE)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_BY_VK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_BY_MAIL)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_BY_YANDEX)
        self.find_element(LoginPageLocators.QR_LOGIN_TAB)

#Мы написали Pattern page object - когда каждая страница это отдельный объект, под нее заводится класс, описываются все элементы которые есть на этой странице
# Описываются все действия на этой странице, которую можно делать на этой странице, клик например
# Страницы не соединяем, то есть не пишем на две страницы одновременно тесты а разделяем даже если одна страница открывается только после клика какого либо поля на какой либо странице
# Страницы не смешиваем

    def click_login(self):
    #создаем функцию инициирующую клик по полю войти без заполнения логина или пароля
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        # ищем кнопку login_tab(кнопка войти) и кликаем

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
        #ищем элемент по локатору, который выдает ошибку Введите логин и возвращает текст ошибки этого локатора

    def send_keys_login(self, text_for_send):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_for_send)
