# imports

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


@pytest.fixture
def browser(scope="session"):  # session -> once before the test suite.

    # Initialize webdriver instance with maximized window
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = Chrome(options=options)

    yield browser

    browser.quit()
