from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"  


#lista med korrekta postnummer
correctPostalCodes = [
    "12345",
    "54321",
    "00000",
    "99999",
    "123 45",
    "12345",
    "12345",
]

#lista av testfall som ska köras i blommogrammet
testCases = [
    #inkorrekt postnummer
    "12345",
    #bokstäver istället för siffror
    "abcde",
    #storat bokstäver
    "ABCDE",
    #för kort postnummer
    "1234",
    #för långt postnummer
    "123456",
    #tomt postnummer
    "",
    #postnummer med mellanslag
    "1 23 4 5 ",
    #postnummer med bindestreck
    "123-45",
    #postnummer med punkt
    "123.45",
]

class test_index(BaseCase):
    # Kollar om bilderna finns på sidan
    def test_Images(self):
        self.open(startPage)
        for i in range(1, 4):
            print("bild"+str(i))
            self.assert_element(f"[src=\"images/bild{i}.jpg\"]")
    
    
    def test_flowerGram(self):
        self.open(startPage)
        # Kollar om texten "Skicka blommogram" finns på sidan
        self.assert_text("Skicka blommogram")
        
        #Provar att skriva in alla testcases i inputfältet och klickar på knappen
        for postalCode in testCases:
            self.type("#postalCode", postalCode)
            self.click('button')
            self.assert_text("Felaktigt postnummer")
        
        #Provar att skriva in alla korrekta postnummer i inputfältet och klickar på Enter istället
        for postalCode in correctPostalCodes:
            self.type("#postalCode", postalCode)
            self.get_element("#postalCode").send_keys(Keys.ENTER)
            self.assert_text("Tack for din beställning!")
         