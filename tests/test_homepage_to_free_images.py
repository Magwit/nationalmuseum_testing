"""
This test covers starting at the Nationalmuseum homepage
scrolling down and clicking in the Free Images tile
"""


from pages.homepage import HomePage
from pages.free_images import FreeImages


def test_homepage_to_free_images(browser):
    homepage = HomePage(browser)
    free_images = FreeImages(browser)

    # GIVEN Nationalmuseum homepage is displayed
    homepage.load(HomePage.URL)

    # WHEN whe user scrolls down to the Free Images tile
    homepage.scroll_to(HomePage.FREE_IMAGES_TILE)

    # AND clicks on the Freeimages tile

    homepage.click_tile()

    # THEN the user is at Nattionalmuseum Free Images page

    assert free_images.title() == "Fria bilder | Nationalmuseum"
    # NOTE I am not really testing a propery of the Free images page itself
    # assert homepage.title() == "Fria bilder | Nationalmuseum" also passes
    # The test asserts what the browser is doing at the moment.
