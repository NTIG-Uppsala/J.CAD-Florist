from seleniumbase import BaseCase
import pathlib
from selenium.webdriver.common.by import By

# Filsökvägen till rotmappen
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

# Filsökväg till index.html
startPage = filePath + "index.html"  

# Lista med alla sociala medier ikoner
socialMediaPaths = [
    "images/facebook.svg",
    "images/instagram.svg",
    "images/twitter.svg"
]

# Lista med länkarna till alla sociala medier
socialMediaLinks = [
    "https://www.facebook.com/ntiuppsala",
    "https://www.instagram.com/ntiuppsala/",
    "https://x.com/ntiuppsala"
    ]

# Klass för att testa footern
class test_footer(BaseCase):
    
    # Testar att footern innehåller öppettider, adress och telefonnummer
    def test_Footer(self):
        self.open(startPage)
        # Förväntade texter i footern
        expected_texts = [
            "Måndagar 10-18",
            "Tisdagar 10-18",
            "Onsdagar 10-17",
            "Torsdagar 10-17",
            "Fredagar 10-18",
            "Lördagar 12-16",
            "Söndagar 12-15",
            "1 jan - Nyårsdagen",
            "6 jan - Trettondedag jul",
            "1 maj - Första maj",
            "6 jun - Sveriges nationaldag",
            "24 dec - Julafton",
            "25 dec - Juldagen",
            "26 dec - Annandag jul",
            "31 dec - Nyårsafton",
            "Fjällgatan 32H 981 39 KIRUNA",
            "0630-555-555"
        ]

        # Kollar att alla förväntade texter finns i footern
        for text in expected_texts:
            self.assert_text(text, "footer")
        
    def test_SocialMediaLinks(self):
        # Kollar så att ikonerna finns på sidan
        self.open(startPage)
        for i in range(len(socialMediaPaths)):
            self.assert_element(f"[src=\"{socialMediaPaths[i]}\"]")
            self.assert_element(f"[href=\"{socialMediaLinks[i]}\"]")
           
