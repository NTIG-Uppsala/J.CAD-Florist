from utils import *


class TestMapEmbed(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the OSM map is displayed correctly
    def testMapEmbed(self) -> None:
        self.checkNumberOfElements("#map", 1)
        self.checkNumberOfElements(".leaflet-container", 1)
        self.checkNumberOfElements(".leaflet-pane", 7)
        self.checkNumberOfElements(".leaflet-control-container", 1)
        self.checkNumberOfElements(".leaflet-map-pane", 1)
        self.checkNumberOfElements("img.leaflet-marker-icon", 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
