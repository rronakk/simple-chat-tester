from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page(object):
    """
    Base class that all page models inherit from
    """

    def __init__(self, selenium_driver,
                 base_url='https://simple-chat-asapp.herokuapp.com/',
                 timeout=10):
        """
        Args:
            selenium_driver (object): selenium webdriver to navigate pages with
            base_url (str, optional): url prefix for which other urls are based
            timeout (int, optional): seconds to wait for conditions to be
            satisfied

        """
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = timeout
        self.windows = {
            ''
        }

    def find_element(self, locator, timeout=None):
        """Return the element specified with value using the `by` selector type.

        Args:
            by (object): the selenium selection type for the value.
                http://selenium-python.readthedocs.org/en/latest/api.html#selenium.webdriver.common.by.By
                for supported locator strategies
            value (str): value locator strategy uses to evaluate presence of
            element
            timeout (int, optional): seconds to wait for selector condition to
                be satisfied
        """
        if timeout is None:
            timeout = self.timeout

        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )

        except WebDriverException:
            print("Element with %s locator not found!")

        finally:
            return element

    def click_element(self, locator):
        """Click the element specified with value using the by selector type.

        Args:
            by (object): the selenium selection type for the value.
                http://selenium-python.readthedocs.org/en/latest/api.html#selenium.webdriver.common.by.By
                for supported locator strategies
            value (str): value locator strategy uses to evaluate presence of
                element
        """
        element_to_click = self.find_element(locator)
        element_to_click.click()

    def open_page(self):
        """Call the base Page open function to go to the provided url
        when an instance is created.
        """
        return self.open(self.url)

    def open(self, url):
        """open the page to the url using webdriver's get function.

        Args:
            url (str): url of page to append to page base url
        """
        url = self.base_url + url
        self.driver.get(url)

    def switch_to_window(self, number):
        """Switch to the open window
        Args:
            number (int) : the window number specified, in the order of how it is opened.
        """

        self.driver.switch_to_window(self.driver.window_handles[number - 1])

    def open_new_window(self):
        """Open a new window for the simple-chat-app
        """
        self.driver.execute_script('window.open("https://simple-chat-asapp.herokuapp.com/")')
