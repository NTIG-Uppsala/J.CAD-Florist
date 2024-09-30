from utils import *


class TestEssentialInformation(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="public/se/index.html")

    # Test that the name of the florist is displayed
    def testName(self) -> None:
        self.assertInText("florista")

    # Test that the address of the florist is displayed
    def testAddress(self) -> None:
        self.assertAllInText(["Fjällgatan 32H", "981 39", "KIRUNA"])

    # Test that the phone number of the florist is displayed both as text and as a link
    def testPhoneNumber(self) -> None:
        self.assertInText("0630-555-555")
        self.assertInHTML("tel:0630555555")

    # Test that the email address of the florist is displayed both as text and as a link
    def testEmail(self) -> None:
        self.assertInText("info@florista.ntig.dev")
        self.assertInHTML("mailto:info@florista.ntig.dev")

    # Test that the email address of the florist is displayed both as text as links with images
    def testSocialMedia(self) -> None:
        self.assertAllInHTML(
            [
                "facebook.com/ntiuppsala",
                "images/facebook.svg",
                "instagram.com/ntiuppsala",
                "images/instagram.svg",
                "x.com/ntiuppsala",
                "images/twitter-x.svg",
            ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
