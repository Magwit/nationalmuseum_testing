# imports

import pytest
import selenium.webdriver


# pytest fixture config(scope="session")
# config had headless browsers and value for all implicit waits.
# maybe not needed


@pytest.fixture
def browser(scope="session"):  # session -> once before the test suite.

    # Initialize webdriver instance
    browser = selenium.webdriver.Chrome()

    # optional implicit wait
    browser.implicitly_wait(10)

    yield browser

    browser.quit()
