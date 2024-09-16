from utils import *


class TestDynamicOpenHoursDays(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Tests that the open hours are displayed correctly during different times of Monday
    def testDynamicOpenHoursDisplayMonday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 9, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 10, 0, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 17, 59, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 9, 18, 0, matches=["Vi har stängt. Vi öppnar kl. 10:00 på tisdag"])

    # Tests that the open hours are displayed correctly during different times of Tuesday
    def testDynamicOpenHoursDisplayTuesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 10, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 10, 0, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 17, 59, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 10, 18, 0, matches=["Vi har stängt. Vi öppnar kl. 10:00 på onsdag"])

    # Tests that the open hours are displayed correctly during different times of Wednesday
    def testDynamicOpenHoursDisplayWednesday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 11, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 10, 0, matches=["Vi har öppet. Vi stänger kl. 17:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 16, 59, matches=["Vi har öppet. Vi stänger kl. 17:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 11, 17, 0, matches=["Vi har stängt. Vi öppnar kl. 10:00 på torsdag"])

    # Tests that the open hours are displayed correctly during different times of Thursday
    def testDynamicOpenHoursDisplayThursday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 12, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 10, 0, matches=["Vi har öppet. Vi stänger kl. 17:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 16, 59, matches=["Vi har öppet. Vi stänger kl. 17:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 12, 17, 0, matches=["Vi har stängt. Vi öppnar kl. 10:00 på fredag"])

    # Tests that the open hours are displayed correctly during different times of Friday
    def testDynamicOpenHoursDisplayFriday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 13, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 10:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 10, 0, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 17, 59, matches=["Vi har öppet. Vi stänger kl. 18:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 13, 18, 0, matches=["Vi har stängt. Vi öppnar kl. 12:00 på lördag"])

    # Tests that the open hours are displayed correctly during different times of Saturday
    def testDynamicOpenHoursDisplaySaturday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 14, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 12:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 12, 0, matches=["Vi har öppet. Vi stänger kl. 16:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 15, 59, matches=["Vi har öppet. Vi stänger kl. 16:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 14, 16, 0, matches=["Vi har stängt. Vi öppnar kl. 12:00 på söndag"])

    # Tests that the open hours are displayed correctly during different times of Sunday
    def testDynamicOpenHoursDisplaySunday(self) -> None:
        self.setTimeAndAssertMatches(2024, 9, 15, 9, 59, matches=["Vi har stängt. Vi öppnar kl. 12:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 12, 0, matches=["Vi har öppet. Vi stänger kl. 15:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 14, 59, matches=["Vi har öppet. Vi stänger kl. 15:00 idag"])
        self.setTimeAndAssertMatches(2024, 9, 15, 15, 0, matches=["Vi har stängt. Vi öppnar kl. 10:00 på måndag"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
