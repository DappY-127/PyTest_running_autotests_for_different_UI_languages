import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
    browser.quit()



