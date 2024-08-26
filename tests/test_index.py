from seleniumbase import BaseCase
import pathlib

#Path to the rootfile
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Path to index.html
startPage = filePath + "index.html"  
 

class test_index(BaseCase):
    #kollar om bilderna finns på sidan
    def test_Images(self):
        self.open(startPage)
        for i in range(1, 4):
            print("bild"+str(i))
            self.assert_element(f"[src=\"images/bild{i}.jpg\"]")