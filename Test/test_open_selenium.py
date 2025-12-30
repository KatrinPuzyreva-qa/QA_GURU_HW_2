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


@pytest.mark.github
def test_open_github(browser):
    url = 'https://github.com/'
    browser.get(url)

    expected_title = 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'
    actual_title = browser.title.strip()  # Избавляемся от возможных пробелов

    assert actual_title == expected_title, f'Заголовок страницы отличается от ожидаемого: {actual_title}'
    assert browser.current_url == url, f'URL страницы отличается от ожидаемого: {browser.current_url}'
