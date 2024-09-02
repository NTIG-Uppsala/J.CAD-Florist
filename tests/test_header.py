from seleniumbase import BaseCase
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"  

class header_test(BaseCase):
    # Testar att loggan finns i headern
    def testLogo(self):
        self.open(startPage)
        self.assert_element(".header [src=\"images/florist_Logga.png\"]")

    # Kollar om titel finns på sidan
    def test_Title(self):
        self.open(startPage)
        self.assert_text("florista")
        
    # Kollar om texten "Den här hemsidan tillhör florista" finns på sidan
    def test_PageMessage(self):
        self.open(startPage)
        self.assert_text("Den här hemsidan tillhör florista")
