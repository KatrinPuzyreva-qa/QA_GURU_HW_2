import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.selenium
def test_open_selenium(browser):
    url = 'https://www.selenium.dev/'
    browser.get(url)

    assert browser.title == 'Selenium', f'Заголовок страницы отличается от ожидаемого: {browser.title}'
    assert browser.current_url == url, f'URL страницы отличается от ожидаемого: {browser.current_url}'




def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url
