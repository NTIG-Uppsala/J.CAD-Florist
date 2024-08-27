from seleniumbase import BaseCase
import pathlib
from selenium.webdriver.common.by import By

#filsökvägen till rotmappen
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#filsökväg till index.html
startPage = filePath + "index.html"  

#lista med alla sociala medier ikoner
socialMediaPaths = [
    "images/facebook.svg",
    "images/instagram.svg",
    "images/twitter.svg"
]

#lista med länkarna till alla sociala medier
socialMediaLinks = [
    "https://www.facebook.com/ntiuppsala",
    "https://www.instagram.com/ntiuppsala/",
    "https://x.com/ntiuppsala"
    ]

#klass för att testa footern
class footer_test(BaseCase):
    
    #testar att footern innehåller öppettider, adress och telefonnummer
    def testFooter(self):
        self.open(startPage)
        #förväntade texter i footern
        expected_texts = [
            "Måndagar 10-18",
            "Tisdagar 10-18",
            "Onsdagar 10-17",
            "Torsdagar 10-17",
            "Fredagar 10-28",
            "Lördagar 12-16",
            "Söndagar 12-15",
            "Nyårsdagen 1 Januari",
            "Trettondedag jul 6 Januari",
            "Första maj 1 Maj",
            "Sveriges nationaldag 6 Juni",
            "Julafton 24 December",
            "Juldagen 25 December",
            "Annandag jul 26 December",
            "Nyårsafton 31 December",
            "Fjällgatan 32H 981 39 KIRUNA",
            "0630-555-555"
        ]

        #kollar att alla förväntade texter finns i footern
        for text in expected_texts:
            self.assert_text(text, "footer")
        
    def testSocialMediaLinks(self):
        #Kollar så att ikonerna finns på sidan
        for i in range(len(socialMediaPaths)):
            self.open(startPage)
            #klickar på iknerna
            self.click(f"[src=\"{socialMediaPaths[i]}\"]")
            
            #kontrollerar att vi hamnar på rätt sida
            current_url = self.get_current_url()
            if (self.get_current_url() != socialMediaLinks[i]):
                print(f"Expected URL: {socialMediaLinks[i]}, but got: {current_url}")
                raise NameError("Link does not lead to the right place")
