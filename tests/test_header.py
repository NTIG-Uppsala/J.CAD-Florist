from seleniumbase import BaseCase
import pathlib

#Path to the rootfile
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Path to index.html
startPage = filePath + "index.html"  

class footer_test(BaseCase):
    #testar att loggan finns i headern
    def testLogo(self):
        self.open(startPage)
        self.assert_element(".header [src=\"images/instagram.svg\"]")
