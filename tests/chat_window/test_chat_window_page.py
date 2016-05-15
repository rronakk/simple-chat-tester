""" Test Various Functionality of chat window page
"""

def test_message_sender_to_recipient(landing_page):
    """verify that message/response sent by sender is received by recipient.
    """
    # Begin Conversation between user_1 and user_2
    join_chat = landing_page
    join_chat.set_sender("user1")
    join_chat.set_recipient("user2")
    chat_window_1 = join_chat.login()


    # Open another chat window, and begin chat between user2 and user1
    join_chat.open_new_window()
    join_chat.switch_to_window(2)
    join_chat.set_sender("user2")
    join_chat.set_recipient("user1")
    chat_window_2 = join_chat.login()

    # Add and send message
    chat_window_2.add_message("This is message from user2 to user1")
    chat_window_2.send_message()
    message_sent = chat_window_2.get_message_from_sender(0)

    # Go to 1st window and compare the message
    chat_window_1.switch_to_window(1)
    assert message_sent == chat_window_1.get_message_from_sender(0)

    # Respond to the message
    chat_window_1.add_message("This is reply message from user1 to user_2")
    chat_window_1.send_message()
    reply_message = chat_window_1.get_message_from_sender(1)

    # Go to 2nd window and compare message.
    chat_window_2.switch_to_window(2)
    assert reply_message == chat_window_2.get_message_from_sender(1)

def test_message_not_seen_by_unwanted_recipient(landing_page):
    """Verify that message sent from user_1 to user_2 is not seen in the chat_window between user1 & user_3
    """
    # Begin Conversation between user_1 and user_2
    join_chat = landing_page
    join_chat.set_sender("user1")
    join_chat.set_recipient("user2")
    chat_window_1 = join_chat.login()

    # Open another chat window, and begin chat between user1 and user3
    join_chat.open_new_window()
    join_chat.switch_to_window(2)
    join_chat.set_sender("user1")
    join_chat.set_recipient("user3")
    chat_window_2 = join_chat.login()

    # switch to chat_window for user1 and user2
    join_chat.switch_to_window(1)
    chat_window_1.add_message("This is message from user1 to user2")
    chat_window_1.send_message()
    message_between_user1_and_user2 = chat_window_1.get_message_from_sender(0)

    # switch to chat_window for user1 and user3
    join_chat.switch_to_window(2)
    chat_window_2.add_message("This is message from user1 to user3")
    chat_window_2.send_message()
    message_between_user1_and_user3 = chat_window_2.get_message_from_sender(0)

    # compare text
    assert message_between_user1_and_user2 != message_between_user1_and_user3

