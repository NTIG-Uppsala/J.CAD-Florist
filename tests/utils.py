import unittest
from playwright.sync_api import sync_playwright, expect
from lxml import etree, html
from os import path


class TestBase(unittest.TestCase):

    @classmethod
    # Set up the browser and page before running the tests
    def setUpClass(self, jsEnabled: bool = True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context(java_script_enabled=jsEnabled)  # enable JavaScript by default
        self.page = self.context.new_page()

    # Close the browser and page after running the tests
    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    # Set up the page before each test
    def setUp(self, filePathFromRoot: str, jsEnabled: bool = True) -> None:
        filePath = path.abspath(path.join(path.dirname(__file__), "..", filePathFromRoot))
        self.page.goto(f"file://{filePath}", wait_until="domcontentloaded", timeout=60000)
        if jsEnabled:  # wait for JavaScript to load if enabled
            self.page.wait_for_selector("#JSLoaded", state="attached")

    # Close the page after each test
    def tearDown(self) -> None:
        self.page.goto("about:blank")

    # Helper functions

    # Returns all HTML tags on the page
    def getHTML(self) -> str:
        tree = html.fromstring(self.page.content(), parser=etree.HTMLParser())
        for element in tree.iter():
            if element.text:
                element.text = None
            if element.tail:
                element.tail = None
        return html.tostring(tree, pretty_print=True, method="html", encoding="unicode")

    # Sets the time on the page
    def setTime(self, year: int, month: int, day: int, hour: int, minute: int) -> None:
        self.page.evaluate(
            f"""
            now.setFullYear({year}, {month - 1}, {day});
            now.setHours({hour}, {minute});
            updateCurrentStatus();
            setDealOfTheDay();
            sortClosedDays();
            """
        )

    # Sets the time on the page and asserts that the given match is in the text content
    def setTimeAndAssertMatch(self, year: int, month: int, day: int, hour: int, minute: int, match: str) -> None:
        self.setTime(year, month, day, hour, minute)
        self.assertInText(match)

    # Sets the time on the page and asserts that all the given matches are in the text content
    def setTimeAndAssertMatches(self, year: int, month: int, day: int, hour: int, minute: int, matches: list[str]) -> None:
        self.setTime(year, month, day, hour, minute)
        self.assertAllInText(matches)

    # Checks that the number of elements with the given selector is equal to the given number of expected occurrences
    def checkNumberOfElements(self, selector: str, expected: int) -> None:
        elementCount = self.page.locator(selector).count()
        self.assertEqual(elementCount, expected)

    # Sets the time on the page and checks that the number of elements with the given selector is equal to the given number of expected occurrences
    def setTimeAndCheckNumberOfElements(self, year: int, month: int, day: int, hour: int, minute: int, selector: str, expected: int) -> None:
        self.setTime(year, month, day, hour, minute)
        self.checkNumberOfElements(selector, expected)

    # Fills a field, submits the form, and asserts that the given match is in the text content
    def fillAndSubmitAndAssertInText(self, fieldSelector: str, buttonSelector: str, fieldInput: str, match: str) -> None:
        self.page.fill(fieldSelector, fieldInput)
        self.page.click(buttonSelector)
        self.assertInText(match)

    # Opens the flowergram form, fills the ZIP code field, submits the form, and asserts that the given match is in the text content
    def submitAndAssertZIPCodeValidityInText(self, fieldInput: str, match: str) -> None:
        button = self.page.query_selector("#flowergram-btn")
        button.click()
        self.fillAndSubmitAndAssertInText("#postal-code", "#postal-code-btn", fieldInput, match)
        button.click()

    # Sets the time on the page and asserts that the given match is in the text content in the given order
    def setTimeAndAssertInTextInOrder(self, year: int, month: int, day: int, hour: int, minute, matches: list[str]) -> None:
        self.setTime(year, month, day, hour, minute)
        self.assertInTextInOrder(matches)

    # Assertions

    # Asserts that the given match is in the text content
    def assertInText(self, match: str) -> None:
        self.assertIn(match, self.page.text_content("body"))

    # Asserts that all the given matches are in the text content
    def assertAllInText(self, matches: list[str]) -> None:
        for match in matches:
            self.assertInText(match)

    # Asserts that the given match is in the HTML content
    def assertInHTML(self, match: str) -> None:
        self.assertIn(match, self.getHTML())

    # Asserts that all the given matches are in the HTML content
    def assertAllInHTML(self, matches: list[str]) -> None:
        for match in matches:
            self.assertInHTML(match)

    # Asserts that the given match is not in the text content
    def assertNotInText(self, match: str) -> None:
        self.assertNotIn(match, self.page.text_content("body"))

    # Asserts that all the given matches are not in the text content
    def assertAllNotInText(self, matches: list[str]) -> None:
        for match in matches:
            self.assertNotInText(match)

    # Asserts that the given match is not in the HTML content
    def assertNotInHTML(self, match: str) -> None:
        self.assertNotIn(match, self.getHTML())

    # Asserts that all the given matches are not in the HTML content
    def assertAllNotInHTML(self, matches: list[str]) -> None:
        for match in matches:
            self.assertNotInHTML(match)

    # Asserts that the given matches are in the text content in the given order
    def assertInTextInOrder(self, matches: list[str]) -> None:
        text = self.page.text_content("body")
        for index, match in enumerate(matches[:-1]):
            self.assertLess(text.index(match), text.index(matches[index + 1]))
