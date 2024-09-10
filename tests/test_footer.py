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
    "images/icons8-facebook.svg",
    "images/icons8-instagram.svg",
    "images/icons8-twitterx.svg",
]

# Lista med länkarna till alla sociala medier
socialMediaLinks = [
    "https://www.facebook.com/ntiuppsala",
    "https://www.instagram.com/ntiuppsala/",
    "https://x.com/ntiuppsala",
    ]

# Klass för att testa footern
class test_footer(BaseCase):
    
    # Testar att footern innehåller öppettider, adress och telefonnummer
    def test_Footer(self):
        self.open(startPage)
        # Förväntade texter i footern
        expected_texts = [
            "Måndag",
            "Tisdag",
            "Onsdag",
            "Torsdag",
            "Fredag",
            "Lördag",
            "Söndag",
            "10-18",
            "10-18",
            "10-17",
            "10-17",
            "10-18",
            "12-16",
            "12-15",
            "1 jan",
            "6 jan",
            "1 maj",
            "6 jun",
            "24 dec",
            "25 dec",
            "26 dec",
            "31 dec",
            "Nyårsdag",
            "Trettondag",
            "Första maj",
            "Nationaldag",
            "Julafton",
            "Juldagen",
            "Annandag jul",
            "Nyårsafton",
            "Fjällgatan 32H 981 39 KIRUNA",
            "0630-555-555",
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
           
