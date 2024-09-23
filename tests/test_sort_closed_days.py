from utils import *


class TestClosedDays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the closed days are sorted correctly on New Year's Day
    def testNewYearsDay(self):
        self.setTimeAndAssertInTextInOrder(2022, 1, 1, 12, 0, matches=["Nyårsdagen", "Trettondedag jul", "Första maj", "Nationaldagen", "Julafton", "Juldagen", "Annandag jul", "Nyårsafton"])

    # Test that the closed days are sorted correctly on Epiphany
    def testEpiphany(self):
        self.setTimeAndAssertInTextInOrder(2022, 1, 6, 12, 0, matches=["Trettondedag jul", "Första maj", "Nationaldagen", "Julafton", "Juldagen", "Annandag jul", "Nyårsafton", "Nyårsdagen"])

    # Test that the closed days are sorted correctly on May Day
    def testMayDay(self):
        self.setTimeAndAssertInTextInOrder(2022, 5, 1, 12, 0, matches=["Första maj", "Nationaldagen", "Julafton", "Juldagen", "Annandag jul", "Nyårsafton", "Nyårsdagen", "Trettondedag jul"])

    # Test that the closed days are sorted correctly on the National Day
    def testNationalDay(self):
        self.setTimeAndAssertInTextInOrder(2022, 6, 6, 12, 0, matches=["Nationaldagen", "Julafton", "Juldagen", "Annandag jul", "Nyårsafton", "Nyårsdagen", "Trettondedag jul", "Första maj"])

    # Test that the closed days are sorted correctly on Christmas Eve
    def testChristmasEve(self):
        self.setTimeAndAssertInTextInOrder(2022, 12, 24, 12, 0, matches=["Julafton", "Juldagen", "Annandag jul", "Nyårsafton", "Nyårsdagen", "Trettondedag jul", "Första maj", "Nationaldagen"])

    # Test that the closed days are sorted correctly on Christmas Day
    def testChristmasDay(self):
        self.setTimeAndAssertInTextInOrder(2022, 12, 25, 12, 0, matches=["Juldagen", "Annandag jul", "Nyårsafton", "Nyårsdagen", "Trettondedag jul", "Första maj", "Nationaldagen", "Julafton"])

    # Test that the closed days are sorted correctly on Boxing Day
    def testBoxingDay(self):
        self.setTimeAndAssertInTextInOrder(2022, 12, 26, 12, 0, matches=["Annandag jul", "Nyårsafton", "Nyårsdagen", "Trettondedag jul", "Första maj", "Nationaldagen", "Julafton", "Juldagen"])

    # Test that the closed days are sorted correctly on New Year's Eve
    def testNewYearsEve(self):
        self.setTimeAndAssertInTextInOrder(2022, 12, 31, 12, 0, matches=["Nyårsafton", "Nyårsdagen", "Trettondedag jul", "Första maj", "Nationaldagen", "Julafton", "Juldagen", "Annandag jul"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
