from selenium.webdriver.common.by import By


class JoinChatLocators(object):
    """locators for join_chat module"""

    join_chat_form_loc = {
        'sender': (By.XPATH, ".//*[@id='content']/div/form/div[1]/input"),
        'recipient': (By.XPATH, ".//*[@id='content']/div/form/div[2]/input")
    }

    header_loc = {
        'title': (By.CSS_SELECTOR, ".app>h1")
    }

    login_button_loc = {
        'login_button': (By.CSS_SELECTOR, ".input>button")
    }