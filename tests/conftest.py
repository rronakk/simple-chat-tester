"""
The conftest module allows for specifying test run configurables at runtime
such as the sender, receiver, base-url, browser etc. In the absence of command
line options, the config passed to default config will be used. Additionally
the config argument accepts a config with settings to override defaults.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from tests import utils
from src.pages import join_chat_page


def pytest_addoption(parser):
    """get parameters from command line using fixture function

    Args:
        parser (TYPE): Description
    """

    parser.addoption("--config", action="store", nargs='?',
                     type=str, default='config.base',
                     help='the config you\'d like to use')


@pytest.fixture
def browser_type(request):
    """Set fixture of browser_type to provided argument

    Args:
        request (object): conftest object to introspect test environment
    """

    _browser = utils.get_config_var('BROWSER',
                                    utils.process_config_file(request))
    return _browser


@pytest.fixture
def base_url(request):
    """Set fixture of BASE_URL to provided argument

    Args:
        request (object): conftest object to introspect test environment
    """

    _base_url = utils.get_config_var('BASE_URL',
                                     utils.process_config_file(request))
    return _base_url


@pytest.yield_fixture
def driver(browser_type):
    """return a webdriver instance for testing

    Args:
        browser_type (str): type of browser for test to run
            (i.e. Chrome, Firefox, Safari, Ie, etc.)

    Raises:
        AttributeError: Raise if browser type unavailable
    """
    if browser_type == "Chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")
        _driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        try:
            _driver = getattr(webdriver, browser_type)()
        except AttributeError:
            raise AttributeError
    yield _driver
    _driver.quit()


@pytest.fixture
def landing_page(driver, base_url, timeout):
    """returns the main page

    Args:
        driver (object): browser defined in browser conftest fixture
        base_url (str): base_url defined in base_url conftest fixture
        timeout (int) : timeout defined in timeout conftest fixture
    """
    main_page = join_chat_page.JoinChatPage(driver, base_url, timeout)
    main_page.open_page()
    return main_page.return_join_chat_page()


@pytest.fixture
def timeout(request):
    """Set fixture of timeout to provided argument or default

    Args:
        request (object): conftest object to introspect test environment
    """

    _timeout = utils.get_config_var('TIMEOUT',
                                    utils.process_config_file(request))
    return _timeout
