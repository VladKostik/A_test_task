from typing import Union
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.basepage import BasePage
from pages.desktop.desktop_locators_collection import DesktopLocatorsCollection


class DesktopPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locators_collection = DesktopLocatorsCollection()

    def new_message(self) -> None:
        self._click(self.__locators_collection.new_message_button)

    def fill_address(self, email: str) -> None:
        self._send_keys(self.__locators_collection.input_field_To, email)

    def fill_subject(self, subject: str) -> None:
        self._send_keys(self.__locators_collection.subject_field, subject)

    def fill_message(self, message: str) -> None:
        self._send_keys_to_frame(
            self.__locators_collection.message_frame,
            message
        )

    def send_message(self) -> None:
        self._click(self.__locators_collection.send_button)

    def find_unread_list_counter(self) -> str:
        return self._find_element(
            self.__locators_collection.income_list_count
        ).text

    def click_income_list_counter(self) -> None:
        self._click(self.__locators_collection.income_list_count)

    def get_subjects_and_messages(self) -> Union[list, WebElement]:
        return self._find_elements(self.__locators_collection.mails_table)

    def click_main_checkbox(self) -> None:
        self._click(self.__locators_collection.main_checkbox)

    def deselect_first_checkbox(self) -> None:
        self._click(self.__locators_collection.first_checkbox)

    def click_remove_button(self) -> None:
        self._click(self.__locators_collection.remove_button)
