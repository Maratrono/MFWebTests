import allure

from pages.BasePage import BasePage
#Импортируется класс By который позволяет искать локаторы(элементы по id, xpath и т.д.)
#если WebDriverWait отвечает за вопрос «Когда искать?», то класс By отвечает за вопрос «Как искать?» (по какому признаку)
from selenium.webdriver.common.by import By

#Создаем класс для хранения найденных элементов на странице по xpath
class LoginPageLocators(BasePage):
    LOGIN_FIELD = (By.XPATH, '//*[@id="login-phone-email"]')
    #LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.XPATH, '//*[@id="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-submit-btn"]')
    LOGIN_TAB = (By.XPATH, '//*[@id="tabLogin"]')
    LOGIN_BUTTON_QR_CODE = (By.XPATH, '//*[@id="tabQr"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="forgot-password-link"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="hero-register-btn"]')
    REGISTRATION_BUTTON_2 = (By.XPATH, '//*[@id="hero-login-btn"]')
    ERROR_TEXT = (By.XPATH, '//*[@id="login-error"]')
    RECOVERY_BUTTON = (By.XPATH, '//*[@id="lockout-recover-btn"]')
    CANCEL_BUTTON = (By.XPATH, "//*[@id='lockout-cancel-btn']")

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
        with allure.step("Проверяем корректность страницы загрузки"):
            self.attach_screenshot()
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
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_2)



#Мы написали Pattern page object - когда каждая страница это отдельный объект, под нее заводится класс, описываются все элементы которые есть на этой странице
# Описываются все действия на этой странице, которую можно делать на этой странице, клик например
# Страницы не соединяем, то есть не пишем на две страницы одновременно тесты а разделяем даже если одна страница открывается только после клика какого либо поля на какой либо странице
# Страницы не смешиваем


    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login(self):
    #создаем функцию инициирующую клик по полю войти без заполнения логина или пароля
        self.attach_screenshot() #скриншот перед кликом войти
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        # ищем кнопку login_tab(кнопка войти) и кликаем

    @allure.step("Вывод текста ошибки при клике 'Войти'")
    def get_error_text(self):
        self.attach_screenshot() #скриншот после вывода ошибки
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
        #ищем элемент по локатору, который выдает ошибку Введите логин и возвращает текст ошибки этого локатора

    @allure.step("Ввод текста в поле 'Логин'")
    def send_keys_login(self, text_for_send):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_for_send)


    @allure.step("Заполняем поле логин")
    def type_login(self, text_for_login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_for_login)
        self.attach_screenshot()
        #здесь в отличие от предыдущего send_keys сразу же заполняем поле, то есть находим элемент и вводим текст, а не как выше сделано
        #Переменная text_for_login (в скобках метода) — это и есть тот текст,
        # который мы передадим из теста для ввода в поле

    @allure.step("Заполняем поле пароля")
    def type_password(self, text_for_password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(text_for_password)
        self.attach_screenshot()

    @allure.step("Кликаем на 'Восстановить'")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()