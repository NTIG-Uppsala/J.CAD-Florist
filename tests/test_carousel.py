from seleniumbase import BaseCase
import pathlib

filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  

class test_carousel(BaseCase):
    def test_carousel_items_count(self):
        self.open(startPage)
        
        # använder javascript för att räkna antalet items i carouselen
        num_items = self.execute_script("return document.querySelectorAll('div.carousel-track > div.carousel-item').length;")
        
        #kollar att det är antigen 6 eller 9 items i carouselen, den kollar efter båda för att det kan vara
        #antingen 6 eller 9 element beroende på om elementen har blivit klonade i carousel.js eller inte
        self.assert_true(num_items in [6, 9], "There should be either 6 or 9 carousel items")