from selenium.webdriver.chrome.webdriver import WebDriver
from get_sign_in_data import login, password
from pages.basepage import BasePage
from pages.sign_in_page.accounts_locators_collection import AccountsLocatorsCollection


class AccountsPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locators_collection = AccountsLocatorsCollection()

    def sign_in(self) -> None:
        self._click(self.__locators_collection.log_in_field)
        self._send_keys(self.__locators_collection.log_in_field, login)
        self._click(self.__locators_collection.password_field)
        self._send_keys(self.__locators_collection.password_field, password)
        self._click(self.__locators_collection.submit_button)
