from utils import *


class TestMapEmbed(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/se/index.html")

    # Test that the OSM map is displayed correctly
    def testMapEmbed(self) -> None:
        self.assertAllInHTML(
            '<iframe class="map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1503.2561387938995!2d20.23140837816331!3d67.8660575009758!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x45d0ba6368d7c9a3%3A0xe3887ef038c559b0!2sFj%C3%A4llgatan%2032%2C%20981%2039%20Kiruna!5e0!3m2!1ssv!2sse!4v1694676651494!5m2!1ssv!2sse" style="border:0; width: 100%; border-radius: 7px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
