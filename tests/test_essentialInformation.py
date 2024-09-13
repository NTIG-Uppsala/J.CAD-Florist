from utils import *


class TestEssentialInformation(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    def testName(self) -> None:
        self.assertInText("florista")

    def testAddress(self) -> None:
        self.assertAllInText(["Fjällgatan 32H", "981 39", "KIRUNA"])

    def testPhoneNumber(self) -> None:
        self.assertInText("0630-555-555")
        self.assertInHTML("tel:0630555555")

    def testSocialMedia(self) -> None:
        self.assertAllInHTML(
            [
                "facebook.com/ntiuppsala",
                "images/icons8-facebook.svg",
                "instagram.com/ntiuppsala",
                "images/icons8-instagram.svg",
                "x.com/ntiuppsala",
                "images/icons8-twitterx.svg",
            ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
