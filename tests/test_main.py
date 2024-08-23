from seleniumbase import BaseCase
import pathlib
 
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Filsökvägen till index.htmldfs
startPage = filePath + "index.html"  
 
#testar huvuddelen av hemsidan
class testworkingWebsite(BaseCase):
    #testar att namnet på hemsidan är korrekt
    def test_Title(self):
        self.open(startPage)
        self.assert_text("Florista" , "h1")
        
    #testar att sidan tillhär företaget visas
    def test_PageMessage(self):
        self.open(startPage)
        self.assert_text("Den här hemsidan tillhör florista" , "p")