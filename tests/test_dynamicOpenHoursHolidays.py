from utils import *


class TestDynamicOpenHoursHolidays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testDynamicOpenHoursDisplayNewYearsDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 1, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på tisdag"])

    def testDynamicOpenHoursDisplayEpiphany(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 6, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 12 på söndag"])

    def testDynamicOpenHoursDisplayMayDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 5, 1, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på torsdag"])

    def testDynamicOpenHoursDisplayNationalDayOfSweden(self) -> None:
        self.setTimeAndAssertMatches(2024, 6, 6, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på fredag"])

    def testDynamicOpenHoursDisplayChristmasEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 24, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på fredag"])

    def testDynamicOpenHoursDisplayChristmasDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 25, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på fredag"])

    def testDynamicOpenHoursDisplayBoxingDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 26, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på fredag"])

    def testDynamicOpenHoursDisplayNewYearsEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 31, 9, 59, matches=["Stängt för helgdag, vi öppnar kl 10 på torsdag"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
