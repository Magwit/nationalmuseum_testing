from selenium.webdriver.common.by import By
import time  # TODO remove sleep in final version


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

    # Interaction methods
    def scroll_to_free_images_tile(self):
        # using self to scope to class -> instance variable as the locator is re-used
        # TODO ask if this is an antipattern or just quirky
        # DONE https://qaboy.com/2018/01/22/test-automation-framework-with-python-part-2/
        self.free_images_tile = self.browser.find_element(*self.FREE_IMAGES_TILE)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", self.free_images_tile
        )

    def click_free_images_tile(self):
        self.browser.implicitly_wait(10)
        # free_images_tile = self.browser.find_element(*self.FREE_IMAGES_TILE)
        self.browser.execute_script("arguments[0].click()", self.free_images_tile)

    # Return methods
    def title(self):
        time.sleep(5)
        return self.browser.title
