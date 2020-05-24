"""
This test covers starting at the homepage
scrolling down and clicking in the Free Images tile
"""


from pages.homepage import HomePage
from pages.free_images import FreeImages


def test_homepage_to_free_images(browser):
    homepage = HomePage(browser)
    free_images = FreeImages(browser)

    # GIVEN Nationalmuseum homepage is displayed
    homepage.load()

    # WHEN whe user scrolls down to the Free Images tile
    homepage.scroll_to_free_images_tile()

    # AND clicks on the Freeimages tile

    homepage.click_on_free_images_tile()

    # THEN the user is at Nattionalmuseum Free Images page

    assert "" in free_images.title()

    # ADDITIONALY cookies are deleted

    # TODO remove this exception once the test is completed
    raise Exception("Incomplete test")
