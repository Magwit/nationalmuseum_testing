import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def load(self, url):
        return self.browser.get(url)

    def scroll_to(self, locator):
        # time.sleep(4)
        try:
            self.wait.until(
                EC.presence_of_element_located(self.browser.find_element(*locator))
            )
        except Exception as e:
            print(type(e))
            print(e.args)

        self.locator = self.browser.find_element(*locator)
        return self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", self.locator
        )

    def click_tile(self):
        # locator = self.browser.find_element(*locator)
        # self.browser.implicitly_wait(10)
        # time.sleep(3)
        return self.browser.execute_script("arguments[0].click()", self.locator)

    def get_title(self, title):
        # self.browser.implicitly_wait(10)
        # time.sleep(3)
        try:
            self.wait.until(EC.title_is(title))
        except Exception as e:
            print(type(e))
            print(e.args)
        return self.browser.title
