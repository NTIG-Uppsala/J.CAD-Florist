from utils import *


class TestEnglish(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/en/index.html")

    # Check that the page contains information in English
    def testPage(self) -> None:
        self.assertAllInText(["Products", "Map", "Staff", "Contact us", "Opening hours", "Closed days"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
