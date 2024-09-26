from utils import *


class TestDealOfTheDay(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the deal of the day is displayed on Monday
    def testDealsMonday(self) -> None:
        self.setTime(2024, 9, 16, 12, 0)
        self.assertAllInText(["Tulpaner 10-pack", "89 kr"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-tulpaner-10-pack")

    # Test that the deal of the day is displayed on Tuesday
    def testDealsTuesday(self) -> None:
        self.setTime(2024, 9, 17, 12, 0)
        self.assertAllInText(["Liljor", "19 kr/st"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-liljor")

    # Test that the deal of the day is displayed on Wednesday
    def testDealsWednesday(self) -> None:
        self.setTime(2024, 9, 18, 12, 0)
        self.assertAllInText(["Hortensia", "39 kr"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-hortensia")

    # Test that the deal of the day is displayed on Thursday
    def testDealsThursday(self) -> None:
        self.setTime(2024, 9, 19, 12, 0)
        self.assertAllInText(["Aloe vera", "79 kr"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-aloe-vera")

    # Test that the deal of the day is displayed on Friday
    def testDealsFriday(self) -> None:
        self.setTime(2024, 9, 20, 12, 0)
        self.assertAllInText(["Kaktus i kruka", "79 kr"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-kaktus-i-kruka")

    # Test that the deal of the day is displayed on Saturday
    def testDealsSaturday(self) -> None:
        self.setTime(2024, 9, 21, 12, 0)
        self.assertAllInText(["Rosor 10-pack", "127 kr"])
        self.checkNumberOfElements(selector=".active", expected=1)
        self.assertNth(".product", 0, "product-rosor-10-pack")

    # Test that the deal of the day is displayed on Sunday
    def testDealsSunday(self) -> None:
        self.setTime(2024, 9, 22, 12, 0)
        self.checkNumberOfElements(selector=".active", expected=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
