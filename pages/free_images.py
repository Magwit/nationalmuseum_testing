from selenium.webdriver.common.by import By
import time  # TODO remove sleep in final version


class FreeImages:

    # URL
    URL = "https://www.nationalmuseum.se/samlingarna/fria-bilder"

    # Locators
    WIKIMEDIA_TILE = (
        By.XPATH,
        "//a[@href='https://commons.wikimedia.org/wiki/Category:Media_contributed_by_Nationalmuseum_Stockholm:_2016-10' and @class='link-container']",
    )

    # Initializer and setting state
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # TODO load is needed for the last test case
        pass

    # Interaction methods

    def scroll_to_wikimedia_tile(self):
        # Declaring an instance variable which will be re used in the click function
        self.wikimedia_tile = self.browser.find_element(*self.WIKIMEDIA_TILE)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", self.wikimedia_tile
        )

    def click_wikimedia_tile(self):
        self.browser.implicitly_wait(10)
        self.browser.execute_script("arguments[0].click()", self.wikimedia_tile)
        time.sleep(8)

    # return methods
    def title(self):
        # TODO
        return ""
