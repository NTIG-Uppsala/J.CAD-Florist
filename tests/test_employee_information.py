from utils import *


class TestEmployeeInformation(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Check that the employee names are displayed
    def testEmployeeNames(self) -> None:
        self.assertAllInText(["Fredrik", "Örjan", "Anna"])

    # Check that the employee last names are displayed
    def testEmployeeLastNames(self) -> None:
        self.assertAllInText(["Örtqvist", "Johansson", "Pettersson"])

    # Check that the roles are displayed
    def testEmployeeRoles(self) -> None:
        self.assertAllInText(["Ägare", "Florist", "Hortonom"])

    # Check that the images are displayed
    def testEmployeeImages(self) -> None:
        self.assertAllInHTML(["images/272x408/fredrik-ortqvist.jpg", "images/272x408/orjan-johansson.jpg", "images/272x408/anna-pettersson.jpg"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
