from selenium.webdriver.common.by import By
import time  # TODO remove sleep in final version

from pages.basepage import BasePage


class HomePage(BasePage):

    # URL
    URL = "https://www.nationalmuseum.se/"

    # Locators
    FREE_IMAGES_TILE = (
        By.XPATH,
        "//div[@class='blurb-link']/a[@href='https://www.nationalmuseum.se/samlingarna/fria-bilder' and @tabindex='0']",
    )

    # Interaction methods
    # def scroll_to_free_images_tile(self):
    #     self.free_images_tile = self.browser.find_element(*self.FREE_IMAGES_TILE)
    #     self.browser.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'})", self.free_images_tile
    #     )

    # def click_free_images_tile(self):
    #     self.browser.implicitly_wait(10)
    #     self.browser.execute_script("arguments[0].click()", self.free_images_tile)

    # Return methods
    def title(self):
        time.sleep(5)
        return self.browser.title
