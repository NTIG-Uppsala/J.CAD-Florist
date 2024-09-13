from utils import *


class TestDynamicOpenHoursDays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testDynamicOpenHoursDisplayMonday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 9, 9, 59, matches=["Stängt, vi öppnar kl 10 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 10, 0, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 17, 59, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 18, 0, matches=["Stängt, vi öppnar kl 10 på tisdag"])

    def testDynamicOpenHoursDisplayTuesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 10, 9, 59, matches=["Stängt, vi öppnar kl 10 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 10, 0, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 17, 59, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 18, 0, matches=["Stängt, vi öppnar kl 10 på onsdag"])

    def testDynamicOpenHoursDisplayWednesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 11, 9, 59, matches=["Stängt, vi öppnar kl 10 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 10, 0, matches=["Öppet, vi stänger kl 17 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 16, 59, matches=["Öppet, vi stänger kl 17 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 17, 0, matches=["Stängt, vi öppnar kl 10 på torsdag"])

    def testDynamicOpenHoursDisplayThursday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 12, 9, 59, matches=["Stängt, vi öppnar kl 10 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 10, 0, matches=["Öppet, vi stänger kl 17 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 16, 59, matches=["Öppet, vi stänger kl 17 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 17, 0, matches=["Stängt, vi öppnar kl 10 på fredag"])

    def testDynamicOpenHoursDisplayFriday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 13, 9, 59, matches=["Stängt, vi öppnar kl 10 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 10, 0, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 17, 59, matches=["Öppet, vi stänger kl 18 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 18, 0, matches=["Stängt, vi öppnar kl 12 på lördag"])

    def testDynamicOpenHoursDisplaySaturday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 14, 9, 59, matches=["Stängt, vi öppnar kl 12 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 12, 0, matches=["Öppet, vi stänger kl 16 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 15, 59, matches=["Öppet, vi stänger kl 16 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 16, 0, matches=["Stängt, vi öppnar kl 12 på söndag"])

    def testDynamicOpenHoursDisplaySunday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 15, 9, 59, matches=["Stängt, vi öppnar kl 12 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 12, 0, matches=["Öppet, vi stänger kl 15 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 14, 59, matches=["Öppet, vi stänger kl 15 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 15, 0, matches=["Stängt, vi öppnar kl 10 på måndag"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
