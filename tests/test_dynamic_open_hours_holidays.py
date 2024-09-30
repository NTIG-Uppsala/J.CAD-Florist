from utils import *


class TestDynamicOpenHoursHolidays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/se/index.html")

    # Tests that the open hours are displayed on New Year's Day
    def testDynamicOpenHoursDisplayNewYearsDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 1, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på tisdag"])
        self.setTimeAndAssertMatches(2024, 1, 2, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])

    # Tests that the open hours are displayed on Epiphany
    def testDynamicOpenHoursDisplayEpiphany(self) -> None:
        self.setTimeAndAssertMatches(2024, 1, 6, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 12:00 på söndag"])
        self.setTimeAndAssertMatches(2024, 1, 7, 11, 59, matches=["Vi har stängt. Vi öppnar kl. 12:00 idag"])

    # Tests that the open hours are displayed on May Day
    def testDynamicOpenHoursDisplayMayDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 5, 1, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på torsdag"])
        self.setTimeAndAssertMatches(2024, 5, 2, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])

    # Tests that the open hours are displayed on the National Day of Sweden
    def testDynamicOpenHoursDisplayNationalDayOfSweden(self) -> None:
        self.setTimeAndAssertMatches(2024, 6, 6, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])
        self.setTimeAndAssertMatches(2024, 6, 7, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])

    # Tests that the open hours are displayed on Christmas Eve
    def testDynamicOpenHoursDisplayChristmasEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 24, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])
        self.setTimeAndAssertMatches(2024, 12, 25, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])

    # Tests that the open hours are displayed on Christmas Day
    def testDynamicOpenHoursDisplayChristmasDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 25, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])
        self.setTimeAndAssertMatches(2024, 12, 26, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])

    # Tests that the open hours are displayed on Boxing Day
    def testDynamicOpenHoursDisplayBoxingDay(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 26, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på fredag"])
        self.setTimeAndAssertMatches(2024, 12, 27, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])

    # Tests that the open hours are displayed on New Year's Eve
    def testDynamicOpenHoursDisplayNewYearsEve(self) -> None:
        self.setTimeAndAssertMatches(2024, 12, 31, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på torsdag"])
        self.setTimeAndAssertMatches(2025, 1, 1, 9, 59, matches=["Idag har vi stängt p.g.a helgdag. Vi öppnar kl. 10:00 på torsdag"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
