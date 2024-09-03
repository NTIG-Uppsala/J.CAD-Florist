from seleniumbase import BaseCase
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"  

class header_test(BaseCase):
    #testar att all info finns på headern
    def testHeaderInfo(self):
        self.open(startPage)
        self.assert_element(".header [src=\"images/logga_florist.png\"]")
        self.assert_text("florista")
        self.assert_text("Den här hemsidan tillhör florista")

