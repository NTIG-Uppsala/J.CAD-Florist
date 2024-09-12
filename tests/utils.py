import unittest
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from os import path


class TestWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def setUp(self, pathFromRoot) -> None:
        path = path.abspath(path.join(path.dirname(__file__), "..", pathFromRoot))
        self.page.goto(f"file://{path}")
        self.page.wait_for_selector("#JSLoaded")

    def tearDown(self) -> None:
        self.page.goto("about:blank")

    # Helper functions

    def getHTML(self, page: str) -> str:
        soup = BeautifulSoup(page, "html.parser")
        for element in soup.find_all():
            element.clear()

        return str(soup)

    # Assert functions

    def assertInText(self, match: str) -> None:
        self.assertIn(match, self.page.text_content("body"))

    def assertInHTML(self, match: str) -> None:
        self.assertIn(match, self.getHTML(self.page.content()))

    def assertNotInText(self, match: str) -> None:
        self.assertNotIn(match, self.page.text_content("body"))

    def assertNotInHTML(self, match: str) -> None:
        self.assertNotIn(match, self.getHTML(self.page.content()))
