import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# добавили обработчик опций
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--language", action="store", default="en-gb")


@pytest.fixture(scope="function")
def browser(request):
    browse_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = None
    if browse_name == 'chrome':
        browser = webdriver.Chrome(options=options)
    elif browse_name == 'safari':
        browser = webdriver.Safari(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
