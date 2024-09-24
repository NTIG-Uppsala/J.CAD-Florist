from utils import *


class TestDynamicInformaion(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testHeaderDealOfTheDay(self) -> None:
        self.setTimeAndAssertInTextInLocator(2024, 9, 24, 10, 35, "#dynamic-information", "Idag kostar")

    def testHeaderDealOfTheDayNotVisibleSunday(self) -> None:
        self.setTime(2024, 9, 29, 10, 35)
        self.assertFalse(self.page.is_visible("#dynamic-information-container"))

    def testHeaderDynamicInformationNotVisible(self) -> None:
        self.setTime(2024, 12, 24, 10, 7)
        self.assertFalse(self.page.is_visible("#dynamic-information-container"))


if __name__ == "__main__":
    unittest.main(verbosity=2)