"""
This test covers starting at Nationalmuseum free images page
scrolling down and clicking on the Wikimedia link 
"""


from pages.free_images import FreeImages


def test_free_images_to_wikimedia(browser):
    free_images = FreeImages(browser)

    # GIVEN Nationalmuseum free images page is displayed
    free_images.load(FreeImages.URL)

    # WHEN the user scrolls down to the Wikimedia tile
    free_images.scroll_to(FreeImages.WIKIMEDIA_TILE)

    # AND clicks on the Wikimedia tile
    free_images.click_tile()

    # THEN the user is at Wikimedia commons
    title = "Category:Media contributed by Nationalmuseum Stockholm: 2016-10 - Wikimedia Commons"
    assert free_images.get_title(title) == title
