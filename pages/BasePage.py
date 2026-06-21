#Чтобы тест не падал с ошибкой «элемент не найден», этот инструмент заставляет код временно остановиться и подождать, пока кнопка или текст появятся на экране
from selenium.webdriver.support.wait import WebDriverWait

#Позволяет программе понять, чего именно мы ждем. Например: «жди, пока кнопка станет кликабельной», «жди, пока исчезнет баннер» или «жди, пока появится нужный текст»
from selenium.webdriver.support import expected_conditions
import allure

# Создаем родительский» класс-шаблон. От него будут наследоваться все остальные страницы вашего тестов
# Магическая функция init self чтобы driver был доступен во всех функциях создаваемых под этим классом
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Создаем функцию поиска элементов
    def find_element(self, locator, time=5):
        #Драйвер подожди 5 секунд(по умолчанию 5 секунд, можем и больше поставить) пока не будут видны элементы которые мы тебе укажем в переменной locator
        #Сообщение будет выводится если только какой либо locator не отобразится
        # Суть проверки чтобы как раз найти элементы страницы, которые мы указываем и потом проверяем их по своим атрибутам, например на кликабельность, на ввод текста и т.д.
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message= f"Не удалось найти элемент {locator}")

    #Создаем функцию для перехода к сайту
    @allure.step("Открываем страницу")
    def get_url(self, url):
        return self.driver.get(url)


    def attach_screenshot(self):
       allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)
