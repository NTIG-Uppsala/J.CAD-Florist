from utils import *


class TestZipCodes(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testFlorogramText(self) -> None:
        button = self.page.query_selector("#flowergram-btn")
        button.click()
        self.assertAllInText(
            [
                "Överraska med ett blommogram",
                "Vill du skicka ett blommogram?",
                "Besök oss i butiken eller ring oss på 0630-555-555!",
                "Kontrollera här om vi levererar till ditt önskade postnummer:",
            ]
        )

    def testValidZIPCodes(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("98138", "Vi levererar till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("98144", "Vi levererar till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("98147", "Vi levererar till detta postnummer!")

    def testEmptyZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("", "Du måste skriva in ett postnummer!")

    def testInvalidZIPCodes(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("12345", "Vi levererar tyvärr inte till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("54321", "Vi levererar tyvärr inte till detta postnummer!")

    def testInvalidCharactersInZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("abcde", "Du måste skriva in ett postnummer!")
        self.submitAndAssertZIPCodeValidityInText("ABCDE", "Du måste skriva in ett postnummer!")

    def testInvalidLengthZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("1234", "Postnumret måste vara 5 siffror!")
        self.submitAndAssertZIPCodeValidityInText("123456", "Postnumret måste vara 5 siffror!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
