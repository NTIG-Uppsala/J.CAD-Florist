from seleniumbase import BaseCase
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"

class test_carousel(BaseCase):
    def testCarousel(self):
        self.open(startPage)
        self.switch_to_frame('iframe[name="product"]')
        for i in range(1,7):
            self.assert_element('div.carousel-item:nth-child('+str(i)+')')