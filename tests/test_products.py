from seleniumbase import BaseCase
import pathlib

filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  

class test_Products(BaseCase):
    def testProduct(self):
        self.open(startPage)
        for i in range(1, 7):
            self.assert_element('.product:nth-child(' + str(i) + ')', timeout=1)