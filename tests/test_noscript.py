from utils import *


class TestNoscript(TestBase):

    @classmethod
    # Set up the browser and page without javascript before running the tests
    def setUpClass(self):
        super().setUpClass(jsEnabled=False)

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/se/index.html", jsEnabled=False)

    # Check that the noscript image is displayed
    def testMap(self) -> None:
        self.checkNumberOfElements("#noscript-map", 1)
        self.assertInHTML('img loading="lazy" src="' + relativeRootDir + 'images/noscript-map.png" alt="Karta över butikens läge"')
