import re
import time
from random_string import generate_subject, generate_message


def test_email_1(accounts, desktop):
    # sign in to account
    accounts.sign_in()

    #send 15 e-mails
    for i in range(1, 16):
        desktop.new_message()
        desktop.fill_address('asfrro_test@ukr.net')
        desktop.fill_subject(generate_subject(10))
        desktop.fill_message(generate_message(10))
        desktop.send_message()
        time.sleep(1)

    #make sure all 15 e-mails are received
    assert desktop.find_unread_list_counter() == '15'

    #navigate to income page
    desktop.click_income_list_counter()

    #get list of subjects and messages
    elements = desktop.get_subjects_and_messages()
    proto_list = [element.text for element in elements]

    #convert data to dict
    temp_list = [i.split('  ') for i in proto_list]
    new_list = [i for sublist in temp_list for i in sublist]
    it = iter(new_list)
    res_dict = dict(zip(it, it))

    #generate result message
    result = ''
    for subject, message in res_dict.items():
        numbers_sbj = re.findall(r'[0-9]', subject)
        numbers_msg = re.findall(r'[0-9]', message)
        letters_sbj = re.findall(r'[a-zA-Z]', subject)
        letters_msg = re.findall(r'[a-zA-Z]', message)
        numbers = len(numbers_sbj) + len(numbers_msg)
        letters = len(letters_sbj) + len(letters_msg)

        temp_message = \
            f'Received mail on theme {subject} with message: {message}. ' \
            f'It contains {letters} letters and {numbers} numbers.\n'
        result += temp_message

    #send result message
    desktop.new_message()
    desktop.fill_address('asfrro_test@ukr.net')
    desktop.fill_subject('Test Results')
    desktop.fill_message(result)
    desktop.send_message()
    time.sleep(1)

    # delete all mails except result
    desktop.click_income_list_counter()
    desktop.click_main_checkbox()
    desktop.deselect_first_checkbox()
    desktop.click_remove_button()
