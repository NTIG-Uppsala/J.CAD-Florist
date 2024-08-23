from seleniumbase import BaseCase
import pathlib

#Path to the rootfile
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Path to index.html
startPage = filePath + "index.html"  
 

class test_index(BaseCase):

    def test_Title(self):
        self.open(startPage)
        self.assert_text("Florista" , "h1")
        
    def test_PageMessage(self):
        self.open(startPage)
        self.assert_text("Den här hemsidan tillhör florista" , "p")