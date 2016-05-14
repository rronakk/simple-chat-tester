"""Join chat page, used to join the chat"""

from .base_page import Page
from ..locators.join_chat_locators import JoinChatLocators
from ..pages.chat_window_page import ChatWindowPage


class JoinChatPage(Page):

    url = ''

    def return_join_chat_page(self):
        return JoinChatPage(self.driver)

    def set_sender(self, sender_name):
        """Set the sender name field when joining chat
        """
        element = self.find_element(
            JoinChatLocators.join_chat_form_loc['sender'])
        element.clear()
        element.send_keys(sender_name)

    def set_recipient(self, sender_name):
        """Set the recipient name field when joining chat
        """
        element = self.find_element(
            JoinChatLocators.join_chat_form_loc['recipient'])
        element.clear()
        element.send_keys(sender_name)

    def login(self):
        """Click login button to join the chat
        """
        self.click_element(JoinChatLocators.login_button_loc['login_button'])
        return ChatWindowPage(self.driver)
