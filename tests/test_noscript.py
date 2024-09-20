from utils import *

class TestNoscript(TestBase):

    @classmethod
    # Set up the browser and page without javascript before running the tests
    def setUpClass(self):
        super().setUpClass(jsEnabled=False)
    #     self.playwright = sync_playwright().start()
    #     self.browser = self.playwright.chromium.launch(headless=True)
    #     self.context = self.browser.new_context(java_script_enabled=False)
    #     self.page = self.context.new_page()

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html", jsEnabled=False)

    def testMap(self) -> None:
        self.checkNumberOfElements("#noscript-map", 1)
        self.assertInHTML('img src="images/noscript-map.png" alt="noscript-map"')