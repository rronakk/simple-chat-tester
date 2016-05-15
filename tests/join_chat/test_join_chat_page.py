"""test various functionality of join_chat_page
"""


def test_joining_chat(landing_page):
    """Verify user is able to join the chat room , after login land in chat room page.
    """
    join_chat = landing_page
    join_chat.set_sender("user1")
    join_chat.set_recipient("user2")
    chat_window = join_chat.login()
    assert "Chatting" == chat_window.get_chat_window_title()


def test_sender_name_on_chat_window(landing_page):
    """Verify sender name on chat window
    """
    join_chat = landing_page
    join_chat.set_sender("user1")
    join_chat.set_recipient("user2")
    chat_window = join_chat.login()
    assert "user1" == chat_window.get_sender_name()


def test_recipient_name_on_chat_window(landing_page):
    """Verify recipient name on chat window
    """
    join_chat = landing_page
    join_chat.set_sender("user1")
    join_chat.set_recipient("user2")
    chat_window = join_chat.login()
    assert "user1" == chat_window.get_recipient_name()
