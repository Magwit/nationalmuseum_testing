from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):

    # URL
    URL = "https://www.nationalmuseum.se/"

    # Locators
    FREE_IMAGES_TILE = (
        By.XPATH,
        "//div[@class='blurb-link']/a[@href='https://www.nationalmuseum.se/samlingarna/fria-bilder' and @tabindex='0']",
    )

    # Return methods
    # def title(self):
    #     time.sleep(5)
    #     return self.browser.title
