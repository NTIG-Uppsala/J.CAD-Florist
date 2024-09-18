from utils import *


class TestEmployeeInformation(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Check that the employee names are displayed
    def testEmployeeNames(self) -> None:
        self.assertAllInText(["Fredrik", "Örjan", "Anna"])

    # Check that the roles are displayed
    def testEmployeeRoles(self) -> None:
        self.assertAllInText(["Ägare", "Florist", "Hortonom"])

    # Check that the images are displayed
    def testEmployeeImages(self) -> None:
        self.assertAllInHTML(["images/fredrik_ortqvist.jpg", "images/orjan_johansson.jpg", "images/anna_pettersson.jpg"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
