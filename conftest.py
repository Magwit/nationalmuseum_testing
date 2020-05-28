# imports

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


# pytest fixture config(scope="session")
# config had headless browsers and value for all implicit waits.
# maybe not needed


@pytest.fixture
def browser(scope="session"):  # session -> once before the test suite.

    # Initialize webdriver instance with maximized window
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = Chrome(options=options)

    # optional implicit wait
    browser.implicitly_wait(10)

    yield browser

    browser.quit()
