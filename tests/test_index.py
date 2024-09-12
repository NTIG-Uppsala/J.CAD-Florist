from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"  




class test_index(BaseCase):
    # Kollar om bilderna finns på sidan
    def test_Images(self):
        self.open(startPage)
        for i in range(1, 4):
            print("bild"+str(i))
            self.assert_element(f"[src=\"images/bild{i}.jpg\"]")
    
    #Kollar om texten finns på sidan
    def test_flowerGramText(self):
        self.open(startPage)
        self.click("h4[onclick='flowerGramPopUp()']")
        # List of expected texts
        expected_texts = [
            "Överraska med ett blommogram",
            "Vill du skicka ett blommogram?",
            "Besök oss i butiken eller ring oss på 0630-555-555!",
            "Kontrollera här om vi levererar till ditt önskade postnummer:",
        ]
        # Loop through the expected texts and assert each one
        for text in expected_texts:
            self.assert_text(text)

    # Testar att skriva in postnummer i inputfältet
    def test_flowerGramInput(self):
        #lista med korrekta postnummer
        correctPostalCodes = [
            "981 38",
            "981 44	",
            "981 47"
        ]

        #lista av testfall som ska köras i blommogrammet
        testCases = [
            #inkorrekt postnummer
            "123 45",
            #bokstäver istället för siffror
            "abcde",
            #stora bokstäver
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

        self.open(startPage)
        self.click("h4[onclick='flowerGramPopUp()']")
        #Provar att skriva in alla testcases i inputfältet och klickar på knappen
        for postalCode in testCases:
            self.type("#postalCode", postalCode)
            self.click('button')
            self.assert_text("Vi levererar tyvärr inte till detta postnummer!")
        
        #Provar att skriva in alla korrekta postnummer i inputfältet och klickar på Enter istället
        for postalCode in correctPostalCodes:
            self.type("#postalCode", postalCode)
            self.get_element("#postalCode").send_keys(Keys.ENTER)
            self.assert_text("Vi levererar till detta postnummer!")