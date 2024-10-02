from utils import *


class TestNorwegian(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/no/index.html")

    # Check that the page contains information in Norwegian
    def testPage(self) -> None:
        self.assertAllInText(
            [
                "Produkter",
                "Kart",
                "Butikkpersonale",
                "Kontakt oss",
                "Åpningstider",
                "Stengte dager",
            ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
