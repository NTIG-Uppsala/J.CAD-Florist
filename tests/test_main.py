from seleniumbase import BaseCase
 
import pathlib
 
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")
 
startPage = filePath + "index.html"  # Path to index.html
 
class testworkingWebsite(BaseCase):

    def test_Title(self):
        self.open(startPage)
        self.assert_text("Florista" , "h1")
        
    def test_PageMessage(self):
        self.open(startPage)
        self.assert_text("Den här hemsidan tillhör florista" , "p")