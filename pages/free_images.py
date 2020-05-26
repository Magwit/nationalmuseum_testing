from selenium.webdriver.common.by import By
import time  # TODO remove sleep in final version

from pages.basepage import BasePage


class FreeImages(BasePage):

    # URL
    URL = "https://www.nationalmuseum.se/samlingarna/fria-bilder"

    # Locators
    WIKIMEDIA_TILE = (
        By.XPATH,
        "//a[@href='https://commons.wikimedia.org/wiki/Category:Media_contributed_by_Nationalmuseum_Stockholm:_2016-10' and @class='link-container']",
    )

    # def load(self):
    #     self.browser.get(self.URL)

    # Interaction methods

    # def scroll_to_wikimedia_tile(self):
    #     self.wikimedia_tile = self.browser.find_element(*self.WIKIMEDIA_TILE)
    #     self.browser.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'})", self.wikimedia_tile
    #     )

    # def click_wikimedia_tile(self):
    #     self.browser.implicitly_wait(10)
    #     self.browser.execute_script("arguments[0].click()", self.wikimedia_tile)

    # return methods

    # NOTE carefulu not to call title method after clickin on wikimedia link
    def title(self):
        time.sleep(5)
        return self.browser.title
