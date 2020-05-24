# page objects can have actions and also return values
# A
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    # URL
    URL = "https://www.nationalmuseum.se/"

    # Locators
    FREE_IMAGES_TILE = (
        By.XPATH,
        "//div[@class='blurb-link']/a[@href='https://www.nationalmuseum.se/samlingarna/fria-bilder' and @tabindex='0']",
    )

    # Initializer and setting state
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # Interaction modules
    def scroll_to_free_images_tile(self):

        free_images_tile = self.browser.find_element(*self.FREE_IMAGES_TILE)

        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", free_images_tile
        )

    def click_on_free_images_tile(self):
        self.browser.implicitly_wait(10)
        free_images_tile = self.browser.find_element(*self.FREE_IMAGES_TILE)
        self.browser.execute_script("arguments[0].click()", free_images_tile)
        time.sleep(8)
