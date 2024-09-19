from utils import *


class TestDealOfTheDay(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the deal of the day is displayed on Monday
    def testDealsMonday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 16, 12, 0, matches=["Tulpaner 10-pack", "89 kr"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Tuesday
    def testDealsTuesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 17, 12, 0, matches=["Liljor", "19 kr/st"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Wednesday
    def testDealsWednesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 18, 12, 0, matches=["Hortensia", "39 kr"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Thursday
    def testDealsThursday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 19, 12, 0, matches=["Aloe vera", "79 kr"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Friday
    def testDealsFriday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 20, 12, 0, matches=["Kaktus i kruka", "79 kr"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Saturday
    def testDealsSaturday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 21, 12, 0, matches=["Rosor 10-pack", "127 kr"])
        deals = list(self.page.locator(".deal-of-the-day.active").all())
        print(deals)
        self.assertEqual(len(deals), 1)

    # Test that the deal of the day is displayed on Sunday
    def testDealsSunday(self) -> None:
        # deals = list(self.page.locator(".deal-of-the-day.active").all())
        deals = [item for item in self.page.locator(".deal-of-the-day.active")]
        self.page.get_by_label
        print(deals)
        self.assertEqual(len(deals), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
