from utils import *


class TestOpenHours(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the open hours are displayed
    def testOpenHours(self) -> None:
        self.assertInText("Öppettider")
        self.assertInText("Måndag")
        self.assertInText("Tisdag")
        self.assertInText("Onsdag")
        self.assertInText("Torsdag")
        self.assertInText("Fredag")
        self.assertInText("Lördag")
        self.assertInText("Söndag")
        self.assertInText("10-18")
        self.assertInText("10-17")
        self.assertInText("12-16")
        self.assertInText("12-15")

    # Test that the closed days are displayed
    def testClosedDays(self) -> None:
        self.assertInText("1 jan")
        self.assertInText("6 jan")
        self.assertInText("1 maj")
        self.assertInText("6 jun")
        self.assertInText("24 dec")
        self.assertInText("25 dec")
        self.assertInText("26 dec")
        self.assertInText("31 dec")
        self.assertInText("Nyårsdagen")
        self.assertInText("Trettondedag jul")
        self.assertInText("Första maj")
        self.assertInText("Nationaldagen")
        self.assertInText("Julafton")
        self.assertInText("Juldagen")
        self.assertInText("Annandag jul")
        self.assertInText("Nyårsafton")


if __name__ == "__main__":
    unittest.main(verbosity=2)
