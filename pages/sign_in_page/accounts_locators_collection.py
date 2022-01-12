from selenium.webdriver.common.by import By
from pages.core.locator import Locator


class AccountsLocatorsCollection:
    def __init__(self):
        self.__login_field = Locator(
            By.XPATH,
            '//div/label/input[@name="login"]'
        )
        self.__password_field = Locator(
            By.XPATH,
            '//div/label/input[@name="password"]'
        )
        self.__submit_button = Locator(
            By.XPATH,
            '//button[@type="submit"]'
        )

    @property
    def log_in_field(self):
        return self.__login_field

    @property
    def password_field(self):
        return self.__password_field

    @property
    def submit_button(self):
        return self.__submit_button
