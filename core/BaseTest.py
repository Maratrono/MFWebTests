import pytest
from selenium import webdriver

@pytest.fixture(scope= "function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang = ru")
    driver = webdriver.Remote(command_executor="http://85.198.71.219:8080", options=options)
    yield driver
    if driver:
        driver.quit()