import pytest
from selenium import webdriver
from pages.desktop.desktop_page import DesktopPage
from pages.sign_in_page.accounts_page import AccountsPage


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome('../drivers/chromedriver')
    url_1 = 'https://accounts.ukr.net/'
    browser.get(url_1)
    browser.maximize_window()
    yield browser
    # browser.quit()


@pytest.fixture
def accounts(browser) -> AccountsPage:
    yield AccountsPage(browser)


@pytest.fixture
def desktop(browser) -> DesktopPage:
    yield DesktopPage(browser)
