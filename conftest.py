import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--windows-size=800,600')
    browser = webdriver.Chrome()
    browser.get(url)

    yield browser
    browser.quit()