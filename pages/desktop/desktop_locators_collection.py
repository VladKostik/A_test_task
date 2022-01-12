from selenium.webdriver.common.by import By
from pages.core.locator import Locator


class DesktopLocatorsCollection:
    def __init__(self):
        self.__new_message_button = Locator(
            By.XPATH,
            '//div/aside/button[@class="button primary compose"]'
        )
        self.__input_field_To = Locator(
            By.XPATH,
            '//div/input[@name="toFieldInput"]'
        )

        self.__subject_field = Locator(
            By.XPATH,
            '//div/input[@name="subject"]'
        )

        self.__message_frame = Locator(
            By.XPATH,
            '//div/iframe[@src=" about:blank"]'
        )

        self.__send_button = Locator(
            By.XPATH,
            '//div/button[@class="button primary send"]'
        )

        self.__income_list_count = Locator(
            By.XPATH,
            '//div/section/div/a[@id="unread"]/'
            'span[@class="sidebar__list-link-count"]'
        )

        self.__mails_table = Locator(
            By.XPATH,
            '//tbody//a[@class="msglist__row_href"][position()<16]'
        )

        self.__main_checkbox = Locator(
            By.XPATH,
            '//div/label[@class="checkbox"]'
        )

        self.__first_checkbox = Locator(
            By.XPATH,
            '//tbody//label[@class="checkbox noselect"][1]'
        )

        self.__remove_button = Locator(
            By.XPATH,
            '//div/a[@class="controls-link remove"]'
        )

    @property
    def new_message_button(self):
        return self.__new_message_button

    @property
    def input_field_To(self):
        return self.__input_field_To

    @property
    def subject_field(self):
        return self.__subject_field

    @property
    def message_frame(self):
        return self.__message_frame

    @property
    def send_button(self):
        return self.__send_button

    @property
    def income_list_count(self):
        return self.__income_list_count

    @property
    def mails_table(self):
        return self.__mails_table

    @property
    def main_checkbox(self):
        return self.__main_checkbox

    @property
    def first_checkbox(self):
        return self.__first_checkbox

    @property
    def remove_button(self):
        return self.__remove_button
