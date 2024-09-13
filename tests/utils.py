import unittest
from playwright.sync_api import sync_playwright
from lxml import etree, html
from os import path


class TestBase(unittest.TestCase):

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

    def setUp(self, filePathFromRoot: str) -> None:
        filePath = path.abspath(path.join(path.dirname(__file__), "..", filePathFromRoot))
        self.page.goto(f"file://{filePath}")
        self.page.wait_for_selector("#JSLoaded", state="attached")

    def tearDown(self) -> None:
        self.page.goto("about:blank")

    # Helper functions

    def getHTML(self) -> str:
        tree = html.fromstring(self.page.content(), parser=etree.HTMLParser())
        for element in tree.iter():
            if element.text:
                element.text = None
            if element.tail:
                element.tail = None
        return html.tostring(tree, pretty_print=True, method="html", encoding="unicode")

    def setTime(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        self.page.evaluate(
            f"""
            now.setFullYear({year}, {month - 1}, {day});
            now.setHours({hour}, {minute});
            updateCurrentStatus();
            """
        )

    def setTimeAndAssertMatch(self, year: int, month: int, day: int, hour: int, minute: int, match: str) -> None:
        self.setTime(year, month, day, hour, minute)
        self.assertInText(match)

    def setTimeAndAssertMatches(self, year: int, month: int, day: int, hour: int, minute: int, matches: list[str]) -> None:
        self.setTime(year, month, day, hour, minute)
        self.assertAllInText(matches)

    def fillAndSubmitAndAssertInText(self, fieldSelector: str, buttonSelector: str, fieldInput: str, match: str) -> None:
        self.page.fill(fieldSelector, fieldInput)
        self.page.click(buttonSelector)
        self.assertInText(match)

    def submitAndAssertZIPCodeValidityInText(self, fieldInput: str, match: str) -> None:
        button = self.page.query_selector("#flowergram-btn")
        button.click()
        self.fillAndSubmitAndAssertInText("#postal-code", "#postal-code-btn", fieldInput, match)
        button.click()

    def assertInText(self, match: str) -> None:
        self.assertIn(match, self.page.text_content("body"))

    def assertAllInText(self, matches: list[str]) -> None:
        for match in matches:
            self.assertInText(match)

    def assertInHTML(self, match: str) -> None:
        self.assertIn(match, self.getHTML())

    def assertAllInHTML(self, matches: list[str]) -> None:
        for match in matches:
            self.assertInHTML(match)

    def assertNotInText(self, match: str) -> None:
        self.assertNotIn(match, self.page.text_content("body"))

    def assertAllNotInText(self, matches: list[str]) -> None:
        for match in matches:
            self.assertNotInText(match)

    def assertNotInHTML(self, match: str) -> None:
        self.assertNotIn(match, self.getHTML())

    def assertAllNotInHTML(self, matches: list[str]) -> None:
        for match in matches:
            self.assertNotInHTML(match)
