from utils import *


class TestZipCodes(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testFlorogramText(self) -> None:
        button = self.page.query_selector(".flowerGramContainer>h4")
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
        self.submitAndAssertZIPCodeValidityInText("981 38", "Vi levererar till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("981 44", "Vi levererar till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("981 47", "Vi levererar till detta postnummer!")

    def testEmptyZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("", "Vi levererar tyvärr inte till detta postnummer!")

    def testInvalidZIPCodes(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("12345", "Vi levererar tyvärr inte till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("54321", "Vi levererar tyvärr inte till detta postnummer!")

    def testInvalidCharactersInZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("abcde", "Vi levererar tyvärr inte till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("ABCDE", "Vi levererar tyvärr inte till detta postnummer!")

    def testInvalidLengthZIPCode(self) -> None:
        self.submitAndAssertZIPCodeValidityInText("1234", "Vi levererar tyvärr inte till detta postnummer!")
        self.submitAndAssertZIPCodeValidityInText("123456", "Vi levererar tyvärr inte till detta postnummer!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
