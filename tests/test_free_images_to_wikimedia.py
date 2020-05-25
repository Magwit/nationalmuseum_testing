"""
This test covers starting at Nationalmuseum free images page
scrolling down and clicking on the Wikimedia link 
"""

from pages.free_images import FreeImages


# TODO create a separate Wikimedia page object
# or test everything on here?
def test_free_images_to_wikimedia(browser):
    free_images = FreeImages(browser)

    # GIVEN Nationalmuseum free images page is displayed
    free_images.load()

    # WHEN the user scrolls down to the Wikimedia tile
    free_images.scroll_to_wikimedia_tile()

    # AND clicks on the Wikimedia tile
    free_images.click_wikimedia_tile()

    # THEN the user is at Wikimedia commons

    assert (
        free_images.title()
        == "Category:Media contributed by Nationalmuseum Stockholm: 2016-10 - Wikimedia Commons"
    )
    # And images from Nationalmuseum are displayed
