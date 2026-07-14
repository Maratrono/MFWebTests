import time

from pages.BasePage import BasePage
from core.BaseTest import browser
from pages.ToolbarPage import ToolbarPageLocators, ToolbarPageHeplper
from pages.VkProjectPage import VkProjectPageLocators, VkProjectPageHelper
from pages.LoginPageForOk import LoginPageForOkHelper, LoginPageForOkLocators


import allure


BASE_URL = 'https://ok.ru/'


@allure.title("Переход из вкладки Вк/Проекты обратно на начальную страницу ВК")
@allure.step("Переход на страницу Вк/Проекты")
def test_switch_tabs_ok(browser):
    BasePage(browser).get_url(BASE_URL)
    ToolbarPage = ToolbarPageHeplper(browser)
    #задаем что вкладка со страницей ToolbarPage до нажатия еще индекс - 0
    current_window_id = ToolbarPage.get_window_id(0)
    ToolbarPage.click_button_vk_ecosystem()
    ToolbarPage.click_button_more()
    #import time; time.sleep(1)
    #Задаем другую переменную обозначающую индекс второй вкладки после нажатия перехода на другую страницу с помощью другой вкладки
    new_window_id = ToolbarPage.get_window_id(1)
    #Переходим во вторую вкладку, вызываем функцию переключения из ToolbarPage
    ToolbarPage.switch_window(new_window_id)
    VkProjectPage = VkProjectPageHelper(browser) #Проверяем локаторы на странцие вк проекты
    #Переходим обратно на первую вкладку
    VkProjectPage.switch_window(current_window_id)
    #Проверяем страницу начальную ок что мы там, то есть запускаем проверку тулбара
    LoginPageForOkHelper(browser)







