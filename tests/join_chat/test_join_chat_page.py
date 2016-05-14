"""test various functionality of join_chat_page"""


def test_message_sender_to_recipient(landing_page):
    """verify that message/response sent by sender is received by recipient."""
    # Open the join chat page.
    join_chat = landing_page

    # Add a Sender
    join_chat.set_sender("user_1")

    # Add a recipient
    join_chat.set_recipient("user_2")

    # Join the chat
    join_chat.login()

    # Open another chat window, and join the chat
    join_chat.open_new_window()
    join_chat.switch_to_window(2)
    join_chat.set_sender("user_2")
    join_chat.set_recipient("user_1")
    chat_window = join_chat.login()

    # Add and send message
    chat_window.add_message("This is message from user_2 to user_1")
    chat_window.send_message()
    message_sent = chat_window.get_message_from_sender(0)

    # Go to 1st window and compare the message
    chat_window.switch_to_window(1)
    assert message_sent == chat_window.get_message_from_sender(0)

    # Respond to the message
    chat_window.add_message("This is reply message from user_1 to user_2")
    chat_window.send_message()
    reply_message = chat_window.get_message_from_sender(1)

    # Go to 2nd window and compare message.
    chat_window.switch_to_window(2)
    assert reply_message == chat_window.get_message_from_sender(1)
