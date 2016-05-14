"""Chat window after login """
from .base_page import Page
from ..locators.chat_window_locators import ChatWindowLocators


class ChatWindowPage(Page):

    url = ''

    def add_message(self, message):
        """Enter message to be sent to recipient
        Args :
            message (str) : Message to be sent
        """
        element = self.find_element(
            ChatWindowLocators.input_field_loc['message'])
        element.clear()
        element.send_keys(message)

    def send_message(self):
        """ click send button
        """
        self.click_element(ChatWindowLocators.send_button_loc['send'])

    def get_sender_name(self, message_number):
        """Get the sender name from the chat-box
        Args :
            message_number : sender name for the message order starting from top.
        """
        return self.find_element(ChatWindowLocators.find_chat_box_message_sender_loc(message_number)).text

    def get_message_from_sender(self, message_number):
        """Get the message content from the chat-box
        Args :
            message_number : Message content for the message order starting from top.
        """
        return self.find_element(ChatWindowLocators.find_chat_box_message_loc(message_number)).text
