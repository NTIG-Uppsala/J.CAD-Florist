from utils import *


class TestDynamicOpenHoursHolidays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Tests that the open hours are displayed on New Year's Day
    def testDynamicOpenHoursDisplayNewYearsDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 1, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på tisdag"])

    # Tests that the open hours are displayed on Epiphany
    def testDynamicOpenHoursDisplayEpiphany(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 6, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 12:00 på söndag"])

    # Tests that the open hours are displayed on May Day
    def testDynamicOpenHoursDisplayMayDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 5, 1, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på torsdag"])

    # Tests that the open hours are displayed on the National Day of Sweden
    def testDynamicOpenHoursDisplayNationalDayOfSweden(self) -> None:
        self.setTimeAndAssertMatches(2024, 6, 6, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på fredag"])

    # Tests that the open hours are displayed on Christmas Eve
    def testDynamicOpenHoursDisplayChristmasEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 24, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på fredag"])

    # Tests that the open hours are displayed on Christmas Day
    def testDynamicOpenHoursDisplayChristmasDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 25, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på fredag"])

    # Tests that the open hours are displayed on Boxing Day
    def testDynamicOpenHoursDisplayBoxingDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 26, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på fredag"])

    # Tests that the open hours are displayed on New Year's Eve
    def testDynamicOpenHoursDisplayNewYearsEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 31, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10:00 på torsdag"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
