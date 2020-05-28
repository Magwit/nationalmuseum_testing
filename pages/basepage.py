import time


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        return self.browser.get(url)

    def scroll_to(self, locator):
        self.locator = self.browser.find_element(*locator)
        return self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", self.locator
        )

    def click_tile(self):
        # locator = self.browser.find_element(*locator)
        # self.browser.implicitly_wait(10)
        time.sleep(3)
        return self.browser.execute_script("arguments[0].click()", self.locator)

    def get_title(self):
        # self.browser.implicitly_wait(10)
        time.sleep(3)
        return self.browser.title
