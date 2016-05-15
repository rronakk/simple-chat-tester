from selenium.webdriver.common.by import By


class ChatWindowLocators(object):
    """locators for chat_window module"""
    input_field_loc = {
        'message': (By.CSS_SELECTOR, ".chatForm>input")
    }

    send_button_loc = {
        'send': (By.CSS_SELECTOR, ".chatForm>button")
    }

    header_loc = {
        'title': (By.CSS_SELECTOR, ".app>h1")
    }

    chat_user_loc = {
        'sender': (By.CSS_SELECTOR, "span[data-reactid='.0.1.1']"),
        'recipient': (By.CSS_SELECTOR, "span[data-reactid='.0.1.3']")
    }

    def find_chat_box_message_loc(position):
        """returns locator for chat box message at a particular position
        Args :
            position (int) : the message order from the top
        """
        return By.CSS_SELECTOR, "span[data-reactid='.0.2." + str(position) + ".1']"

    def find_chat_box_message_sender_loc(position):
        """returns locator for chat box sender at a particular position
        Args :
            position (int) : message order from the top
        """
        return By.CSS_SELECTOR, "span[data-reactid='.0.2." + str(position) + ".0']"
