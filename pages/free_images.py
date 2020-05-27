from selenium.webdriver.common.by import By

# import time  # TODO remove sleep in final version

from pages.basepage import BasePage


class FreeImages(BasePage):

    # URL
    URL = "https://www.nationalmuseum.se/samlingarna/fria-bilder"

    # Locators
    WIKIMEDIA_TILE = (
        By.XPATH,
        "//a[@href='https://commons.wikimedia.org/wiki/Category:Media_contributed_by_Nationalmuseum_Stockholm:_2016-10' and @class='link-container']",
    )

    # def title(self):
    #     time.sleep(5)
    #     return self.browser.title
